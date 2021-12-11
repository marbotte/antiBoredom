from flask import Flask
from flask_restful import Api, Resource, abort
from endpoint_def import ActJoke

app = Flask(__name__)
api = Api(app)

api.add_resource(ActJoke, '/ActJoke/<string:type_act>')

if __name__ == "__main__":
    app.run()
