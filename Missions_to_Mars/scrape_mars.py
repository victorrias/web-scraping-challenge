from flask import Flask, render_template, redirect
import requests
import pymongo
# from pymongo import MongoClient
import scrape
from flask_pymongo import PyMongo

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", mars_data=mars_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():


    # Run the scrape function
    scrape_mars_data = scrape.scrape_info()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update_one({}, {"$set": scrape_mars_data}, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
