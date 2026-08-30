def display_menu():
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")


def add_contact(contact_book):
    name = input("Enter contact name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    if name in contact_book:
        print("Contact already exists!")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    contact_book[name] = {"phone": phone, "email": email, "address": address}
    print("Contact added successfully!")


def view_contact(contact_book):
    name = input("Enter contact name to view: ").strip()
    if name in contact_book:
        contact = contact_book[name]
        print(f"\nName: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")
    else:
        print("Contact not found!")


def edit_contact(contact_book):
    name = input("Enter contact name to edit: ").strip()
    if name in contact_book:
        print("Leave blank to keep existing value.")
        phone = input(f"Enter new phone [{contact_book[name]['phone']}]: ").strip()
        email = input(f"Enter new email [{contact_book[name]['email']}]: ").strip()
        address = input(f"Enter new address [{contact_book[name]['address']}]: ").strip()

        if phone == "":
            phone = contact_book[name]["phone"]
        if email == "":
            email = contact_book[name]["email"]
        if address == "":
            address = contact_book[name]["address"]

        contact_book[name] = {"phone": phone, "email": email, "address": address}
        print("Contact updated successfully!")
    else:
        print("Contact not found!")


def delete_contact(contact_book):
    name = input("Enter contact name to delete: ").strip()
    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")


def list_all_contacts(contact_book):
    if not contact_book:
        print("No contacts available.")
    else:
        print("\n--- All Contacts ---")
        for name, details in contact_book.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print("-" * 20)


# Contact book dictionary
contact_book = {}

# Main loop
while True:
    display_menu()
    choice = input("Enter choice (1-6): ").strip()
    if choice == "1":
        add_contact(contact_book)
    elif choice == "2":
        view_contact(contact_book)
    elif choice == "3":
        edit_contact(contact_book)
    elif choice == "4":
        delete_contact(contact_book)
    elif choice == "5":
        list_all_contacts(contact_book)
    elif choice == "6":
        print("Exiting contact book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

