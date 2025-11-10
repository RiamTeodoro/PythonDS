number = int(input("choice a number: "))

if number % 2 == 1:
    print("Weird")

elif number % 2 == 0 and number >= 1 and number <= 15:
    print("Not Weird")
    
elif number % 2 == 0 and number <= 20:
    print("Weird")

elif number % 2 == 0 and number >= 21:
    print("Not Weird")
else:
    print("Number not found")


