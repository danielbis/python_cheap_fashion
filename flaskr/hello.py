from flask import Flask, render_template, request, session, g, redirect, url_for, abort, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Celebrity(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), nullable=False)
	img_path = db.Column(db.String(80), nullable=False)

	def __init__(self, name, img_path):
		self.name = name
		self.img_path = img_path
	def __repr__(self):
		return '<Name %r>' % self.name


class Example(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	artist_name = db.Column(db.String(80), nullable=False)
	img_path = db.Column(db.String(80), nullable=False)
	
	#relationship
	celebrity_id = db.Column(db.Integer, db.ForeignKey('celebrity.id'),
        nullable=False)
	celebrity = db.relationship('Celebrity', backref=db.backref('examples', lazy=True))

	def __init__(self, artist_name, img_path):
		self.artist_name = artist_name
		self.img_path = img_path
	def __repr__(self):
		return '<Name %r>' % self.artist_name
		

class Match(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80), nullable=False)
	img_path = db.Column(db.String(80), nullable=False)
	url = db.Column(db.String(80), nullable=False)
	price = db.Column(db.Integer, nullable=False)
	
	example_id = db.Column(db.Integer, db.ForeignKey('example.id'),
        nullable=False)
	example = db.relationship('Example', backref=db.backref('matches', lazy=True))

	def __init__(self, title, img_path, url, price):
		self.title = title
		self.img_path = img_path
		self.url = url
		self.price = price
	def __repr__(self):
		return '<Title %r>' % self.title




@app.route("/")
def hello():
	artists = Celebrity.query.all()
	paths = [a.img_path.replace(" ","") for a in artists]
	names = [a.name for a in artists]
	print(len(paths))
	return render_template('index.html', paths = paths, names = names)

@app.route("/celebrity/<name>")
def celebrity(name):
	"""user = Celebrity('Brad Pitt', "../static/bp.jpg")
	db.session.add(user)
	db.session.commit()"""
	
	#db.drop_all()
	#allusers = Celebrity.query.all()
	
	#brad = Celebrity.query.filter_by(name = "Brad Pitt").first()
	#print("brad is: ", brad)
	#for u in allusers:
		#print("U: ",u.name, " ", u.img_path)
	print("name is: ", name)
	artist = Celebrity.query.filter(Celebrity.name == name).first()
	examples = artist.examples
	for e in examples:
		temp = e.img_path.replace(" ","")
		e.img_path = temp
		print('example: ', e.img_path)
	return render_template('celebrity_v1.html', examples = examples, name = name)

@app.route("/matches/<id>")
def matches(id):
	print('id: ', id)
	example = Example.query.filter(Example.id == id).first()
	matches = example.matches
	for m in matches:
		print('before: ', m.img_path)
		temp = m.img_path.replace('.jpg', '', 1)
		m.img_path = temp 
		print('after: ', m.img_path)


	print("matches: ", matches)
	return render_template('matches.html', matches = matches)





if __name__ == "__main__":
	db.create_all()
	app.run(debug=True)