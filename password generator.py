import random
import string

def generate_password(length=8, uppercase=True, lowercase=True, digits=True, special_chars=False):
    characters = ""

    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if not characters:
        print("No character sets selected.")
        return

    password = random.choices(characters, k=length)
    password = ''.join(password)

    return password

def main():
    print("Password Generator")
    print("------------------")

    while True:
        print("\nPlease select the desired options:")
        print("1. Generate password")
        print("2. Quit")

        choice = input("Your choice: ")

        if choice == '1':
            length = int(input("Enter the length of the password: "))
            uppercase = input("Use uppercase letters? (yes/no): ").lower() == 'yes'
            lowercase = input("Use lowercase letters? (yes/no): ").lower() == 'yes'
            digits = input("Use digits? (yes/no): ").lower() == 'yes'
            special_chars = input("Use special characters? (yes/no): ").lower() == 'yes'

            password = generate_password(length, uppercase, lowercase, digits, special_chars)
            print("Generated password:", password)

        elif choice == '2':
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()
