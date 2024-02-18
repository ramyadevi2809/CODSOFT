class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address):
        self.contacts[name] = {"phone_number": phone_number, "email": email, "address": address}
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contacts:")
            for name, contact_info in self.contacts.items():
                print(f"Name: {name}, Phone Number: {contact_info['phone_number']}, Email: {contact_info['email']}, Address: {contact_info['address']}")

    def search_contact(self, search_term):
        search_results = []
        for name, contact_info in self.contacts.items():
            if search_term.lower() in name.lower() or search_term in contact_info['phone_number']:
                search_results.append((name, contact_info))
        return search_results

    def update_contact(self, name, phone_number=None, email=None, address=None):
        if name in self.contacts:
            contact_info = self.contacts[name]
            if phone_number:
                contact_info['phone_number'] = phone_number
            if email:
                contact_info['email'] = email
            if address:
                contact_info['address'] = address
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_manager.add_contact(name, phone_number, email, address)
        elif choice == "2":
            contact_manager.view_contacts()
        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            search_results = contact_manager.search_contact(search_term)
            if search_results:
                print("Search Results:")
                for name, contact_info in search_results:
                    print(f"Name: {name}, Phone Number: {contact_info['phone_number']}, Email: {contact_info['email']}, Address: {contact_info['address']}")
            else:
                print("No contacts found.")
        elif choice == "4":
            name = input("Enter name of contact to update: ")
            phone_number = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")
            contact_manager.update_contact(name, phone_number, email, address)
        elif choice == "5":
            name = input("Enter name of contact to delete: ")
            contact_manager.delete_contact(name)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
