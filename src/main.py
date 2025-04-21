import command.help
import command.auth
import command.tracker
from module.json_handler import current_user_json_handler

COMMAND_CONSTRAINTS = {
    "help": {"arg_count": [0, 1]},
    "login": {"arg_count": [2]},
    "register": {"arg_count": [2]},
    "logout": {"arg_count": [0]},
    "delete": {"arg_count": [0]},
    "tracker_add_task": {"arg_count": [1]},
    "tracker_remove_task": {"arg_count": [1]},
    "tracker_reset_task_time": {"arg_count": [1]},
    "tracker_rename_task": {"arg_count": [2]},
}

def validateCommand(*args):
    command = args[0]
    if command not in COMMAND_CONSTRAINTS:
        return False

    return len(args) - 1 in COMMAND_CONSTRAINTS[command]["arg_count"]

def exeCommand(*args):
    if not validateCommand(*args):
        print("Invalid command! Type 'help' to list commands.")
        return

    match args[0]:
        case "help":
            command.help.help(*args)

        case "login":
            command.auth.login(*args[1:])

        case "register":
            command.auth.register(*args[1:])

        case "logout":
            command.auth.logout()

        case "delete":
            password = input("Enter you password to proceed: ")
            if not command.auth.authUser(current_user_json_handler.data["username"], password):
                print("Invalid password!")
                return

            confirm = input("Are you sure you want to delete your account? (y/n): ")
            if confirm.lower() == 'y':
                command.auth.delete()

        case "tracker_add_task":
            command.tracker.addTask(*args[1:])

        case "tracker_remove_task":
            command.tracker.removeTask(*args[1:])

        case "tracker_reset_task_time":
            command.tracker.resetTaskTime(*args[1:])

        case "tracker_rename_task":
            command.tracker.renameTask(*args[1:])

        case _:
            raise Exception("Unknown Error! command unmatched")

def main():
    print("Productivity Tracker App(no gui)\n")
    print("'help' to list all commands")

    if current_user_json_handler.data['username'] is not None:
        print(f"Logged in as {current_user_json_handler.data['username']}\n")

    while True:
        command = input("command: ")
        if command.strip() == '':
            continue
        if command == "quit":
            break

        print()
        exeCommand(*command.split())
        print()

if __name__ == "__main__":
    main()
