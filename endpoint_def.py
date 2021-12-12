from flask import Flask, render_template
from flask_restful import Resource, Api
from main import exp_act_joke
from main import export_log
import psycopg2
import os

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

class ActJoke(Resource):
    def get(self, type_act):
        return exp_act_joke(type_act)

class ExportCsv(Resource):
    def get(self):
        return export_log(conn)
