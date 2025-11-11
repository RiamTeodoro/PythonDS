year = int(input("choise a year: "))

def is_leap(year):

    leap = False

    if year % 4 == 0:
        leap = True

    if year % 400 == 0:
        leap = True

    elif year % 100 == 0:
        leap = False
    
    return leap

print(is_leap(year))

## if leap == False:
##    yes_or_no = "not is bissexto"
##else:
##    yes_or_no = "is bissexto"


##print(f"The year {year} {yes_or_no}")

