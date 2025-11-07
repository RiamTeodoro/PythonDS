import sys

arr = [1,2,3,4,5,6,7,8,2,4,5,7,34,56,23,1234,134,57,67,345,2000]

def largest(arr):

    large = -sys.maxsize
    for i in arr:
        if i > large:
            large = i

    print (large)

largest(arr)        