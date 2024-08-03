import pickle

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name}, Phone: {self.phone}, Email: {self.email}"

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact added: {contact}")

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact removed: {contact}")
                return True
        return False

    def list_contacts(self):
        if not self.contacts:
            print("No contacts in the address book.")
        else:
            print("Contacts in the address book:")
            for contact in self.contacts:
                print(contact)

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)
    print(f"Address book saved to {filename}")

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        print(f"No such file: {filename}. Starting with an empty address book.")
        return AddressBook() 
    except Exception as e:
        print(f"An error occurred while loading the address book: {e}")
        return AddressBook()

def main():
    book = load_data()

    while True:
        print("\nAddress Book Menu:")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. List Contacts")
        print("4. Save and Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contact = Contact(name, phone, email)
            book.add_contact(contact)
        elif choice == "2":
            name = input("Enter name of contact to remove: ")
            if not book.remove_contact(name):
                print(f"No contact found with the name {name}.")
        elif choice == "3":
            book.list_contacts()
        elif choice == "4":
            save_data(book)
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
