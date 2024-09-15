
while True:
    try:
        x = int(input("Write a number: "))
        y = int(x) + 1
        print(y)
        if x == x:
            break
    except ValueError:
        print("Please write a numeric value")
