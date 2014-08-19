#newlist= "newlisttest" #raw_input("enter text: ")
newdict={}

testdict=['\n','!','#','%','$','&',')','(','+','*','@','[', ']','_','^','{','}']

newfile="task2text.txt"
with open(newfile, "r") as newlist:
    for line in newlist:
        for char in line:
            if char not in testdict:
                print char
                if char in newdict:
                    newdict[char]=newdict[char]+1
                else:
                    newdict[char]=1

print newdict
    
