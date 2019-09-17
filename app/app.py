
import flask
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import os
from SatelliteImageSearch import SatelliteImageSearch

api_key = open('key.txt').readline().strip()
satSearch = SatelliteImageSearch(api_key)

app = Flask(__name__)
app.config['IMAGES_DIR'] = os.path.join('static', 'images')
Bootstrap(app)

@app.route('/search', methods=['GET', 'POST'])
def search():
    search_form = dict(term='mosque', location='Srinagar, Kashmir')
    search_result = {}

    if flask.request.method == 'POST':
        search_term = flask.request.values.get('searchTerm')
        search_loc = flask.request.values.get('searchLoc')

        search_form = dict(term=search_term, location=search_loc)
        search_result = satSearch.search(search_term=search_term, location=search_loc)

    return render_template('search.html', search_form=search_form, place_list=search_result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
