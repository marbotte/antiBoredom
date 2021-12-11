from flask_restful import Resource
import requests
import spacy



def get_activity(type_act: str):
    if type_act not in ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"]:
        return "I am a computer... As such I am very dumb, and I did not reocognise your activity type. It should be one of 'education', 'recreational', 'social', 'diy', 'charity', 'cooking', 'relaxation', 'music', 'busywork'"
    api = f"https://www.boredapi.com/api/activity?type={type_act}"
    response = requests.get(api)
    return response["activity"]

def extract_noun(text: str):
    load_spacy = spacy.load("en_core_web_sm")
    nouns = load_spacy(text)
    return [i.text for i in nouns.noun_chunks]

def get_joke(word_contains: str):
    api = f"https://v2.jokeapi.dev/joke/Any?contains={word_contains}"
    response = requests.get(api)
    content = response.json()
    if content["error"]:
        joke = 'This is a very boring activity'
    else:
        if content["type"] == 'single':
            joke = content["joke"]
        elif content["type"] == 'twopart':
            joke = content["setup"] + ' -> ' + content["delivery"]
        else: 
            joke= 'This is a very boring activity (type of joke unrecognized)'
    return(joke)
