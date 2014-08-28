
#  http://www.pythonchallenge.com/pc/return/5808.html

from PIL import Image

myimage = Image.open('cave.jpg')

mysize = myimage.size

for i in range(0,mysize[0]):
    mypixel = myimage.getpixel((i, midpoint))[1]
    myarray.append(mypixel)
    if i % 7 == 0:
        mystring = mystring + chr(mypixel)


im1 = Image.new("RGB", (640, 480), 'white')
im2 = Image.new("RGB", (640, 480), 'white')




# im1.save('output1.jpg')
# im2.save('output2.jpg')