# Deuces-numpy
Numpy version of deuces.
See parent project page for details: https://github.com/worldveil/deuces.

## Installation

```
$ pip install deuces-numpy
```

## Implementation notes

Deuces-numpy currently handles only 7 card hand lookups (via evaluate method).
Some extra functionality provided:
- evaluate_hands5(self, hands)
- simulate_hands(self, n_sims, n_cards=5, deck=Deck.GetFullDeck()
- simulate_games(self, cards, n_players, n_sims)
- analyze_hand(self, hand, n_players, n_sims) - Monte Carlo simulation for Texas Holdem.

## Usage

```python
from deuces_numpy import Deck, EvaluatorNumpy
deck = Deck()
board = deck.draw(5)
player1_hand = deck.draw(2)
player2_hand = deck.draw(2)
evaluator = EvaluatorNumpy()
hands = np.array([board + player1_hand, board + player2_hand])
scores = evaluator.evaluate(hands)
print(scores)
```

## License

Copyright (c) 2013 Will Drevo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
