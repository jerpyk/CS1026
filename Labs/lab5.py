# 1
numbList = []
for i in range(10):
    numb = int(input("Enter a unique number: "))
    while numb in numbList:
        numb = int(input("Not a unique number, try again: "))
    numbList.append(numb)

print(numbList)


# 2
def checkSameFirstLast(stringList):
    count = 0
    for word in stringList:
        if word[0] == word[len(word) - 1] and len(word) > 2:
            count += 1
    return count


print(checkSameFirstLast(['bgh', 'wer', 'yuy', '1661']))


# 3
def zFirst(words):
    zresult = []
    result = []
    for word in words:
        if word.lower()[0] == 'z':
            zresult.append(word)
        else:
            result.append(word)
    zresult.sort()
    result.sort()
    return zresult + result


words = ["hello", "good", "nice", "as", "at", "baseball", "absorb", "sword", "a", "tall", "so", "bored",
         "silver", "hi", "pool", "we", "am", "seven", "do", "you", "want", "ants", "because", "that's",
         "how", "you", "get", "zebra", "zealot", "zoo", "xylophone", "asparagus"]
print(zFirst(words))

# 4
values = [1, 2, 3, 4, 5]
# Cast the newValues into a separate list
newValues = list(values)
# Do not need +1 for the length of values
for i in range(len(values)):
    # Add the 1 to the newValues, not original values
    newValues[i] += 1
    # the first line should print items of values not newValues
    print("Old Value at index {} is : {} ".format(i, values[i]))
    print("New Value at index {} is : {} \n".format(i, newValues[i]))
