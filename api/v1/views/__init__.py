#!/usr/bin/python3
   " erpgfn "


from flask import Blueprint
from flask import Flask

app_views = Flask(__name__)
app-views.register_blueprint(app-views_blueprint, url_prefix = "/api/v1")
