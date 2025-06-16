def help(command_line):
    if len(command_line.split()) == 1:
        listCommands()
        return

    helpCommand(command_line)

def listCommands():
    print("account login <username> <password>")
    print("account register <username> <password>")
    print("account logout")
    print("account delete")

    print("tracker add task <location>")
    print("tracker remove task <location>")
    print("tracker update time <location> <value>")
    print("tracker rename task <initial_location> <new_name>")
    print("tracker move task <initial_location> <new_location>")
    print("tracker list task (<location>)") # todo

    print("tracker start task <location>")
    print("tracker stop task <location>")

    print("quit")

    print("\nhelp <command> - Show help for a specific command")

def helpCommand(command):
    match command.split(maxsplit=1)[1]:
        case "account login":
            print("Usage: account login <username> <password>")
            print("Login to your account registered in the app.")

        case "account register":
            print("Usage: account register <username> <password>")
            print("Register a new account in the app.")

        case "account logout":
            print("Usage: account logout")
            print("Logout from your current account.")

        case "account delete":
            print("Usage: account delete")
            print("Delete your current account.")

        case "tracker add task":
            print("Usage: tracker add task <location>")
            print("Add a new task to the specified location.")

        case "tracker remove task":
            print("Usage: tracker remove task <location>")
            print("Remove a task from the specified location.")

        case "tracker update time":
            print("Usage: tracker update time <location> <time>")
            print("time: HH:MM:SS")
            print("Updates the time spent on a task in the specified location to the give value.")

        case "tracker rename task":
            print("Usage: tracker rename task <initial_location> <new_name>")
            print("Rename a task from the initial location with new name.")

        case "tracker move task":
            print("Usage: tracker move task <initial_location> <new_location>")
            print("Move a task from the initial location to the new location.")

        case "tracker list task":
            print("Usage: tracker list task (<location>)")
            print("List all tasks in the specified location.")
            print("location is an optional argument.")

        case "tracker start task":
            print("Usage: tracker start task <location>")
            print("Start a task at the specified location.")

        case "tracker stop task":
            print("Usage: tracker stop task <location>")
            print("Stop a task at the specified location.")

        case "quit":
            print("Usage: quit")
            print("Exit the app.")

        case "help":
            print("Usage: help (<command>)")
            print("Show help for a specific command.")
            print("command is an optional argument.")

        case _:
            print(f"Unknown command '{command}'. Type 'help' to list all commands.")