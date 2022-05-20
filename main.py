from array import array
import re
import math

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

def Split(input: str):
    InputString = input
    Words = re.split('(\W)', InputString)
    print(Words)
    return Words

def Bold(word_arr: array):
    BoldArr = []
    PrevWordIsSpace = ' '
    for word in word_arr:
        print("Current Word:", word)
        if re.fullmatch('(\W)', word):
            PrevWordIsSpace = ' '
            print("Word in arr not a word, skipping")
            continue
        if len(word) <= 3:
            print("Current Word is <= 3 Characters.")
            firstChar = word[0]
            restOfWord = word[1:]
            print(firstChar + "+" + restOfWord)
            BoldWord = f"<b>{firstChar}</b>{restOfWord}"
            if PrevWordIsSpace is ' ':
                BoldWord += ' '
            print(BoldWord)
            BoldArr.append(BoldWord)
        else:
            print("Current Word is >= 4 Characters")
            boldAmount = int(round_up(len(word)/2))
            print("Amount of characters to be bolded: ", boldAmount)
            boldedChars = word[:boldAmount]
            restOfWord = word[boldAmount:]
            print(boldedChars + "+" + restOfWord)
            BoldWord = f"<b>{boldedChars}</b>{restOfWord}"
            if PrevWordIsSpace is ' ':
                BoldWord += ' '
            print(BoldWord)
            BoldArr.append(BoldWord)
    return BoldArr
def Combine():
    return    
InputStr = "Bionic Reading is a new"
StrArr = Split(InputStr)
BoldendArr = Bold(StrArr)

print(BoldendArr)

OutputStr = ""
for BoldWord in BoldendArr:
    OutputStr += BoldWord
    
print(OutputStr)