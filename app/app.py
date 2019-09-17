
import flask
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import os
from SatelliteImageryTool.SatelliteImageSearch import SatelliteImageSearch

api_key = open('key.txt').readline().strip()
satSearch = SatelliteImageSearch(api_key)

app = Flask(__name__)
app.config['IMAGES_DIR'] = os.path.join('static', 'images')
Bootstrap(app)

@app.route('/search', methods=['GET', 'POST'])
def search():
    search_form = dict(term='mosque', lat=34.083672, lng=74.797279)
    search_result = {}

    if flask.request.method == 'POST':
        search_term = flask.request.values.get('searchTerm')
        search_lat = flask.request.values.get('searchLat')
        search_lng = flask.request.values.get('searchLng')

        search_form = dict(term=search_term, lat=search_lat, lng=search_lng)
        search_result = satSearch.search(search_term, search_lat, search_lng)


    return render_template('search.html', search_form=search_form, place_list=search_result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
