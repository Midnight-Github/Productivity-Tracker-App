def help(*args):
    if len(args) == 1:
        list_commands()
        return

    match args[1]:
        case "login":
            help_login()

        case "register":
            help_register()

        case "logout":
            help_logout()

        case "delete":
            help_delete()

        case "add":
            pass

        case "quit":
            pass

        case "help":
            pass

        case _:
            print(f"Unknown command '{args[1]}'. Type 'help' to list all commands.")

def list_commands():
    print("login <username> <password>")
    print("register <username> <password>")
    print("logout")
    print("delete")

    print("add <location> <task>")

    print("quit")

    print("help <command> - Show help for a specific command")

def help_login():
    print("Usage: login <username> <password>")
    print("Login to your account registered in the app.")
    
def help_register():
    print("Usage: register <username> <password>")
    print("Register a new account in the app.")

def help_logout():
    print("Usage: logout")
    print("Logout from your current account.")

def help_delete():
    print("Usage: delete")
    print("Delete your current account.")