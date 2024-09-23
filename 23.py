def login():
    while True:
        print("Please Login to continue... ")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == "admin" and password == "password":
            print("Login successful!")
            break
        else:
            print("Login failed. Please try again.")
            continue

login()