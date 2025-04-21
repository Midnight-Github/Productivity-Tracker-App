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

    print("tracker_add_task <location>")
    print("tracker_remove_task <location>")
    print("tracker_reset_time <location>")
    print("tracker_rename_task <initial_location> <new_location>")
    print("tracker_list_task (<location>)") # todo

    print("timer_update") #todo

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

        case "tracker_add_task":
            print("Usage: tracker_add_task <location>")
            print("Add a new task to the specified location.")

        case "tracker_remove_task":
            print("Usage: tracker_remove_task <location>")
            print("Remove a task from the specified location.")

        case "tracker_reset_time":
            print("Usage: tracker_reset_time <location>")
            print("Reset the time spent on a task in the specified location.")

        case "tracker_rename_task":
            print("Usage: tracker_rename_task <initial_location> <new_location>")
            print("Rename a task from the initial location to the new location.")

        case "tracker_list_task":
            print("Usage: tracker_list_task (<location>)")
            print("List all tasks in the specified location.")
            print("location is an optional argument.")

        case "timer_update":
            print("Usage: timer_update")
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