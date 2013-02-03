import os
import sys

print "making ~/.googler directory."

path = str(os.environ['HOME']) + '/.googler'

if not os.path.exists(path):
    os.makedirs(path)
else:
    print "directory already exists."

print "writing file"

src = open('googler.py')
dst = open(path + '/googler.py', 'w+')

dst.write(src.read())

src.close()
dst.close()

print 'all done, it is suggested that you run alias googler="python ~/.googler/googler.py" for ease of use.'
