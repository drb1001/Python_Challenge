#  http://www.pythonchallenge.com/pc/def/peak.html


import pickle

output = []

with open("banner.p", "r") as banner:
    unpickle = pickle.load(banner)

print unpickle

data = []
for item in unpickle:
    for seq in item:
        data.append(seq[0] * seq[1])
    data.append('\n')

print "".join(data)


#  http://www.pythonchallenge.com/pc/def/channel.html