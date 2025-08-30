# PRODIGY_CS_03
A Python script to check the strength of your password. It evaluates length, uppercase, lowercase, digits, and special characters. Based on these factors, it provides a strength rating (Very Weak to Very Strong) and offers tips to improve your password’s security.
# Password Strength Checker

This Python script checks the strength of a given password and provides feedback on how to improve it. The strength evaluation considers the following factors:

- Length of the password
- Presence of uppercase letters
- Presence of lowercase letters
- Presence of numbers
- Presence of special characters (e.g., `!@#$%^&*`)

The script provides a rating based on these factors, ranging from **Very Weak** to **Very Strong**. It also offers tips to help you create a more secure password.

## Features

- **Length Check**: Passwords should be at least 8 characters long, but 12 or more is better.
- **Character Variety**: Includes checks for uppercase, lowercase, digits, and special characters.
- **Rating System**: Your password gets a rating based on these checks: `Very Weak`, `Weak`, `Moderate`, `Strong`, or `Very Strong`.
- **Suggestions**: If your password is weak, you'll get specific tips to make it stronger.

## How to Use

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/password-strength-checker.git
    ```

2. Navigate to the project directory:

    ```bash
    cd password-strength-checker
    ```

3. Run the script:

    ```bash
    python password_checker.py
    ```

4. Enter a password when prompted. The script will display its strength and provide suggestions if needed.

5. To exit the program, type `exit`.

## Example Usage

```bash
=== Password Checker ===
type 'exit' to quit

Enter a password: mySecureP@ssw0rd123

Strength: Very Strong
Nice! Your password looks solid.
-------------------------

Enter a password: weakpassword

Strength: Very Weak
Suggestions:
→ Make it at least 8 chars long (12+ is better).
→ Add an uppercase letter (A-Z).
→ Add some numbers (0-9).
→ Use a special symbol (!@#$ etc).
-------------------------
