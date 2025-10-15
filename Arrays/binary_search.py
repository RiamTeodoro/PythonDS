number_to_find = int(input("Type a number: "))
arr = [1,3,5,6,7,8,9,11,13,15,19,32,45,60,100,150,200]

def binary_search(arr, start, end, value):
    while start <= end:
        mid = (start + end )//2
        if value == arr[mid]:
            return mid
        elif value > arr[mid]:
            start = mid + 1 
        else:
            end = mid - 1

    return -1

def search(arr, value):
    if len(arr) == 1:
        if arr[0] == value:
            return "Found"
        else:
            return "Not Found"
        
    low = 0
    high = 1

    while high < len(arr) and arr[high] < value:
        low = high
        high = 2 * high
        
    if high >= len(arr):
        high = len(arr) - 1    

    binary = binary_search(arr, low, high, value)  
    if binary == -1:
        return "Not Found"
    else:
        return "Found at index {}".format(binary)

print(search(arr, number_to_find))  