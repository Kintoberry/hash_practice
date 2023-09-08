import os

if not os.path.exists("user_db"):
    os.mkdir("user_db")

current_user = None
user_db_path = os.path.join("user_db", "users.txt")

def register(username, password):
    with open(user_db_path, "a") as f:
        f.write(f"{username}, {password}\n")

def is_registered(username):
    with open(user_db_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            saved_username, _ = line.strip().split(", ")
            if saved_username == username:
                return True
    return False

def login(username, password):
    global current_user
    if current_user is not None:
        print("You are already logged in.")
    elif is_registered(username):
        with open(user_db_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                saved_username, saved_password = line.strip().split(", ")
                if saved_username == username and saved_password == password:
                    current_user = username
                    print("Login successful.")
                    return
        print("Incorrect username or password.")
    else:
        print("User not registered. Please register first.")

def logout():
    global current_user
    if current_user is not None:
        current_user = None
        print("Logout successful.")
    else:
        print("You are not logged in.")

while True:
    command = input("Enter a command (register, login, logout, or finish): ").strip().split()
    
    if not command:
        continue

    action = command[0].lower()

    if action == "register":
        if current_user is not None:
            print("You can't register while logged in. Logout first.")
        elif len(command) == 3:
            username, password = command[1], command[2]
            if is_registered(username):
                print("Username already exists. Please choose another one.")
            else:
                register(username, password)
                print("Registration successful.")
        else:
            print("Invalid command format. Use 'register username password'.")

    elif action == "login":
        if current_user is not None:
            print("You are already logged in.")
        elif len(command) == 3:
            username, password = command[1], command[2]
            login(username, password)
        else:
            print("Invalid command format. Use 'login username password'.")

    elif action == "logout":
        logout()

    elif action == "finish":
        break

    else:
        print("Invalid command. Please use 'register', 'login', 'logout', or 'finish'.")
