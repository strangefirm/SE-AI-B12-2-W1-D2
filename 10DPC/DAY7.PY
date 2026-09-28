print("EVENT GUEST LIST Example using Set and Frozenset")

guests = {"Ava", "Noah"}
vip_guests = {"Mia", "Ava"}
frozen_guests = frozenset()  # Empty, unchangeable set

while True:
    print("\n1. View guest lists")
    print("2. Add a guest")
    print("3. Remove a guest")
    print("4. Compare guest lists")
    print("5. Save a frozen snapshot")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Guests:", guests)
        print("VIP guests:", vip_guests)
        print("Frozen snapshot:", frozen_guests)

    elif choice == "2":
        name = input("Guest name: ").strip().title()
        guests.add(name)  # Add one guest
        print(name, "added.")

    elif choice == "3":
        name = input("Guest name to remove: ").strip().title()
        guests.discard(name)  # Remove safely, even if the name is absent
        print(name, "removed if they were on the list.")

    elif choice == "4":
        print("All guests:", guests | vip_guests)  # Union
        print("Guests on both lists:", guests & vip_guests)  # Intersection
        print("Guests who are not VIPs:", guests - vip_guests)  # Difference
        print("Guests on only one list:", guests ^ vip_guests)  # Symmetric difference

    elif choice == "5":
        frozen_guests = frozenset(guests)  # Save an unchangeable copy
        print("Snapshot saved:")
        for name in frozen_guests:
            print("-", name)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Choose a number from 1 to 6.")