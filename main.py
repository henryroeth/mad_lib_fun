import random
import re

# string literals identifying the files to be chosen from
madLib1 = "Mad_Lib_1.txt"
madLib2 = "Mad_Lib_2.txt"
madLib3 = "Mad_Lib_3.txt"
madLib4 = "Mad_Lib_4.txt"

# list to randomly choose the string literals from
madLibList = []
madLibList.append(madLib1)
madLibList.append(madLib2)
madLibList.append(madLib3)
madLibList.append(madLib4)

# opens a randomly chosen index with the string literal identifying the file
randomIndex = random.randrange(0,4)
file = open(madLibList[randomIndex])

# list containing lines of the file
lines = file.readlines()

# prompts the user for inputs and substitutes them into the mad lib
def completeMadLib(a):
    inputs = []
    newa = []
    d = ")"
    for i in a:
        parentheticals = re.findall(r'\(.*?\)', i)
        for x in parentheticals:
            response = input(x.replace('(','').replace(')',': '))
            inputs.append(response)
    joined = ' '.join(a)
    for j in range(0,len(inputs)):
        joined = re.sub("\(.*?\)",inputs[j],joined,1)
    print("File: \"Mad_Lib_" + str(randomIndex + 1) + ".txt\"")
    print(joined)

if __name__ == "__main__":
    completeMadLib(lines)