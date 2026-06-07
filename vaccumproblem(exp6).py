def vacuum_cleaner(location, roomA, roomB):

    while True:

        if location == 'A':
            if roomA == 'Dirty':
                print("Room A is Dirty.")
                print("Action: SUCK")
                roomA = 'Clean'
            else:
                print("Room A is Clean.")
                print("Action: Move Right")
                location = 'B'

        elif location == 'B':
            if roomB == 'Dirty':
                print("Room B is Dirty.")
                print("Action: SUCK")
                roomB = 'Clean'
            else:
                print("Room B is Clean.")
                print("Action: Move Left")
                location = 'A'

        if roomA == 'Clean' and roomB == 'Clean':
            print("\nBoth rooms are clean.")
            print("Goal State Reached!")
            break

location = input("Enter Vacuum Location (A/B): ")
roomA = input("Enter Room A Status (Clean/Dirty): ")
roomB = input("Enter Room B Status (Clean/Dirty): ")

vacuum_cleaner(location, roomA, roomB)
