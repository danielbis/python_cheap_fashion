#creates an json file of objects of format ["title": example_name, "matches": [{"name": "matched_file", "simillarity": float}]]
import json 
from pprint import pprint
import os, sys
from os import listdir
from os.path import isfile, join
#list of files to be matched
#list of dictionaries matching the provided examples
result = []
examples = []
examples_no_json = []
artists = ["AsapRocky", "ChrisBrown", "JadenSmith", "JerryLorenzo", "JustinBeiber", "KanyeWest", "RusselWestbrook", "TravisScott", "VicMensa"]
for a in artists:
	src = "../profiles/" + a +"/examples/"
	[examples.append(f.replace('.jpg', '.json')) for f in os.listdir(src)]
for e in examples:
	examples_no_json.append(e.strip('.json'))

mypath = "../nearest_neighbors/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for f in onlyfiles:
	if f in examples:
		print(f)
		data = json.load(open("../nearest_neighbors/"+f))
		example = {'title': f.strip('.json'), 'matches': []}
		
		for i in range(1,8):
			if data[i]["filename"] not in examples_no_json:
				match = { "name": data[i]["filename"] + ".jpg", "similarity": data[i]["similarity"] }
				example["matches"].append(match)
		if len(example["matches"]) >= 3:
			result.append(example)
		else:
			print("not enough matches for :", f, " got only: ", len(example["matches"]) )

with open('matches.json', 'w') as outfile:
    json.dump(result, outfile)





