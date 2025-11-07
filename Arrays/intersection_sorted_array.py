arr1 = [1,2,3,4,5,7,8,9]
arr2 = [1,2,4,6,8]
res = []

def intersection (arr1, arr2):
    
    pointer_a = 0
    pointer_b = 0

    while pointer_a < len(arr1) and pointer_b < len(arr2):
        if arr1[pointer_a] < arr2[pointer_b]:
            pointer_a += 1
        elif arr2[pointer_b] < arr1[pointer_a]:
            pointer_b += 1
        else:
            res.append(arr1[pointer_a])
            pointer_a += 1
            pointer_b += 1
        
    return res
    
print(intersection(arr1, arr2))