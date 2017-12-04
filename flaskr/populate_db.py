import json 
from pprint import pprint
from hello import db, Celebrity, Example, Match
print("name is: ", __name__)
data = json.load(open('final2.json'))

artists = [{"name": "Future", "examples": ["future1", "future2", "future3", "future4"]} ,{"name": "Gucci Mane", "examples": ["gucci1", "gucci2", "gucci3"]} , 
{"name": "Kanye West", "examples": ["kanye1", "kanye2", "kanye3", "kanye4"]}, {"name": "Kendrick Lamar", "examples": ["kendrick1", "kendrick2", "kendrick3","kendrick4"]}, {"name": "Travis Scott", "examples": ["travis1", "travis2", "travis3", "travis4"]}, {"name": "Wiz Khalifa", "examples":["wiz1", "wiz2", "wiz3", "wiz4"]}, {"name": "Chance the Rapper", "examples": ["chance1", "chance2", "chance3", "chance4"]}, {"name": "Kim Cudi", "examples": ["cudi1", "cudi2", "cudi3"]}]
i = 0
for artist in artists:
	celeb = Celebrity(artist["name"], './static/profiles/' + artist["name"] + "/" + artist["name"] + ".jpg")
	print(celeb)
	for e in artist["examples"]:
		example = Example(artist["name"], './static/profiles/' + artist["name"] + "/examples/" + e + ".jpg")
		print("e: ", e)
		for d in data:
			if d["title"] == e:
				for m in d["matches"]:
					i += 1
					print("Match!")
					img_path = "./static/data/" + m["img"] + ".jpg"
					match = Match(m["title"], img_path, m["url"], m["price"])
					print("match is: ", match)
					example.matches.append(match)

		celeb.examples.append(example)
	db.session.add(celeb)
	db.session.commit()

print("i: ", i)
if __name__ == "__main__":
	db.create_all()