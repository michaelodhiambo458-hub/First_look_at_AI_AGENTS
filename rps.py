letters = ('A','B','C')
#unpacking a tuple
items=(0,'A')
index, letter = items
for index,letters in enumerate( letters):
    print(index,letters)
    #enumerate creates a tuple ,enumerate returns a value with its index