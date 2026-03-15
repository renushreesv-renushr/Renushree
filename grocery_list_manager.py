grocery_list = []

while True:
    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Enter item name: ")
        grocery_list.append(item)
        print("Item added successfully")

    elif choice == "2":
        item = input("Enter item to remove: ")
        if item in grocery_list:
            grocery_list.remove(item)
            print("Item removed")
        else:
            print("Item not found")

    elif choice == "3":
        print("Your Grocery List:", grocery_list)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice")