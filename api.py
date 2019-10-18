import flask
from flask import jsonify
from weird_shit_scraper import scrape_weird_shit

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/weird_shit', methods=['GET'])
def weird_shit():
    return jsonify(scrape_weird_shit())


app.run()
