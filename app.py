# import necessary libraries
from flask import Flask, render_template
import scrape_mars
# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

# create instance of Flask app
app = Flask(__name__)

# Code from 12.3 Activity 7 for Mongo part(??)
# # Create connection variable
# conn = 'mongodb://localhost:27017'

# # Pass connection to the pymongo instance.
# client = pymongo.MongoClient(conn)

# # Connect to a database. Will create one if not already available.
# db = client.team_db

# # Drops collection if available to remove duplicates
# db.team.drop()

# # Creates a collection in the database and inserts two documents
# db.team.insert_many(
#     [
#         {
#             'player': 'Jessica',
#             'position': 'Point Guard'
#         },
#         {
#             'player': 'Mark',
#             'position': 'Center'
#         }
#     ]
# )



# create route that renders index.html template
@app.route("/")
def echo():
    #return render_template("scrape_mars.py")
    return 'Hello World'
    # hello
@app.route("/scrape")
def scrape():
    mars = scrape_mars.scrape()
    return render_template('index.html', mars=mars)

if __name__ == "__main__":
    app.run(debug=True)
