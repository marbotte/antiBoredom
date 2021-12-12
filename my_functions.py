from flask_restful import Resource
import requests
import spacy
import random
import re



def get_activity(type_act: str):
    if type_act not in ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"]:
        return "I am a computer... As such I am very dumb, and I did not reocognise your activity type. It should be one of 'education', 'recreational', 'social', 'diy', 'charity', 'cooking', 'relaxation', 'music', 'busywork'"
    api = f"https://www.boredapi.com/api/activity?type={type_act}"
    response = requests.get(api)
    content = response.json()
    return {"unrecognized": False, "type_act": type_act, "activity": content["activity"],"key": content["key"]}

def extract_noun(text: str):
    load_spacy = spacy.load("en_core_web_sm")
    nouns = load_spacy(text)
    return [i.text for i in nouns.noun_chunks]

def extract_words(text: str):
    pattern = '[A-Za-z]+'
    words = re.findall(pattern, text)
    del_items = ["A", "a", "s", "An", "an", "The", "the", "One", "one", "is", "This", "this", "That", "that", "get", "on", "up", "down", "in", "your", "to", "with", "make", "are", "be", "go", "some", "have", "Have"]
    return [x for x in words if x not in del_items]

def get_joke(word_contains: str):
    api = f"https://v2.jokeapi.dev/joke/Any?contains={word_contains}"
    response = requests.get(api)
    content = response.json()
    joke = "This is a very boring activity"
    if content["error"]:
        return {"error": content["error"], "joke": joke, "id": type(None)}
    else:
        if content["type"] == 'single':
            joke = content["joke"]
        elif content["type"] == 'twopart':
            joke = content["setup"] + ' -> ' + content["delivery"]
#        else: 
#            joke= 'This is a very boring activity (type of joke unrecognized)'
    return {"error": content["error"], "joke": joke, "id": content["id"]}

def act_joke(type_act: str):
    act = get_activity(type_act)
    print(act)
    extracted = extract_words(act["activity"])
    print(extracted)
    if len(extracted) == 0:
        res_joke = {"error": True, "joke": "This is a very boring activity", "id": type(None)}
    elif len(extracted) == 1:
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
    print(word)
#    return extracted
    return {"activity": act["activity"], "joke": res_joke["joke"]}
