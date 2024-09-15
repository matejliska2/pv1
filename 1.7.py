

while True:
    try:
        exponent = int(input("Write an exponent (can't be zero nor a negative number): "))
        
        if exponent > 0:
            break
        else:
            print("The exponent must be a positive number. Try again.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")


while True:
    try:
        bo_power= int(input("Write the base of power (can't be zero nor a negative number): "))
        
        if bo_power > 0:
            break
        else:
            print("The base of power must be a positive number. Try again.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")


power = pow(exponent, bo_power)

print(power)

