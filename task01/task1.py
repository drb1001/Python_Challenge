#  http://www.pythonchallenge.com/pc/def/map.html


from string import maketrans

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq" \
       " glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. " \
       "lmu ynnjw ml rfc spj"


intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
trantab = maketrans(intab, outtab)

print text.translate(trantab)

print "map".translate(trantab)


#  http://www.pythonchallenge.com/pc/def/ocr.html