# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
### - call exposes all registered services (none by default)
#########################################################################



from gluon.serializers import loads_json
     
def index():
	response.files.append('http://cdn.leafletjs.com/leaflet-0.7/leaflet.js')
    	response.files.append('http://cdn.leafletjs.com/leaflet-0.7/leaflet.css')
    	return {}
     
def get_geojson():
	rows= db(db.geostuff).select(db.geostuff.name, db.geostuff.geometry.st_asgeojson())
     
    	features= [{"type": "Feature",
    			"properties": {
    				"popupContent": r[db.geostuff.name]
    			},
    			"geometry": loads_json(r[db.geostuff.geometry.st_asgeojson()])} for r in rows]
     
    	return response.json({"type": "FeatureCollection", 'features': features})
