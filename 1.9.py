pin = 2586

# Cyklus pro 3 pokusy
for i in range(3):
    try:
        inpt = int(input("Password: "))
        if inpt == pin:
            print("Password correct")
            break
        else:
            print("Password incorrect, try again.")
    except ValueError:
        print("Invalid input. Please enter a numeric PIN.")
else:
    print("Too many failed attempts.")