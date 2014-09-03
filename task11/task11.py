
#  http://www.pythonchallenge.com/pc/return/5808.html

from PIL import Image, ImageOps

myimage = Image.open('cave.jpg')

mysize = myimage.size
#  print mysize  # (640, 480)

im1 = Image.new("RGB", (640, 480), 'black')
pix1 = im1.load()
im2 = Image.new("RGB", (640, 480), 'black')
pix2 = im2.load()


for i in range(0, mysize[0]):
    for j in range(0, mysize[1]):
        mypixel = myimage.getpixel((i, j))
        if (i+j) % 2 == 0: pix1[i,j] = mypixel
        else: pix2[i,j] = mypixel


im1 = ImageOps.invert(im1)
im2 = ImageOps.invert(im2)


# for i in range(0, mysize[0]):
#     for j in range(0, mysize[1]):
#         mypixel = myimage.getpixel((i, j))
#         if (i+j) % 2 == 0:
#             if i%2 == 0: pix1[i/2,j] = mypixel
#             else: pix1[(i-1)/2,j] = mypixel
#         else:
#             if i%2 == 0: pix2[i/2,j] = mypixel
#             else: pix2[(i-1)/2,j] = mypixel


im1.save('output1_i.png')
print "output1 saved"
im2.save('output2_i.png')
print "output2 saved"

#  http://www.pythonchallenge.com/pc/return/evil.html
