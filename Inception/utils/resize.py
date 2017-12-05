import os, sys
from PIL import Image
from os import listdir
from os.path import isfile, join
basewidth = 135
#size = 194, 194
mypath = "/Users/daniel/Desktop/code/python_proj/Images1"
print("path is: ", mypath)
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print("mypath[0]: ", onlyfiles[0])
for infile in onlyfiles:
    outfile = "/Users/daniel/Desktop/code/python_proj/Images/" + os.path.splitext(infile)[0] + ".jpg"
    print("outfile: ", outfile)
    if infile != outfile:
        try:
            im = Image.open(infile)
            wpercent = (basewidth/float(im.size[0]))
            hsize = int((float(im.size[1])*float(wpercent)))
            im = im.resize((basewidth,hsize), Image.ANTIALIAS)
            print("size[1]: ",im.size[1])

            #im.thumbnail(size, Image.ANTIALIAS)
            im.save(outfile, "JPEG")
        except IOError:
            print ("cannot create thumbnail for '%s'" % infile)
