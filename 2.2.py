import math

while True:
    try:
        r = int(input("Please write the radius of a circle: "))
        if r > 0:
            break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    except ArithmeticError:
        print("The radius must be a positive number. Try again.")

S = math.pi * pow(r, 2)
print(S)