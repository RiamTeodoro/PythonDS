target = int(input("Enter a number to find the sum: "))
arr = list(range(1, 51))


def find(arr, target):
    right = 0
    left = len(arr) - 1

    while right < left:
        if arr[right] + arr[left] == target:
            return [right +1, left +1]
        
        elif arr[right] + arr[left] > target:
            left -= 1
        else:
            right += 1

    return []

resultado = find(arr, target)

print(f"The target number is: {target}")
print(f"The end result is: {resultado}")