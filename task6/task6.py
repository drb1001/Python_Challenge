#welcome to my zipped list.
#hint1: start from 90052
#hint2: answer is inside the zip

filepath="task6zip/"
fileno="90052"
fileext=".txt"

for i in range(0,1000):
    newfile=filepath+fileno+fileext
    with open(newfile, "r") as read_file:
        for line in read_file:
            print str(i)+": "+line
            splitline=line.split()
            l=len(splitline)
            fileno=splitline[l-1]

print text
