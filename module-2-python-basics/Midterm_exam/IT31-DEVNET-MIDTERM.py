"""
Midterm Practical Exam — Pet Adoption Records Manager
Student: [Rivera, Renz Lui B.]
"""

pets = []  # starts empty — the user adds pets as the program runs

def display_menu():
    print ("\n===Pet Adoption Records Manager===")
    print("\n 1. Add a pet\n 2. View all pets\n 3. Count available vs adopted\n 4. Find a pet by name\n 5. Remove a pet by name\n 6. Exit")
    choice = input("Choose an option: ")
    return choice

def add_pet(pets):
    name = input("enter name: ").upper()
    type = input("enter type: ").upper()
    status = input("enter status: ").upper()
    space = " - "
    final = name + space + type + space + status
    pets.append(final)
    print(pets)


def view_pets(pets):
    for i in range(len(pets)):
        print(pets[i])

def count_available_adopted(pets):
    available_count = 0
    adopted_count = 0
    for pet in pets:
        if "AVAILABLE" in pet:
            available_count += 1
        elif "ADOPTED" in pet:
            adopted_count += 1
    print(f"\nAvailable pets: {available_count}")
    print(f"Adopted pets: {adopted_count}")


def find_pet(pets):
    pet_name = input("\nEnter the name of the pet to find: ").upper()
    for pet in pets:
        if pet_name in pet:
            print(f"Pet found: {pet}")
            return
    print("Pet not found.")


# BONUS (optional)
def remove_pet(pets):
    pet_name = input("\nEnter the name of the pet to remove: ").upper()
    for pet in pets:
        if pet_name in pet:
            pets.remove(pet)
            print(f"Pet removed: {pet}")
            return
    print("Pet not found.")

def main():
    running = True
    while running:
        choice = display_menu()
        if choice == "1":
            add_pet(pets)
        elif choice == "2":
            view_pets(pets)
        elif choice == "3":
            count_available_adopted(pets)
        elif choice == "4":
            find_pet(pets)
        elif choice == "5":
            remove_pet(pets)
        elif choice == "6":
            running = False
        else:
            print("Invalid option. Please try again.")  

main()
