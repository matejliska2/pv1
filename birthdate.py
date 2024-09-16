


print("Tell me your date of birth")

while True:
    try:
        month = int(input("Write what month were you born in (number): "))
    except ValueError:
        print("Please write a valid numeric value")
        
        if month >= 1 and month <= 12:
            break
    
while True:
    try:
        year = int(input("Write the year that you were born in: "))
    except ValueError:
        print("Please write a valid numeric value")

        if year >= 1905 and year <= 2024:
            break
        else:
            raise Exception("Write a survivable age")



while True:
    try:
        day = int(input("Write the day that you were born: "))
    except ValueError:
        print("Please write a valid numeric value")

        

        
        