import sys

values = [10, 20,100, 50, 101 ]
naoDivisivel = []

def check(values):
    min = sys.maxsize
    for number in values:
        if number < min:
            min = number
    for number in values:
        if  not number % min == 0:
            naoDivisivel.append(number)
            
    if naoDivisivel:
        return f"O valor minimo é {min} e o numero não divisivel é {naoDivisivel}"
    else:
        return "Todos divisiveis"    
        
print (check(values))
