guest_list = []

def add_guest(name):
    if name not in guest_list:
        guest_list.append(name)
        print(f"{name} has been added to the guest list.")
    else:
        print(f"{name} is already on the guest list.")

def remove_guest(name):
    if name in guest_list:
        guest_list.remove(name)
        print(f"{name} has been removed from the guest list.")
    else:
        print(f"{name} is not on the guest list.")

def check_guest(name):
    if name in guest_list:
        print(f"{name} is on the guest list.")
    else:
        print(f"{name} is not on the guest list.")

def display_guests():
    if guest_list:
        print("Guest list:")
        for guest in guest_list:
            print(f"- {guest}")
    else:
        print("The guest list is empty.")
