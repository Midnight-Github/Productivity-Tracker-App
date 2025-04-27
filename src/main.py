import command.help
import command.auth
import command.tracker
from module.json_handler import current_user_json_handler

COMMAND_CONSTRAINTS = {
    "help": {"command_len": [1, 2]},
    "login": {"command_len": [3]},
    "register": {"command_len": [3]},
    "logout": {"command_len": [1]},
    "delete": {"command_len": [1]},
    "tracker add task": {"command_len": [4]},
    "tracker remove task": {"command_len": [4]},
    "tracker reset task time": {"command_len": [5]},
    "tracker rename task": {"command_len": [5]},
}

def validateCommand(*args, command_line):
    for command_constraint in COMMAND_CONSTRAINTS:
        if command_constraint in command_line:
            command_key = command_constraint
            break
    else:
        return False

    if len(args) in COMMAND_CONSTRAINTS[command_key]["command_len"]:
        return command_key

def exeCommand(*args, command_line):
    command_key = validateCommand(*args, command_line=command_line)

    if command_key is False:
        print("Invalid command! Type 'help' to list commands.")
        return

    match command_key:
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

        case "tracker add task":
            command.tracker.addTask(args[3])

        case "tracker remove task":
            command.tracker.removeTask(args[3])

        case "tracker reset task time":
            command.tracker.resetTaskTime(args[4])

        case "tracker rename task":
            command.tracker.renameTask(*args[3:])

        case _:
            raise Exception("Unknown Error! command unmatched")

def main():
    print("Productivity Tracker App(no gui)\n")
    print("'help' to list all commands")

    if current_user_json_handler.data['username'] is not None:
        print(f"Logged in as {current_user_json_handler.data['username']}\n")

    while True:
        command_line = input("command: ")
        if command_line.strip() == '':
            continue
        if command_line == "quit":
            break

        print()
        exeCommand(*command_line.split(), command_line=command_line)
        print()

if __name__ == "__main__":
    main()
