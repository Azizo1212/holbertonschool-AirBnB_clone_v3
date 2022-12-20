#!/usr/bin/python3
    "api"


import app_views from api.v1.views

@app.route('/status')
def app_views():
    return 'OK'
