import sys

values = [10, 20,100, 50, 101 ]
not_divisible = []

def check(values):
    min = sys.maxsize
    for number in values:
        if number < min:
            min = number
    for number in values:
        if  not number % min == 0:
            not_divisible.append(number)
            
    if not_divisible:
        return f"O valor minimo é {min} e o numero não divisivel é {not_divisible}"
    else:
        return "Todos divisiveis"    
        
print (check(values))
