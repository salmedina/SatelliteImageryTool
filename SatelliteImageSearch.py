import time
import googlemaps
import requests
import os.path as osp
from easydict import EasyDict as edict

class SatelliteImageSearch():
    def __init__(self, api_key):
        self.gmaps = googlemaps.Client(key=api_key)
        self.api_key = api_key

    def search(self, search_term, location, width=400, height=400, zoom_level=18, format='png'):

        geocode_res = self.gmaps.geocode(location)
        geocode_location = geocode_res[0]['geometry']['location']
        lat = geocode_location['lat']
        lng = geocode_location['lng']
        print(f'Geo-coords for {location}  lat: {lat}   lng:{lng}')

        num_pages = 0
        gmaps_results = []
        res = self.gmaps.places(search_term, location=(lat, lng))
        next_page_token = res['next_page_token'] if 'next_page_token' in res else None
        while res['status'] == 'OK' and num_pages < 1:
            num_pages += 1
            gmaps_results += res['results']
            if 'next_page_token' not in res:
                break
            time.sleep(2)
            res = self.gmaps.places(search_term, location=(lat, lng), page_token=res['next_page_token'])

        places_info_list = []
        for gmaps_res in gmaps_results:
            pinfo = edict(gmaps_res)
            places_info_list.append(dict(lat=pinfo.geometry.location.lat,
                                         lng=pinfo.geometry.location.lng,
                                         name=pinfo.name,
                                         place_id=pinfo.place_id))

        return places_info_list
