#!/usr/bin/python3
    

from flask import Blueprint
from models import storage
from api.v1.views import app_views
from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext('/teardown_appcontext', methods=['GET', 'POST'])
def teardown_appcontext():
    if request.method == 'POST':
        return storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    app.run(threaded=True)
