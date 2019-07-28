from deuces import Card, EvaluatorNumpy, Deck
import numpy as np

# create a card
card = Card.new('Qh')

# create a board and hole cards
board = [
    Card.new('2h'),
    Card.new('2s'),
    Card.new('Jc')
]
hand = [
    Card.new('Qs'),
    Card.new('Th')
]

# pretty print cards to console
Card.print_pretty_cards(board + hand)

# create an evaluator
evaluator = EvaluatorNumpy()

# and rank your hand
rank = evaluator.evaluate_hands5(np.array([board + hand]))
print(rank)
# or for random cards or games, create a deck
print("Dealing a new hand...")
deck = Deck()
board = deck.draw(5)
player1_hand = deck.draw(2)
player2_hand = deck.draw(2)

print("The board:")
Card.print_pretty_cards(board)

print("Player 1's cards:")
Card.print_pretty_cards(player1_hand)

print("Player 2's cards:")
Card.print_pretty_cards(player2_hand)

hands = np.array([board + player1_hand, board + player2_hand])

scores = evaluator.evaluate(hands)
p1_score, p2_score = scores

# bin the scores into classes
p1_class = evaluator.get_rank_class(p1_score)
p2_class = evaluator.get_rank_class(p2_score)

# or get a human-friendly string to describe the score
print(f"Player 1 hand rank = {p1_score} {evaluator.class_to_string(p1_class)}")
print(f"Player 2 hand rank = {p2_score} {evaluator.class_to_string(p2_class)}")

# or just a summary of the entire hand
# hand_summary doesn't work
# hands = [player1_hand, player2_hand]
# evaluator.hand_summary(board, hands)
