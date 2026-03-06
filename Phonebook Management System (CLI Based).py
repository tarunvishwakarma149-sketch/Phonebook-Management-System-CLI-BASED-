phonebook = {}

while True:
    print("\n1. Add Contact")
    print("2. Delete Contact")
    print("3. Search Contact")
    print("4. Show All Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter number: ")
        phonebook[name] = number
        print("Contact saved successfully.")

    elif choice == "2":
        name = input("Enter name to delete: ")
        if name in phonebook:
            del phonebook[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter name to search: ")
        if name in phonebook:
            print("Number:", phonebook[name])
        else:
            print("Contact not found.")

    elif choice == "4":
        print("All Contacts:")
        for name, number in phonebook.items():
            print(name, ":", number)

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")
