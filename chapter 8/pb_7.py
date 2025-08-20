def rem(lst , word):
    n=[]
    for item in lst:
        if not(item == word):
            n.append(item.strip(word))
    return n

lst = ['apple', 'banana', 'cherry', 'dana']
word = input("Enter a word to remove: ")
print("Updated list:", rem(lst, word))