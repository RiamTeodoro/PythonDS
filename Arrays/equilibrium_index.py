arr = [-7, 1, 5, 2, -4, 3, 0]

def find_equi(arr):
    total_sum = sum(arr)

    left_sum = 0

    for number, num in enumerate(arr):
        total_sum -= num

        if left_sum == total_sum:
            return number 
        
        left_sum += num 

    return -1

print(find_equi(arr))

