from flask import Flask, render_template, request, session, g, redirect, url_for, abort, flash

app = Flask(__name__)

	
@app.route("/")
def hello():
	return render_template('index.html')

@app.route("/celebrity/<name>")
def celebrity(name):
	return render_template('celebrity_v1.html', name = name)


app.run(debug=True)