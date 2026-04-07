# ===============================================
# RESERVATION SYSTEM - HOTEL SANTO AMARO
# Made by: Leonardo Lima
# ===============================================

# Fixed daily rate
daily_rate = 120

# List that stores all reservations
reservations = []

# Total number of available rooms in the hotel
available_rooms = 5


# -------- FUNCTION TO MAKE A RESERVATION --------
def make_reservation(available_rooms, reservations):
    # Check if there are no rooms available
    if available_rooms == 0:
        print("No rooms available.")
        return available_rooms, reservations

    # Ask guest information
    name = input("Enter the guest name: ")
    days = int(input("How many days will the guest stay? "))

    # Calculate total price
    total_value = days * daily_rate

    # Create reservation and add to the list
    reservation = {"name": name, "days": days, "value": total_value}
    reservations.append(reservation)

    # Decrease available rooms
    available_rooms -= 1

    print(f"\nReservation successfully made for {name}!")
    print(f"Total price: R${total_value:.2f}")
    print(f"Remaining rooms: {available_rooms}")

    return available_rooms, reservations


# -------- FUNCTION TO LIST GUESTS --------
def list_guests(reservations):
    if len(reservations) == 0:
        print("No guests registered yet.")
    else:
        print("\nGuest list:")
        for i, reservation in enumerate(reservations, start=1):
            print(f"{i}. Name: {reservation['name']} | Days: {reservation['days']} | Value: R${reservation['value']:.2f}")


# -------- FUNCTION TO SHOW TOTAL REVENUE --------
def show_report(reservations):
    total = 0

    for reservation in reservations:
        total += reservation["value"]

    print(f"\nTotal revenue so far: R${total:.2f}")


# -------- MAIN MENU --------
def menu():
    available_rooms = 5
    reservations = []

    while True:
        print("\n========= MAIN MENU =========")
        print("1 - Make reservation")
        print("2 - List guests")
        print("3 - Show financial report")
        print("4 - Exit system")

        option = input("Choose an option: ")

        if option == "1":
            available_rooms, reservations = make_reservation(available_rooms, reservations)
        elif option == "2":
            list_guests(reservations)
        elif option == "3":
            show_report(reservations)
        elif option == "4":
            print("\nExiting system... Thank you for using Hotel Santo Amaro!")
            break
        else:
            print("Invalid option! Try again.")


# -------- PROGRAM START --------
menu()
