print("Operations using Dictionary")
print("***************************")
print("SCHOOL EVENT BUDGET TRACKER")
print("===========================")

food_team = {"Snacks": 2500, "Drinks": 1200}
decoration_team = {"Balloons": 800, "Banners": 1500}

while True:
    print("\n1. View team budgets")
    print("2. Merge and view all expenses")
    print("3. Add or update an expense")
    print("4. Search for an expense")
    print("5. Remove an expense")
    print("6. Show total budget")
    print("7. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Food team:", food_team)
        print("Decoration team:", decoration_team)

    elif choice == "2":
        all_expenses = food_team.copy()
        all_expenses.update(decoration_team)
        print("All expenses:", all_expenses)

    elif choice == "3":
        team_name = input("Which team? (food/decoration): ").strip().lower()

        if team_name == "food":
            team = food_team
        elif team_name == "decoration":
            team = decoration_team
        else:
            print("Please enter food or decoration.")
            continue

        item = input("Expense name: ").strip().title()

        try:
            amount = int(input("Cost: "))
            team[item] = amount  # Adds a new expense or updates its cost
            print(f"{item} is now recorded as {amount}.")
        except ValueError:
            print("Please enter a whole number for the cost.")

    elif choice == "4":
        item = input("Expense to search for: ").strip().title()
        all_expenses = food_team.copy()
        all_expenses.update(decoration_team)

        if item in all_expenses:
            print(f"{item} costs {all_expenses[item]}.")
        else:
            print(f"{item} was not found.")

    elif choice == "5":
        item = input("Expense to remove: ").strip().title()
        removed = food_team.pop(item, None)

        if removed is None:
            removed = decoration_team.pop(item, None)

        if removed is None:
            print(f"{item} was not found.")
        else:
            print(f"Removed {item}, which cost {removed}.")

    elif choice == "6":
        total = sum(food_team.values()) + sum(decoration_team.values())
        print(f"Total event budget: {total}")

    elif choice == "7":
        print("Good luck with the event!")
        break

    else:
        print("Please choose a number from 1 to 7.")
    