from datetime import datetime


def vehicle_command(command):

    time_now = datetime.now().strftime("%H:%M:%S")

    with open("vehicle_log.txt", "a") as log:
        log.write(time_now + " - " + command + "\n")

    if command == "FORWARD":
        print("Vehicle: FORWARD")

    elif command == "LEFT":
        print("Vehicle: LEFT")

    elif command == "RIGHT":
        print("Vehicle: RIGHT")

    elif command == "STOP":
        print("Vehicle: STOP")

    else:
        print("Vehicle: NO COMMAND")