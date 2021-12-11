from flask_restful import Resource


endpoints = [
    {
        "id": 1,
        "name": "GetActivity"
    },
    {
        "id": 2,
        "name": "GetJoke"
    }
]

class Endpoint(Resource):
    def get(self,id):
        for endpoint in endpoints:
            if(id == endpoint["id"]
               return endpoint, 200
           return "Endpoint not found for id {}".format(id) ,404
        
    
