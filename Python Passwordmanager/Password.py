import json
import getpass

PASSWORDS_FILE = 'passwords.json'

def load_passwords():
    try:
        with open(PASSWORDS_FILE, 'r') as file:
            passwords = json.load(file)
    except FileNotFoundError:
        passwords = {}
    
    return passwords

def save_passwords(passwords):
    with open(PASSWORDS_FILE, 'w') as file:
        json.dump(passwords, file, indent=4)

def add_password(passwords):
    service = input("Service: ")
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    passwords[service] = {
        'username': username,
        'password': password
    }

    save_passwords(passwords)
    print(f"Password for {service} added successfully.")

def get_password(passwords):
    service = input("Service: ")
    if service in passwords:
        account = passwords[service]
        print(f"Username: {account['username']}")
        print(f"Password: {account['password']}")
    else:
        print(f"No password found for {service}.")

def list_services(passwords):
    if passwords:
        print("List of services:")
        for service in passwords:
            print(service)
    else:
        print("No passwords saved.")

def main():
    passwords = load_passwords()

    while True:
        print("Menu:")
        print("1. Add a password")
        print("2. Get a password")
        print("3. List services")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_password(passwords)
        elif choice == '2':
            get_password(passwords)
        elif choice == '3':
            list_services(passwords)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

    print("Goodbye!")

if __name__ == "__main__":
    main()
1