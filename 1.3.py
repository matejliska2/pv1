#3

while True:
    name = input("What is your name: ")
    clarification = input("Is your name really " + name + "? (y/n)")

    if (clarification == "y"):
        print("Thank you, goodbye")
        break
