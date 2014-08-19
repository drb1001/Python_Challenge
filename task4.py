import urllib2

url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=82682"

for i in range(0,400):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    text=response.read()
    
    print text

    text=text.split()
    newtext=text[len(text)-1]

    if newtext=="6711":
        break

    url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+newtext

print text

# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345

#http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=16044
#Yes. Divide by two and keep going.
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022

#http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=82682
#There maybe misleading numbers in the 
#text. One example is 82683. Look only for the next nothing and the next nothing is 63579
#http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=63579
