from flask import Flask, render_template, request
from PyDictionary import PyDictionary

app = Flask(__name__)
dictionary=PyDictionary()

@app.route('/')
def index():
    word = 'dictionary'
    word = request.args.get('word', 'dictionary')

    try:
        meaning = dictionary.meaning(word)
    except:
        meaning = dictionary.meaning('dictionary')

    return render_template('index.html', word=word, meaning=meaning)

if __name__ == '__main__':
	app.run()
