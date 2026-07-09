#OTT Login program

from unittest import case


username = input("Enter your username: ")
password = input("Enter your password: ")
age = int(input("Enter your age: "))
plan = input("Enter your subscription plan (Basic, Standard, Premium): ")

if username == "Avinash" and password == "Avinash@123":
    print("Login successful!")

    if plan.lower() not in ["basic", "standard", "premium"]:
        print("Invalid subscription plan selected. Please choose from Basic, Standard, or Premium.")
        exit()

    if age < 13:
        category = "Kids"
    elif 13 <= age < 18:
        category = "Teens"
    else:
        category = "Adults"

    hd="Yes" if plan.lower() in ["standard", "premium"] else "No"

    match plan.lower():
        case "basic":
            screens = 1
            price = 99
        case "standard":
            screens = 2
            price = 199
        case "premium":
            screens = 4
            price = 299

    print(f"Subscription Plan: {plan.capitalize()}")
    print(f"Number of Screens: {screens}")
    print(f"Price: ${price}")
    print(f"HD Support: {hd}")
    print(f"Category: {category}")
else:
    print("Invalid username or password. Please try again.")
    exit()