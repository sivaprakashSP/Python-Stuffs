from googletrans import Translator
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to Translator'

@app.route('/translate/<word>')
def translation(word):
    translator = Translator(service_urls=['translate.google.com'])
    translation1 = translator.translate(word, dest="ta")

    return translation1.text

app.run()