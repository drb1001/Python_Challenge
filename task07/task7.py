#  http://www.pythonchallenge.com/pc/def/oxygen.html


from PIL import Image

myimage = Image.open('oxygen.png')
mysize = myimage.size
midpoint = (mysize[1] - 1)/2

print mysize, midpoint

myarray = []
mystring = ""
for i in range(0,mysize[0]):
    mypixel = myimage.getpixel((i, midpoint))[1]
    myarray.append(mypixel)
    if i % 7 == 0:
        mystring = mystring + chr(mypixel)

print myarray
print mystring

#  smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]n\S

mystring2 = ""
for i in [105, 110, 116, 101, 103, 114, 105, 116, 121]:
    mystring2 = mystring2 + chr(i)
print mystring2


#  http://www.pythonchallenge.com/pc/def/integrity.html
