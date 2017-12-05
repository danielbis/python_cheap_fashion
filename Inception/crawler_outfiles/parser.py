import json 
from pprint import pprint

data = json.load(open('mergedv2.json'))
matches_data = json.load(open('matches.json'))
results = []
counter = 0
for m in matches_data:
	temp_object = {'title': m["title"], 'matches': []}

	for match in m["matches"]:
		temp_img = match["name"]
		for d in data:
			counter +=1
			print(counter)
			if "path" in d["files"][0].keys():
				if d["files"][0]["path"].strip('full/') == temp_img.strip(".jpg") or d["files"][0]["path"].strip('full/') == temp_img:
					print("Match!")
					product = {
						"price": d["price"], 
						"title": d["title"], 
						"url": d["item_url"], 
						"img": temp_img, 
						"name": temp_img, 
						"similarity": match["similarity"]

					}					
					"""product = match
					product["price"] = d["price"]
					product["title"] = d["title"]
					product["url"] = d["item_url"]
					product["img"] = temp_img"""
					temp_object['matches'].append(product)

	if len(temp_object['matches']) >= 2:
		results.append(temp_object)
	else: 
		print("less then 3 matches for: ", m["title"], " only: ", len(temp_object['matches']))

with open('final_data.json', 'w') as outfile:
    json.dump(results, outfile)






#for d in data:
	#pprint(d["price"])

#pprint(data)