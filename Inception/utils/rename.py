import sys
import os
import glob
import re

artists = ["AsapRocky", "ChrisBrown", "JadenSmith", "JerryLorenzo", "JustinBeiber", "KanyeWest", "RusselWestbrook", "TravisScott", "VicMensa"]
for a in artists:
	src = "../profiles/" + a +"/examples/"
	suffix = ".jpg"
	[os.rename(os.path.join(src,f), os.path.join(src, f.strip(".PNG.jpg") + suffix)) for f in os.listdir(src) if f.endswith(".PNG.jpg")]
#[os.rename(os.path.join(src,f), os.path.join(src, f + suffix)) for f in os.listdir(src) if not f.endswith(suffix)]
