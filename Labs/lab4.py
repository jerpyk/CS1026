# A : False
# B : 21
# C : True
# D : -1
# E : False
# F : 0

def main():
    print(factorial(5))
    helloWorldNTimes(2)
    helloWorldNTimes(1)
    helloWorldNTimes(3)
    helloWorldNTimes(2)
    print(countVowels("AEIOu"))


def factorial(n):
    result = n
    for i in range(n-1, 0, -1):
        result = result*i
    return result


def helloWorld():
    print("Hello World")


def helloWorldNTimes(n):
    for i in range(n):
        helloWorld()


def countVowels(word):
    # number of vowels should start at 0
    numVowels = 0
    # use variable word, not string
    # check for vowels by checking the lower case vowels in the word
    for letter in word:
        if letter.lower() in "aeiou":
            numVowels += 1
    # return the number of vowel counts, not the letter
    return numVowels


main()
