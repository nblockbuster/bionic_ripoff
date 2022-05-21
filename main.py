from array import array
import re
import math
import sys

regex_pattern = '([^a-zA-Z0-9_!"#$%&\'()*+,\-.\/:;<=>?@[\]^_`{|}~])'

symbol_regex_pattern = "([_!\"#$%&'()*+,\-.\\\/:;<=>?@[\]^_`{|}~])"

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

def Split(input: str):
    InputString = input
    Words = re.split(regex_pattern, InputString)
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
            i = 0
            firstChar = word[i]
            if re.fullmatch(symbol_regex_pattern, firstChar):
                i+=1
            restOfWord = word[(i+1):]
            BoldWord = f"{BoldChar}{firstChar}{UnboldChar}{restOfWord}"
            BoldWord += PrevWord
            BoldArr.append(BoldWord)
        else:
            boldAmount = int(round_up(len(word)/2))
            firstChar = word[0]
            Unbolded_Char = ""
            if re.fullmatch(symbol_regex_pattern, firstChar):
                Unbolded_Char = word[:1]
                boldedChars = word[1:(boldAmount)]
                restOfWord = word[(boldAmount):]
                print(UnboldChar, boldedChars, restOfWord)
            else:
                boldedChars = word[:boldAmount]
                restOfWord = word[boldAmount:]
            BoldWord = f"{Unbolded_Char}{BoldChar}{boldedChars}{UnboldChar}{restOfWord}"
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