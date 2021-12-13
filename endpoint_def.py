from flask import Flask, render_template, jsonify
from flask_restful import Resource, Api
from main import exp_act_joke
from main import act_joke
from main import export_log
from main import export_log_complete
import psycopg2
import os

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')


class ActJoke(Resource):
    def get(self, type_act):
        res = act_joke(type_act)
        if res["unrecognized"]:
            return {"error": 400, "message": "The act_type you gave is unrecognized. It should be one of 'education', 'recreational', 'social', 'diy', 'charity', 'cooking', 'relaxation', 'music', 'busywork'. Note: for example https:/marbotteantiboredom.herokuapp.com/ActJoke/charity"}, 400
        else:
            return exp_act_joke(res),200

class ExportCsv(Resource):
    def get(self):
        return export_log(conn), 200

class ExportCsvComplete(Resource):
    def get(self):
        return export_log_complete(conn), 200
