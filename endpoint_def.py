from flask import Flask
from flask_restful import Resource, Api, reqparse
from my_functions import get_activity
from my_functions import get_joke

class ActJoke(Resource):
    def get(self, type_act):
        return get_activity(type_act)
    
