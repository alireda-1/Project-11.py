# Coin Guessing Game

An interactive **Python** script that simulates a coin toss and lets the user guess whether the result will be heads or tails.

## Features
- **Two Toss Methods:** Choose between `random.randint()` and `random.random()` to generate the coin toss.
- **Case-Insensitive Guesses:** Uses `.lower()` so guesses such as `Heads` and `TAILS` are accepted.
- **Input Validation:** Checks that the selected method is `1` or `2` and that the guess is either heads or tails.
- **Win/Loss Feedback:** Compares the guess with the toss result and displays the outcome.

## Technologies Used
- Python 3
- `random` module
