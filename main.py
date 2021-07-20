from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo

# Create a flask app
app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)
## Mongo Configurations - uncomment when you're ready to fill them in
# app.config["MONGO_DBNAME"] = "" # Your database name here
# app.config["MONGO_URI"] = "" # Your URI here (w/ username and password)
# mongo = PyMongo(app)

#### ROUTES 
# Index page
@app.route('/')
@app.route('/index')
def index():
  return render_template("index.html")


## These run configurations are necessary for Flask to run here in Replit
## The host must be 0.0.0.0 and the port must be 8080
if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )
