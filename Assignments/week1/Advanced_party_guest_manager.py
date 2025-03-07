def get_guest_info(guests, guest_name):
    """Retrieve information about a specific guest."""
    if guest_name in guests:
        age, email = guests[guest_name]
        return f"{guest_name} (Age: {age}) is coming to the party! Email: {email}"
    return f"{guest_name} is not on the guest list."

def add_guest(guests):
    """Add a new guest with user input, handling existing guests."""
    name = input("Enter guest name: ").capitalize()
    
    if name in guests:
        print(f"{name} is already on the guest list!")
        update = input("Would you like to update their details? (yes/no): ").lower()
        if update != 'yes':
            return
    
    try:
        age = int(input("Enter guest age: "))
        email = input("Enter guest email: ")
        guests[name] = (age, email)
        print(f"{name} has been added/updated successfully!")
    except ValueError:
        print("Invalid age input! Guest not added.")

def display_guests_by_age(guests):
    """Display all guests sorted by age."""
    if not guests:
        print("No guests in the list!")
        return
    
    # Sort guests by age (first element of tuple)
    sorted_guests = sorted(guests.items(), key=lambda x: x[1][0])
    print("\nGuests sorted by age:")
    print("-" * 40)
    for name, (age, email) in sorted_guests:
        print(f"{name}: Age {age}, Email: {email}")

def main():
    # Step 1: Initialize empty guest dictionary
    guests = {}
    
    # Step 2: Add initial guests
    guests["Alice"] = (28, "alice@email.com")
    guests["Bob"] = (35, "bob@email.com")
    guests["Charlie"] = (30, "charlie@email.com")
    
    print("Initial guest list:")
    print(guests)
    
    # Step 3: Update guest list
    guests["David"] = (22, "david@email.com")
    del guests["Bob"]
    
    print("\nUpdated guest list:")
    print(guests)
    
    # Step 4: Test guest info retriever
    print("\nTesting guest information:")
    print(get_guest_info(guests, "Alice"))
    print(get_guest_info(guests, "Bob"))
    
    # Step 5: Display total number of guests
    print(f"\nTotal number of guests: {len(guests)}")
    
    # Extensions
    while True:
        print("\nParty Guest Manager Menu:")
        print("1. Add new guest")
        print("2. Display guests by age")
        print("3. Get guest info")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_guest(guests)
        elif choice == "2":
            display_guests_by_age(guests)
        elif choice == "3":
            name = input("Enter guest name to lookup: ").capitalize()
            print(get_guest_info(guests, name))
        elif choice == "4":
            print("Thank you for using Party Guest Manager!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()