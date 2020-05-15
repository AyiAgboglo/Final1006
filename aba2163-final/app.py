##################
# Name: Ayi Agboglo
# uni: aba2163
#
# File contains Flask app for personal website (1006 Final)
##################

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route to main page
@app.route("/")
def main_page():
    return render_template("index.html")

#static route to hyperlink about future plans
@app.route("/futureplans")
def hyplink():
    return render_template("future.html")

#static route to hyperlink about fun facts
@app.route("/funfacts")
def hyplink1():
    return render_template("funfacts.html")

#start the server
if __name__ == "__main__":
    app.run()