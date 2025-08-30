import re

def check_password(pwd):
    score = 0
    tips = []

    # length
    if len(pwd) >= 12:
        score += 2
    elif len(pwd) >= 8:
        score += 1
    else:
        tips.append("→ Make it at least 8 chars long (12+ is better).")

    # upper case
    if re.search(r"[A-Z]", pwd):
        score += 1
    else:
        tips.append("→ Add an uppercase letter (A-Z).")

    # lower case
    if re.search(r"[a-z]", pwd):
        score += 1
    else:
        tips.append("→ Add a lowercase letter (a-z).")

    # numbers
    if re.search(r"\d", pwd):
        score += 1
    else:
        tips.append("→ Add some numbers (0-9).")

    # special chars
    if re.search(r"[\W_]", pwd):
        score += 1
    else:
        tips.append("→ Use a special symbol (!@#$ etc).")

    # rating
    if score <= 2:
        rating = "Very Weak"
    elif score == 3:
        rating = "Weak"
    elif score == 4:
        rating = "Moderate"
    elif score == 5:
        rating = "Strong"
    else:
        rating = "Very Strong"

    return rating, tips


def main():
    print("=== Password Checker ===")
    print("type 'exit' to quit\n")

    while True:
        try:
            pwd = input("Enter a password: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nBye!")
            break

        if pwd.lower() == "exit":
            print("Goodbye!")
            break

        if not pwd:
            print("Empty password, try again.\n")
            continue

        rating, tips = check_password(pwd)
        print(f"\nStrength: {rating}")
        if tips:
            print("Suggestions:")
            for t in tips:
                print(t)
        else:
            print("Nice! Your password looks solid.")
        print("-" * 25 + "\n")


if __name__ == "__main__":
    main()
