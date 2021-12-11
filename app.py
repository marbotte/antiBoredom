from flask import Flask
from flask_resful import Api

from resources.endpoint_def

app = Flask(__name__)
api = Api(app)

api.add_resource(Endpoint, "endpoint/<int:id>")

if __name__ == "__main__":
    app.run()
