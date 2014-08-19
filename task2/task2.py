# http://www.pythonchallenge.com/pc/def/ocr.html

testdict = {}

newfile = "task2text.txt"
with open(newfile, "r") as newlist:
    for line in newlist:
        for char in line:
            if char in testdict:
                testdict[char] = testdict[char] + 1
            else:
                testdict[char] = 1

print testdict


output = ""

with open(newfile, "r") as newlist:
    for line in newlist:
        for char in line:
            if str.isalpha(char):
                output = output + char

print output


# http://www.pythonchallenge.com/pc/def/equality.html