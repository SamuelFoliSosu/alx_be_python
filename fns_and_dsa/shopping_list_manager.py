"""
1. Shopping List Manager
mandatory
Objective: Utilize Python lists to create a simple shopping list manager that allows users to add items, view the current list, and remove items.

Task Description:
Create a Python script named shopping_list_manager.py that implements a simple interface for managing a shopping list. This task focuses on using lists to store and manipulate data dynamically.

Requirements:
Core Functionality:

Your script should start with an empty list named shopping_list.
Implement functionality to add items to the list, remove items, and display the current list.
User Interface:

Use a loop to continuously display a menu with options to the user until they choose to exit. The menu should offer options to add an item, remove an item, view the list, and exit.
For adding items, prompt the user for the item name and append it to shopping_list.
For removing items, ask the user for the item name and remove it from shopping_list. If the item is not found, display a message indicating so.
To view the list, print each item in shopping_list to the console.
Ensure your script handles invalid menu choices gracefully.
shopping_list_manager.py Skeleton:
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            pass
        elif choice == '2':
            # Prompt for and remove an item
            pass
        elif choice == '3':
            # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
Note for Students:

You are responsible for completing the main() function with the appropriate logic to handle adding, removing, and displaying items in the shopping_list.
This task introduces you to working with lists in a practical scenario, enhancing your understanding of how dynamic data structures can be manipulated and utilized in Python programs.

"""

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            pass
        elif choice == '2':
            # Prompt for and remove an item
            pass
        elif choice == '3':
            # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()