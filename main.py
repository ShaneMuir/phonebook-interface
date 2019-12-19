import os
from flask import (Flask, render_template, request,
				   redirect, url_for, flash)
from flask_pymongo import PyMongo
if os.path.exists('env.py'):
	import env

app = Flask(__name__)
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
mongo = PyMongo(app)






@app.route('/')
def index():
	contacts = mongo.db.contacts.find()

	return render_template('base.html', contacts=contacts)








if __name__ == "__main__":
	app.run(debug=True)