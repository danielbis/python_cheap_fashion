import shutil
import os
import sys

#pass in arguments 1 = src 2nd = dst1 (images) dst2 = testing
#get dst
src = str(sys.argv[1])
dst1 = str(sys.argv[2])
dst2 = str(sys.argv[3])

names = os.listdir(src)
errors = []
number_of_elements = len(names)
to_images = int(number_of_elements * 0.75) 
print("Coping items...")

"""for i in range(0, to_images):
	srcname = os.path.join(src, names[i])
	dstname = os.path.join(dst1, names[i])
	try:
		shutil.copy2(srcname, dstname)
	except(IOError, os.error) as why:
		errors.append((srcname, dstname, str(why)))"""


for i in range(to_images, number_of_elements):
	srcname = os.path.join(src, names[i])
	dstname = os.path.join(dst2, names[i])
	try:
		shutil.copy2(srcname, dstname)
	except(IOError, os.error) as why:
		errors.append((srcname, dstname, str(why)))

if (len(errors) == 0):
	print("Successfully copied all of the items.")
else:
	print("Errors encountered, log below: ")
	print(errors)

