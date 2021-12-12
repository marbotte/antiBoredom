from flask import Flask
from flask_restful import Resource, Api
from my_functions import exp_act_joke

class ActJoke(Resource):
    def get(self, type_act):
        return exp_act_joke(type_act)
    
