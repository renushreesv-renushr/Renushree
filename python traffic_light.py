cars = int(input("Enter number of cars waiting: "))
time_of_day = input("Enter time of day (day/night): ")

if time_of_day.lower() == "night":
    print("Signal Mode: Blinking Yellow")

elif cars > 20:
    print("Green Light Duration: LONG")

elif cars < 5:
    print("Green Light Duration: SHORT")

else:
    print("Green Light Duration: NORMAL")