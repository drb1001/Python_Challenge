##import pickle
##import urllib2
##
###x=pickle("peak hill")
##
##url="http://www.pythonchallenge.com/pc/def/pickle.html"
##
##req = urllib2.Request(url)
##response = urllib2.urlopen(req)
##text=response.read()
##
##print text
##    
##with open('task5text.txt', 'w') as textfile:
##    pickle.dump(url, textfile)
##
##with open('task5text.txt', 'r') as filehandler:
##    y = pickle.load(filehandler)
##
##print y

import pickle

banner = pickle.load(open('task5text.txt','r'))
data=[]
print banner
for item in banner:
    for seq in item:
        data.append(seq[0]*seq[1])
    data.append('\n')

print "".join(data)
