number = int(input("Escolha um numero: "))

if number % 2 == 1:
    print("Weird")

elif number % 2 == 0 and number >= 1 and n <= 15:
    print("Not Weird")
    
elif number % 2 == 0 and number <= 20:
    print("Weird")

elif number % 2 == 0 and number >= 21:
    print("Not Weird")
else:
    print("Number not found")


    