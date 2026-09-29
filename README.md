# Life Checker (Life Predictor Game)

## About the Student

| | |
|---|---|
| **Name** | Divyansh |
| **Registration No.** | 26BCE11446 |
| **Branch** | Computer Science and Engineering (CSE) |
| **University** | VIT Bhopal University |

---

## Overview

Life Checker is a small Python console game that asks 15 Yes/No questions about personal life, habits and goals, and then tells you, just for fun, how your life is going.

Every question is written so that **"Yes" is a good sign**. The questions come in a **random order** every time the game is played. After the last answer, the program counts the good answers, changes the score into a percent, and shows one life result with a short motivational message.

> This game is only for fun. It is not a real prediction.

## Features

- 15 Yes/No questions about personal life and habits
- Questions come in a new random order in every game
- Accepts `Yes`, `yes`, `YES`, `y`, `No`, `no`, `n` (capital letters and extra spaces are ignored)
- Any wrong input (like `hello`) is taken as **No**, and the player is told
- 9 different life results, from "perfect life" to "much bad case", each with its own message
- Runs in the terminal, with no extra library to install

## Technologies / Tools Used

| Tool | Use |
|------|-----|
| Python 3 | Programming language |
| `random` module (built in) | Shuffles the questions |
| `array` module (built in) | Stores each answer as 1 (Yes) or 0 (No) |
| List, Dictionary | Store the questions and the answers |
| Functions, loops, `if / elif / else` | Ask questions, count the score, choose the result |
| Terminal / Command Prompt | To run the game |

## Project Structure

```
project/
├── life_checker.py      # the game (main file)
└── README.md            # this file
```

## Steps to Install and Run

**1. Install Python 3**
- Download it from https://www.python.org/downloads/ and install it.
- On Windows, tick **"Add Python to PATH"** during the installation.
- Check that it works by typing `python --version` in a terminal. (On macOS or Linux, use `python3 --version`.)

**2. Get the project**
- Download or copy the project folder, so that `life_checker.py` is on your computer.

**3. Open a terminal in the project folder**
- Windows: open the folder, click the address bar, type `cmd` and press Enter.
- macOS / Linux: open Terminal and use `cd` to go to the folder.

**4. Run the game**
- Type `python life_checker.py` and press Enter. (On macOS or Linux, use `python3 life_checker.py`.)

**5. Play**
- Read each question, type `Yes` or `No`, and press Enter.
- After question 15, your final life result is shown.

No extra installation (`pip install`) is needed, because `random` and `array` come with Python.

## Instructions for Testing

Run the game by hand and check that the output matches the "Expected result" column.

| # | Test | What to type | Expected result |
|---|------|--------------|-----------------|
| 1 | All Yes | `yes` 15 times | Score 100% → "perfect life u are living..." |
| 2 | All No | `no` 15 times | Score 0% → "aah u are in a much bad case" |
| 3 | Mixed answers | `yes` 12 times, `no` 3 times | Score 80% → "u are just amazing..." |
| 4 | Short and capital answers | `y`, `YES`, `n`, `No` | All are accepted, no error message |
| 5 | Wrong input | `hello` (or just press Enter) | Shows `Invalid input, taking No.` and counts it as No |
| 6 | Random order | Play the game two times | The questions come in a different order each time |

**How the score becomes a result** (15 questions, tested with this project):

| Yes answers | Percent | Life result starts with |
|-------------|---------|--------------------------|
| 15 or 14 | 100% / 93% | perfect life u are living... |
| 13 or 12 | 87% / 80% | u are just amazing... |
| 11 | 73% | your life is going great... |
| 10 or 9 | 67% / 60% | your life is good, but you are not using your full power yet |
| 8 | 53% | u are little bit exhausted... |
| 7 or 6 | 47% / 40% | your life is like a roller coaster... |
| 5, 4 or 3 | 33% / 27% / 20% | your life is not much bad but u can improve |
| 2, 1 or 0 | 13% / 7% / 0% | aah u are in a much bad case |

## Screenshots

Screenshots of the program output are uploaded in the project file.
