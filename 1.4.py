#4

rainy = False
windy = False
foggy = False

if rainy and windy and foggy:
    print("Today is a great day.")
elif not rainy or not foggy and windy:
    print("You should take an umrella wth you.")
elif not windy and rainy:
    print("You should take a hat with you.")
elif not foggy:
    print("You should take a reflective vest.")