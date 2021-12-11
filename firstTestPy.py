import requests
import spacy
import json

def get_activity():
    api = f"https://www.boredapi.com/api/activity"
    response = requests.get(api)
    content = response.json()
    return content

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
