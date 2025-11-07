word = input("Type a word: ")

def first_recurrence(word):
    checker = 0

    for i in word:
        val = ord(i) - ord('a')
        if (checker & (1 << val) > 0):
            return i
        
        checker = checker | (1 << val)
    
    return -1

print(first_recurrence(word))