import random
import string


def get_yes_no(prompt):
    while True:
        answer = input(prompt + " (y/n): ").strip().lower()

        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("Please enter only 'y' or 'n'.")


def get_password_length():
    while True:
        try:
            length = int(input("Enter password length: "))

            if length < 8:
                print("For better security, use at least 8 characters.")
            else:
                return length

        except ValueError:
            print("Please enter a valid number.")


def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""

    if use_letters:
        characters += string.ascii_letters

    if use_numbers:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    if characters == "":
        return None

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


def check_password_strength(password):
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_number = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if has_lower and has_upper:
        score += 1
    if has_number:
        score += 1
    if has_symbol:
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


def main():
    print("=" * 50)
    print("RANDOM PASSWORD GENERATOR")
    print("=" * 50)

    length = get_password_length()

    use_letters = get_yes_no("Include letters?")
    use_numbers = get_yes_no("Include numbers?")
    use_symbols = get_yes_no("Include symbols?")

    password = generate_password(length, use_letters, use_numbers, use_symbols)

    if password is None:
        print("You must choose at least one character type.")
        return

    strength = check_password_strength(password)

    print("\nGenerated Password:")
    print(password)

    print("\nPassword Strength:")
    print(strength)

    print("\nRandom Password Tip:")
    print("Use long, unique passwords and avoid reusing the same password across websites.")


if __name__ == "__main__":
    main()