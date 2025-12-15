# Password Strength Tool

A Python-based password strength analyzer that estimates the time required to brute-force a password. It mathematically calculates entropy and checks for common weak patterns and dictionary words.

## Features

* **Brute-Force Estimation:** Mathematically calculates the time to crack a password based on search space size and attack speed.
* **Pattern Recognition:** Detects common weak patterns (e.g., repeated characters, sequences).
* **Dictionary Checks:** Flags common words that make passwords vulnerable to dictionary attacks.
* **Detailed Feedback:** Provides actionable advice on how to improve password strength.

## How It Works

The tool calculates the "entropy" of your password using the formula:
$E = \log_2(R^L)$

Where:
* **R** is the pool of unique characters used (lowercase, uppercase, digits, symbols).
* **L** is the length of the password.

It then divides the total combinations by an estimated hashrate (guesses per second) to determine the time to crack.

## Prerequisites

* [Python 3.x](https://www.python.org/downloads/)

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/avayunus/password_strength_tool.git](https://github.com/avayunus/password_strength_tool.git)
    cd password_strength_tool
    ```

2.  **Run the tool:**
    ```bash
    python main.py
    ```

## Usage

Run the script and enter a password when prompted. The tool will output:
* A strength score (e.g., Weak, Moderate, Strong).
* Estimated time to crack.
* Specific suggestions for improvement.

## Disclaimer

This tool is for educational and self-assessment purposes only. The "time to crack" is an estimation based on general computing power and does not account for specific breaches, quantum computing, or massive distributed botnets.
