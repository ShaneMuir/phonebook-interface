import os
from flask import (Flask, render_template, request,
				   redirect, url_for, flash)
from flask_pymongo import PyMongo
if os.path.exists('env.py'):
	import env

app = Flask(__name__)
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
mongo = PyMongo(app)



@app.route('/', methods=['GET','POST'])
def index():
	if request.method == "POST":
		if request.form.get('q') == "":
			contacts = mongo.db.contacts.find()
			return render_template('index.html', contacts=contacts)
		else:
			query = request.form.get('q')
			contacts = mongo.db.contacts.find({'$text': {'$search' : query}})
			return render_template('index.html', contacts=contacts)

	return render_template('index.html')



if __name__ == "__main__":
	app.run(debug=True)