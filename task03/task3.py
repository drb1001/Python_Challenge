# http://www.pythonchallenge.com/pc/def/equality.html

#looking for this pattern:  aAAAaAAAa

output = ""

uppercount = 0
gooduptolower = False
targetletter = ""

newfile = "task3text.txt"
with open(newfile, "r") as newlist:
    for line in newlist:
        line = line.strip()
        for char in line:
            if str.isupper(char):
                uppercount = uppercount + 1
            else:
                if uppercount == 3:
                    if gooduptolower:
                        output = output + targetletter
                        gooduptolower = False
                    else:
                        targetletter = char
                        gooduptolower = True
                else:
                    gooduptolower = False
                    targetletter = ''
                uppercount = 0

print output


# http://www.pythonchallenge.com/pc/def/linkedlist.html
