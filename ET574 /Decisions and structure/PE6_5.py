vehicles = ['car', 'Truck', 'boat', 'PLANE']
search_letter = input("Enter a search letter: ")

if len(search_letter) != 1:
    print("Invalid search letter.")
else:
    found = False
    for i, vehicle in enumerate(vehicles):
        if search_letter.lower() in vehicle.lower():
            found = True
            print(f"{vehicle} contains ‘{search_letter}’ and it is in position {i}.")
        else:
            print(f"{vehicle} does not contain ‘{search_letter}’.")
    if not found:
        print(f"No vehicle contains the letter ‘{search_letter}’.")
