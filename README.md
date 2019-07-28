# Deuces-numpy
Numpy version of deuces.
See parent project page for details: https://github.com/worldveil/deuces.

## Installation

```
$ pip install deuces-numpy
```

## Implementation notes

Deuces-numpy currently handles only 7 card hand lookups (via evaluate method). This is not just a wrapper, the whole score calculation is rewritten in numpy so it's really fast. Original lookup tables are used.

Some extra functionality provided:
- evaluate_hands5(self, hands)
- simulate_hands(self, n_sims, n_cards=5, deck=Deck.GetFullDeck()
- simulate_games(self, cards, n_players, n_sims)
- analyze_hand(self, hand, n_players, n_sims) - Monte Carlo simulation for Texas Holdem.

## Usage

```python
from deuces_numpy import Deck, EvaluatorNumpy
import numpy as np
deck = Deck()
board = deck.draw(5)
player1_hand = deck.draw(2)
player2_hand = deck.draw(2)
evaluator = EvaluatorNumpy()
hands = np.array([board + player1_hand, board + player2_hand])
scores = evaluator.evaluate(hands)
print(scores)
```

## Related

See also https://github.com/grabantot/numpy_shuffle_row_wise.

## Benchmark

```python
from deuces_numpy import EvaluatorNumpy
import time
evaluator = EvaluatorNumpy()
hands = evaluator.simulate_hands(250000, 7)
t = time.time()
evaluator.evaluate(hands)
print(time.time() - t)
```
