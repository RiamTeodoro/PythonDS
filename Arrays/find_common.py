arr1 = [2, 5, 8, 10, 15, 20]
arr2 = [1, 6, 10, 15, 18,20]
arr3 = [10, 11, 15, 17,20]

def find_common(arr1, arr2, arr3):


    first, second, third = 0, 0, 0

    while first < len(arr1) and second < len(arr2) and third < len(arr3):
        if arr1[first] == arr2[second] == arr3[third]:
            print(arr1[first])

            first += 1
            second += 1
            third += 1

        elif arr1[first] < arr2[second]:
            first += 1
        
        elif arr2[second] < arr3[third]:
            second += 1

        else:
            third += 1

find_common(arr1,arr2,arr3)
            