from flask import Flask
from flask_restful import Api, Resource, abort
from endpoint_def import ActJoke
from endpoint_def import ExportCsv

app = Flask(__name__, static_folder='static', static_url_path='')
api = Api(app)

@app.route('/')
def mainPage():
    return(app.send_static_file("home.html"))

api.add_resource(ActJoke, '/ActJoke/<string:type_act>')
api.add_resource(ExportCsv, '/Export')

if __name__ == "__main__":
    app.run()
