from flask import Flask
from flask_restful import Resource, Api, reqparse
from my_functions import act_joke

class ActJoke(Resource):
    def get(self, type_act):
        return act_joke(type_act)
    
