arr = [ 1, 3, 2, 2, 5 ]

def rearrange (arr):
    for number in range(1, len(arr)):
        if number % 2 == 0:
            if arr[number] > arr[number-1]:
                arr[number-1], arr[number] = arr[number], arr[number-1]
        else:
            if arr[number] < arr[number-1]:
                arr[number-1], arr[number] = arr[number], arr[number-1]

    print(arr)

    rearrange(arr)            
