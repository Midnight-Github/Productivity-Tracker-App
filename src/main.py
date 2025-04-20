import command.help
import command.auth

def validateCommand(*args):
    match args[0]:
        case "help":
            if len(args) == 1 or len(args) == 2:
                return True

        case "login":
            if len(args) == 3:
                return True

        case "register":
            if len(args) == 3:
                return True

        case "logout":
            if len(args) == 1:
                return True

        case "delete":
            if len(args) == 1:
                return True

    return False

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
            command.auth.delete()

def main():
    print("Productivity Tracker App(no gui)\n")
    print("'help' to list all commands")

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
