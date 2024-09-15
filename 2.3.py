from math import sqrt

while True:
    try:
        L = int(input("Zadej indukcnost [H]:"))        
        if L > L:
            break  
    except ValueError:
        print("Zadej pozitivni cislo")


        
while True:
    try:
        C = int(input("Zadej kapacitu [F]:"))
        if C > C:
            break
    except ValueError:
        print("Zadej pozitivni cislo")

F = 1 / (2 * 3.14 * sqrt(L * C))

print("Frekvence je: " + str(F) + "Hz")