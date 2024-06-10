def display_contacts(contacts):
    if not contacts:
        print("No contacts in the contact book.")
    else:
        print("Contact Book:")
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contacts[name] = phone
    print("Contact added.")

def remove_contact(contacts):
    name = input("Enter the name of the contact to remove: ")
    if name in contacts:
        del contacts[name]
        print(f"Removed contact: {name}")
    else:
        print("Contact not found.")

def main():
    contacts = {}
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. View Contacts")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            remove_contact(contacts)
        elif choice == '3':
            display_contacts(contacts)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
