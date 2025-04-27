import bcrypt
from module.json_handler import accounts_json_handler, current_user_json_handler

def login(username, password):
    if current_user_json_handler.data['username'] is not None:
        print("You must logout of your current account first!")
        return

    if not accounts_json_handler.data:
        print("No account found!")
        return

    for account in accounts_json_handler.data:
        if account['username'] == username:
            if bcrypt.checkpw(password.encode('utf-8'), account['password'].encode('utf-8')):
                current_user_json_handler.data['username'] = account['username']
                current_user_json_handler.data['password'] = account['password']
                current_user_json_handler.data['user_data'] = account['user_data']
                current_user_json_handler.dump()
                print(f"Logged in as {username}")
                return

    print("Invalid username or password!")

def authUser(username, password):
    if not accounts_json_handler.data:
        return False

    for account in accounts_json_handler.data:
        if account['username'] == username:
            if bcrypt.checkpw(password.encode('utf-8'), account['password'].encode('utf-8')):   
                return True
                
    return False

def register(username, password):
    if accounts_json_handler.data:
        for account in accounts_json_handler.data:
            if account['username'] == username:
                print("Username already exists!")
                return

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    accounts_json_handler.data.append({
        "username": username, 
        "password": hashed_password,
        "user_data": { # Insert default user data here
            "tracker": {}
        } 
    })
    accounts_json_handler.dump()

    print(f"Registered account '{username}'")
    return

def logout():
    if current_user_json_handler.data['username'] is None:
        print("Already logged out!")
        return

    for account in accounts_json_handler.data:
        if account['username'] == current_user_json_handler.data['username']:
            account['user_data'] = current_user_json_handler.data['user_data']
            accounts_json_handler.dump()
            break
    
    current_user_json_handler.reset()
    print("Logged out")

def delete():
    password = input("Enter you password to proceed: ")
    if not authUser(current_user_json_handler.data["username"], password):
        print("Invalid password!")
        return

    confirm = input("Are you sure you want to delete your account? (y/n): ")
    if confirm.lower() == 'y': 
        # delete account
        for account in accounts_json_handler.data:
            if account['username'] == current_user_json_handler.data['username']:
                accounts_json_handler.data.remove(account)
                break

        accounts_json_handler.dump()
        current_user_json_handler.reset()
        print("Account deleted")