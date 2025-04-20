import bcrypt
from module.json_handler import accounts_json_handler, current_user_json_handler

def login(username, password):
    if not accounts_json_handler.data:
        print("No account found!")
        return

    for account in accounts_json_handler.data:
        if account['username'] == username:
            if bcrypt.checkpw(password.encode('utf-8'), account['password'].encode('utf-8')):
                current_user_json_handler.data['account'] = account
                current_user_json_handler.dump()
                print(f"Logged in as {username}")
                return

    print("Invalid username or password!")

def register(username, password):
    if accounts_json_handler.data:
        for account in accounts_json_handler.data:
            if account['username'] == username:
                print("Username already exists!")
                return

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    accounts_json_handler.data.append({'username': username, 'password': hashed_password})
    accounts_json_handler.dump()

    print(f"Registered account '{username}'")
    return

def logout():
    current_user_json_handler.reset()
    print("Logged out")

def delete():
    for account in accounts_json_handler.data:
        if account['username'] == current_user_json_handler.data['username']:
            accounts_json_handler.data.remove(account)
            break

    accounts_json_handler.dump()
    current_user_json_handler.reset()
    print("Account deleted")