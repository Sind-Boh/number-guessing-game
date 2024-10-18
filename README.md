# Number Guessing Game
## Introduction
CLI-based game, where you can try to guess random number from 1 to 100.
### Features:
<ul>
  <li>There are 3 difficulty levels: easy, normal and hard</li>
  <li>There are two types of hints: small hint after each guess that tells prayer eather his guess is higher or lowel than random number; and final hint before last try that tells player boundaries of random number (+-5)</li>
  <li>Game can be played multiple times</li>
</ul>
Sample solution for project "Number Guessing Game" provided by Roadmap.sh:

[https://roadmap.sh/projects/number-guessing@game](https://roadmap.sh/projects/number-guessing-game)
## How to run
1. Clone the Repository:

```bash
git clone https://github.com/Sind-Boh/number-guessing-game
```
2. Run main.py with python
```bash
python main.py
```
## How to play
- Run main.py by using CLI. You will see the welcome text, rules & difficulty levels
- Choose desired difficulty level by entering 1, 2 or 3
- Enter your guess
- If your guess is incorrect, you will receive a small hint "Number is bigger/smaller than your guess"
- Before your last chance you can get final major hint.
- Enter "y" to get the hint "Your number is lower than x and bigger than y"
- You can skip final hint by entering "n"
- If you guess correctly - you will see the "Congrats!" message
- If you loose - you will see the message "You lost! Answer: X"
- After that by entering "y" or "n" you can choose "Do you wanna play again?"

## Technical detailes
Game build using Python and Random library
## Requirements
Python 3.12 or higher
