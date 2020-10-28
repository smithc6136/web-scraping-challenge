# import necessary libraries
from flask import Flask, render_template
import scrape_mars

# create instance of Flask app
app = Flask(__name__)


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
