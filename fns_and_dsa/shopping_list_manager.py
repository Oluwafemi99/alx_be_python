# shopping list manager
shopping_list = []


def add_item(item):
    shopping_list.append(item)
    print(f"You have added {item}")


def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"You have removed {item}")
    else:
        print(f"{item} not found in the shopping list")


def view_list():
    print("Shopping List:")
    for item in shopping_list:
        print(f"- {item}")


def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ")
            add_item(item)
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the item to remove: ")
            remove_item(item)
        elif choice == '3':
            # Display the shopping list
            view_list()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
