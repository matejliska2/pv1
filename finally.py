from math import sqrt
import cmath

x1 = 0
x2 = 0

while True:
    try:
        a = int(input("Write the a value: "))
        b = int(input("Write the b value: "))
        c = int(input("Write the c value: "))

    except ValueError:
        print("Please write numeric values")

        if (a == a and b == b and c == c):
            break
        
        D = pow(b, 2) - 4 * a * c

        if D > 0:
            x1 = (-b + sqrt(D)) / 2 * a
            x2 = (-b - sqrt(D)) / 2 * a
        else:
            raise ValueError ("Discriminant is negative, the result will be complex")
        
        x1 = (-b + cmath.sqrt(D)) / 2 * a
        x2 = (-b - cmath.sqrt(D)) / 2 * a

    except ValueError:
        print("Please write numeric values")
    
    finally:
        print(f"The result of this equation are {x1} and {x2}")