from flask import Flask, render_template, request
from PyDictionary import PyDictionary

app = Flask(__name__)
dictionary=PyDictionary()

@app.route('/', methods=['GET', 'POST'])
def index():
    word = 'dictionary'
    if request.method == 'POST':
        word = request.form.get('word', 'dictionary')

    try:
        meaning = dictionary.meaning(word)
        synonyms = dictionary.synonym(word)
        antonyms = dictionary.antonym(word)
    except:
        meaning = dictionary.meaning('dictionary')
        synonyms = dictionary.synonym('dictionary')
        antonyms = dictionary.antonym('dictionary')

    return render_template('index.html', word=word, meaning=meaning, synonyms=synonyms, antonyms=antonyms)

if __name__ == '__main__':
	app.run()
