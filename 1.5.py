#5

print("Tell me your date of birth :)")



while True:
    day = int(input("Please write a valid day of birth: "))
    if (day < 31 or day > 0):
        break


while True:
    month = int(input("Please write a valid month of birth: "))
    if (month >= 0 or month < 12):
        break


year = int(input("Year of birth: "))
while True:        
    year = int(input("Please write a valid year of birth: "))
    if (year > 1924 or year < 2024):
        break

print("Your date of birth is: {day}/{month}/{year}")