arr = [0, 0, 1, 1, 2, 2, 6, 6, 9, 10, 10]

def find_odd_number(nums):

    number = 0
    for n in nums:
        number ^= n
    
    return number

print(find_odd_number(arr))

