from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/<word>')
def toword(word):
    return {'definition': word.upper(),
            'word': word
    }


if __name__ == '__main__':
    app.run(debug=True, port=5001)