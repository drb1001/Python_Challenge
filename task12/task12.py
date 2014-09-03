
#  http://www.pythonchallenge.com/pc/return/evil.html

from PIL import Image, ImageOps

# myimage = Image.open('evil1.jpg')
#
# mysize = myimage.size
#  print mysize  (640, 480)


# im1 = Image.new("RGB", (640, 480), 'black')
# pix1 = im1.load()
#
# for i in range(0, mysize[0]):
#     for j in range(0, mysize[1]):
#         mypixel = myimage.getpixel((i, j))
#         pix1[mysize[0]/2*(i%2) + (i-(i%2))/2, mysize[1]/6*(j%6) + (j-(j%6))/6] = mypixel
#
# im1.save('output2.png')
# print "output2 saved"


# need to replace each of the pixels in the group of 12 = 2 * 6  (see above) with colour shifted pixel
# array of colours same orientaion


myimage = Image.open('output2.png')

myarray = []
for i in range(0,6):
    myarray.append([myimage.getpixel((124, 21 + 80*i )), myimage.getpixel((444, 21 + 80*i))])

print myarray
print myimage.getpixel((124, 21)), myimage.getpixel((444, 21))
print myimage.getpixel((124, 101)), myimage.getpixel((444, 101))
print myimage.getpixel((124, 181)), myimage.getpixel((444, 181))
print myimage.getpixel((124, 261)), myimage.getpixel((444, 261))
print myimage.getpixel((124, 341)), myimage.getpixel((444, 341))
print myimage.getpixel((124, 421)), myimage.getpixel((444, 421))

