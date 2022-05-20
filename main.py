from array import array
import re
import math
import sys

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

def Split(input: str):
    InputString = input
    Words = re.split('([^a-zA-Z0-9_!"#$%&\'()*+,\-.\/:;<=>?@[\]^_`{|}~])', InputString)
    return Words

def Bold(word_arr: array, style: str):
    BoldArr = []
    PrevWord = ' '
    BoldChar = "<b>"
    UnboldChar ="</b>"
    if style == "markdown":
        BoldChar = "**"
        UnboldChar ="**"
    for word in word_arr:
        if re.fullmatch('(\s)', word):
            PrevWord = ' '
            continue
        if len(word) <= 3:
            firstChar = word[0]
            restOfWord = word[1:]
            BoldWord = f"{BoldChar}{firstChar}{UnboldChar}{restOfWord}"
            BoldWord += PrevWord
            BoldArr.append(BoldWord)
        else:
            boldAmount = int(round_up(len(word)/2))
            boldedChars = word[:boldAmount]
            restOfWord = word[boldAmount:]
            BoldWord = f"{BoldChar}{boldedChars}{UnboldChar}{restOfWord}"
            BoldWord += PrevWord
            BoldArr.append(BoldWord)
    return BoldArr

def Combine(BoldendArr: array):
    OutputStr = ""
    for BoldWord in BoldendArr:
        OutputStr += BoldWord
    return OutputStr

def main():
    BoldStyle = "html"
    if len(sys.argv) == 1:
        print("No arguments provided.")
        print("You must provide an input string.")
        exit(1)
    if len(sys.argv) > 2:
        BoldStyle = sys.argv[2]
    InputStr = sys.argv[1]
    StrArr = Split(InputStr)
    BoldendArr = Bold(StrArr, BoldStyle)
    OutputStr = Combine(BoldendArr)

    print(OutputStr)
    
main()