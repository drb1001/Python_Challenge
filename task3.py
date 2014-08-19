output=''

def iscap(l):
    if l.upper()==l:
        return True
    else:
        return False

uppercount=0
gooduptolower=False
targetletter=''

newfile="task3text.txt"
with open(newfile, "r") as newlist:
    for line in newlist:
        line=line.strip()
        for char in line:
            if iscap(char):
                uppercount=uppercount+1
            else:
                if uppercount==3:
                    if gooduptolower:
                        output=output+targetletter
                        gooduptolower=False
                    else:
                        targetletter=char
                        gooduptolower=True
                else:
                    gooduptolower=False
                    targetletter=''
                uppercount=0

print output

#aAAAaAAAa

