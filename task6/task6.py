#  http://www.pythonchallenge.com/pc/def/channel.html

# readme.txt:
# welcome to my zipped list.
# hint1: start from 90052
# hint2: answer is inside the zip

fileno = "90052"

myarray = []

for i in range(0,1000):
    if not str.isdigit(fileno):
        print str(i) + ": " + line + " (" + newfile + ")"
        break
    newfile = "channel/" + fileno + ".txt"
    myarray.append(fileno + ".txt")
    with open(newfile, "r") as read_file:
        for line in read_file:
            splitline = line.split()
            l = len(splitline)
            fileno = splitline[l-1]


# 46145.txt:
# Collect the comments.

comments = ""

import zipfile
z = zipfile.ZipFile("channel.zip", "r")

for name in myarray:
    zz = z.getinfo(name)
    data = z.read(name)
    comments = comments + zz.comment
    
z.close()

print comments


#  http://www.pythonchallenge.com/pc/def/hockey.html