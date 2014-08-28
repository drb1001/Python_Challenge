
#  http://www.pythonchallenge.com/pc/return/bull.html

# a = [1, 11, 21, 1211, 111221, ...
# len(a[30]) = ?

# look and say sequence

a = ["1", "11"] #, 21, 1211, 111221]

def lookandsay(i):
    stri = str(i)
    if len(stri) == 1:
        return "1" + stri
    else:
        prevl = stri[0]
        count = 1
        output = ""
    for currl in stri[1:]:
        if prevl == currl:
            count += 1
        elif prevl != currl:
            output = output + str(count) + str(prevl)
            prevl = currl
            count = 1
    output = output + str(count) + str(prevl)

    return output


while len(a) < 31:
    anext = lookandsay(a[-1])
    a.append(anext)

print a
print a[30]
print len(a[30])   # 5808

#  http://www.pythonchallenge.com/pc/return/5808.html
