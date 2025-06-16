def help(*args):
    if len(args) == 1:
        listCommands()
        return

    helpCommand(args[1])

def listCommands():
    print("login <username> <password>")
    print("register <username> <password>")
    print("logout")
    print("delete")

    print("tracker add task <location>")
    print("tracker remove task <location>")
    print("tracker update time <location> <value>")
    print("tracker rename task <initial_location> <new_name>")
    print("tracker move task <initial_location> <new_location>") # broken
    print("tracker list task (<location>)") # todo

    print("timer start ") # todo
    print("timer update") # todo

    print("quit")

    print("\nhelp <command> - Show help for a specific command")

def helpCommand(command):
    match command:
        case "login":
            print("Usage: login <username> <password>")
            print("Login to your account registered in the app.")

        case "register":
            print("Usage: register <username> <password>")
            print("Register a new account in the app.")

        case "logout":
            print("Usage: logout")
            print("Logout from your current account.")

        case "delete":
            print("Usage: delete")
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

        case "timer update":
            print("Usage: timer update")
            print("Update the current timer state.")

        case "quit":
            print("Usage: quit")
            print("Exit the app.")

        case "help":
            print("Usage: help (<command>)")
            print("Show help for a specific command.")
            print("command is an optional argument.")

        case _:
            print(f"Unknown command '{command}'. Type 'help' to list all commands.")