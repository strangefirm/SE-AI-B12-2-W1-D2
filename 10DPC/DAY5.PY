print("Operations using List")
print("*********************")

cart = ["bread", "milk"]  # Start with items already in the cart

while True:
    print("\nShopping Cart")
    print("1. View cart")
    print("2. Add item")
    print("3. Remove item")
    print("4. Sort cart")
    print("5. Checkout")

    choice = input("Choose an option: ")

    if choice == "1":
        if cart:
            print("Items:", cart)  # Display the list
        else:
            print("Your cart is empty.")

    elif choice == "2":
        item = input("Enter an item to add: ").strip().lower()
        if item:
            cart.append(item)  # Add one item to the end
            print(f"{item} added.")

    elif choice == "3":
        item = input("Enter an item to remove: ").strip().lower()
        if item in cart:  # Check whether the item is in the list
            cart.remove(item)  # Remove the first matching item
            print(f"{item} removed.")
        else:
            print(f"{item} is not in your cart.")

    elif choice == "4":
        cart.sort()  # Arrange items alphabetically
        print("Cart sorted:", cart)

    elif choice == "5":
        #last_item = cart.pop() if cart else None  # Remove the last item
        print("Checking out with:", cart)
        break

    else:
        print("Please choose a valid option.")