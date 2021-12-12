from flask_restful import Resource
import requests
import spacy
import random
import re
import json
import os
import psycopg2
from psycopg2 import sql




DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')


def get_activity(type_act: str):
    if type_act not in ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"]:
        return {"unrecognized": True, "activity": "I am a computer... As such I am very dumb, and I did not reocognise your activity type. It should be one of 'education', 'recreational', 'social', 'diy', 'charity', 'cooking', 'relaxation', 'music', 'busywork'", "key_act": None}
    api = f"https://www.boredapi.com/api/activity?type={type_act}"
    response = requests.get(api)
    content = response.json()
    return {"unrecognized": False, "type_act": type_act, "activity": content["activity"],"key_act": content["key"]}

def extract_noun(text: str):
    load_spacy = spacy.load("en_core_web_sm")
    nouns = load_spacy(text)
    return [i.text for i in nouns.noun_chunks]

def extract_words(text: str):
    pattern = '[A-Za-z]+'
    words = re.findall(pattern, text)
    del_items = ["A", "a", "s", "An", "an", "The", "the", "One", "one", "is", "This", "this", "That", "that", "get", "on", "up", "down", "in", "your", "to", "with", "make", "are", "be", "go", "some", "have", "Have", "and", "it", "out", "at", "I", "am", "very", "not"]
    return [x for x in words if x not in del_items]

def get_joke(word_contains: str):
    api = f"https://v2.jokeapi.dev/joke/Any?contains={word_contains}"
    response = requests.get(api)
    content = response.json()
    joke = "This is a very boring activity"
    if content["error"]:
        return {"error": content["error"], "joke": joke, "id_joke": None}
    else:
        if content["type"] == 'single':
            joke = content["joke"]
        elif content["type"] == 'twopart':
            joke = content["setup"] + ' -> ' + content["delivery"]
#        else: 
#            joke= 'This is a very boring activity (type of joke unrecognized)'
    return {"error": content["error"], "joke": joke, "id_joke": content["id"]}

def insert_db(row: dict, connection):
    cur = connection.cursor()
    cols = row.keys()
    query = sql.SQL("INSERT INTO antiboredom_log ({}) VALUES ({})").format(
        sql.SQL(', ').join(map(sql.Identifier, cols)),
        sql.SQL(', ').join(map(sql.Placeholder, cols)))
    cur.execute(query,row)
    connection.commit()
    
def act_joke(type_act: str):
    act = get_activity(type_act)
    extracted = extract_words(act["activity"])
    if len(extracted) < 2 or act["unrecognized"]:
        word = extracted[0]
        res_joke = get_joke(word)
    else:
        random.shuffle(extracted)
        word = extracted[0]
        res_joke = get_joke(word)
        if res_joke["error"]:
            print(word)
            word = extracted[1]
            res_joke = get_joke(word)
    extensive_res = {**act, **res_joke, **{"word": word}}
    insert_db(extensive_res, conn)
    return extensive_res
#    return extracted
#    return {"activity": act["activity"], "joke": res_joke["joke"]}

def exp_act_joke(type_act: str):
    extensive_res = act_joke(type_act)
    return json.dumps({"activity": extensive_res["activity"], "joke": extensive_res["joke"]})


