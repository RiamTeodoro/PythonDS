
arr = [3,5,1,2,4,5,2,7,10]


def duplicate(arr):
    tortoise = arr[0]
    hare = arr[0]

    while True:
        tortoise = arr[tortoise]
        hare = arr[arr[hare]]
        if tortoise == hare:
            break

    tortoise = arr[0]

    while tortoise != hare:
        tortoise = arr[tortoise]
        hare = arr[hare]

    return hare
    print(hare)

print(duplicate(arr))

