from . import Deck
from . import Evaluator
import numpy as np
import scipy.special
import itertools

def comb_index(n, k):
    count = scipy.special.comb(n, k, exact=True)
    combs_iter = itertools.combinations(range(n), k)
    combs_flat_iter = itertools.chain.from_iterable(combs_iter)
    index = np.fromiter(combs_flat_iter, dtype=int, count=count*k)
    return index.reshape(-1, k)


class EvaluatorNumpy(Evaluator):
    combos_seven_index = comb_index(7, 5)

    def simulate_hands(self, n_sims, n_cards=5, deck=Deck.GetFullDeck()):
        deck = np.array(deck)
        decks = np.tile(deck, n_sims).reshape(n_sims, -1)
        for i in range(len(decks)):
            np.random.shuffle(decks[i])
        hands = decks[:, :n_cards]
        return hands

    def simulate_games(self, cards, n_players, n_sims):
        '''
        cards: array of pocket and community cards
        returns: array of hands (n_sims, n_players, 7)
        '''
        n_cards = len(cards)
        left_cards = 7 - n_cards
        n_comm = max(n_cards - 2, 0)
        left_comm = 5 - n_comm
        left_pock = max(2 - n_cards, 0)

        deck = Deck.GetFullDeck()
        for card in cards:
            deck.remove(card)
        deck = np.array(deck)
        decks = np.tile(deck, n_sims).reshape(n_sims, -1)
        for i in range(len(decks)):
            np.random.shuffle(decks[i])

        games = np.empty(shape=(n_sims, n_players, 7), dtype=int)
        games[:, 0, :n_cards] = cards
        games[:, 0, n_cards:] = decks[:, :left_cards]

        if n_comm > 0:
            games[:, 1:, 2:n_cards] = cards[2:]
        for i in range(n_players-1):
            start = left_cards + i*2
            games[:, i+1, :2] = decks[:, start:start+2]
            games[:, i+1, 2+n_comm:7] = decks[:, left_pock:left_pock+left_comm]

        # print(cards, 'cards')
        # print(decks, 'decks')
        # print(games, 'games')
        return games

    def calc_primes_products(self, hands):
        return np.prod(hands & 0xFF, axis=-1)

    def check_suited(self, hands):
        suited = (np.bitwise_and.reduce(hands, axis=1) & 0xF000).astype(bool)
        return suited

    def get_scores(self, prime_prods, suited):
        scores = np.empty_like(prime_prods)
        for i, prod in enumerate(prime_prods):
            if suited[i]:
                scores[i] = self.table.flush_lookup[prod]
            else:
                scores[i] = self.table.unsuited_lookup[prod]
        return scores

    def evaluate_hands5(self, hands):
        prods = self.calc_primes_products(hands)
        suited = self.check_suited(hands)
        scores = self.get_scores(prods, suited)
        return scores

    def evaluate(self, hands):
        combos = hands[:, self.combos_seven_index]
        scores = self.evaluate_hands5(combos.reshape(-1, combos.shape[-1]))
        scores = scores.reshape(len(combos), -1).min(axis=1)
        return scores

    def analyze_hand(self, hand, n_players, n_sims):
        '''
        hand: array of known cards
        returns: array [win_odds, tie_odds_2pls, ...]
        '''
        games = self.simulate_games(hand, n_players, n_sims)
        scores = self.evaluate(games.reshape(-1, 7)).reshape(n_sims, n_players)
        winners_scores = scores.min(axis=1)
        winners = np.empty_like(scores, dtype=bool)
        for i in range(n_players):
            winners[:, i] = scores[:, i] == winners_scores
        winners_number = winners.sum(axis=1)
        win_ties_odds = np.empty(shape=n_players, dtype=float)
        for i in range(1, n_players+1):
            is_one_of_i_winners = winners[:, 0] & (winners_number == i)
            win_ties_odds[i-1] = is_one_of_i_winners.sum() / n_sims

        # print(scores, 'scores')
        # print(winners_scores, 'winners_scores')
        # print(winners, 'winners')
        # print(winners_number, 'winners_number')
        return win_ties_odds
