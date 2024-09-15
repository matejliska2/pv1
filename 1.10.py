

while True:
    try:
        weight = int(input("Please, enter your weight: "))
        
        if weight > 0:
            break
        else:
            print("The weight must be a positive number. Try again.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")


while True:
    try:
        height= int(input("Please write your height in cm: "))
        
        if height > 0:
            break
        else:
            print("The height must be a positive number. Try again.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")


BMI = weight/pow(height/100, 2)
BMI = round(BMI)

if BMI < 18.5:
    diagnosis = "underweight"
elif BMI >= 18.5 and BMI <= 25:
    diagnosis = "normal weight"
elif BMI > 25 and BMI <= 30:
    diagnosis = "overweight"
elif BMI > 30 and BMI <= 40:
    diagnosis = "obesity"
elif BMI > 40:
    diagnosis = "morbid obesity"




print(f"Your BMI is {BMI} which is {diagnosis}.")

