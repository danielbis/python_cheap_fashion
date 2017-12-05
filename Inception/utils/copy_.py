import shutil
import os
import sys

#pass in arguments 1 = src 2nd = dst1 (images) dst2 = testing
#get dst
artists = ["AsapRocky", "ChrisBrown", "JadenSmith", "JerryLorenzo", "JustinBeiber", "KanyeWest", "RusselWestbrook", "TravisScott", "VicMensa"]
dst = "../copies/"

for a in artists:
	src = "../profiles/" + a +"/examples/"
	names = os.listdir(src)
	errors = []
	number_of_elements = len(names)

	print("Coping items...")

	for i in range(0, number_of_elements):
		srcname = os.path.join(src, names[i])
		dstname = os.path.join(dst, names[i])
		try:
			shutil.copy2(srcname, dstname)
		except(IOError, os.error) as why:
			errors.append((srcname, dstname, str(why)))

if (len(errors) == 0):
	print("Successfully copied all of the items.")
else:
	print("Errors encountered, log below: ")
	print(errors)

