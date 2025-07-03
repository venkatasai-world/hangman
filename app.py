from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'vangman-secret-key'  # Required for session storage

word_list = ["aardvark", "baboon", "camel", "dolphin", "elephant", "flamingo", "giraffe", "hamster", "iguana",
             "jaguar", "kangaroo", "lemur", "meerkat", "narwhal", "ocelot", "panda", "quokka", "raccoon",
             "sloth", "tiger", "urial", "vulture", "walrus", "xerus", "zebra"]

@app.route("/", methods=["GET", "POST"])
def index():
    if 'word' not in session:
        word = random.choice(word_list)
        session['word'] = word
        session['display'] = ['_'] * len(word)
        session['lives'] = len(word)
        session['guessed'] = []

    if request.method == "POST":
        guess = request.form['letter'].lower()
        if guess and guess not in session['guessed']:
            session['guessed'].append(guess)
            word = session['word']
            for idx, letter in enumerate(word):
                if letter == guess:
                    session['display'][idx] = guess
            session['lives'] -= 1

        if "_" not in session['display']:
            message = "🎉 You Won! The word was: " + session['word']
            session.clear()
            return render_template("index.html", display=[], message=message, win=True)

        if session['lives'] <= 0:
            message = "💀 Game Over! The word was: " + session['word']
            session.clear()
            return render_template("index.html", display=[], message=message, win=False)

    return render_template("index.html", display=session.get('display', []),
                           guessed=session.get('guessed', []),
                           lives=session.get('lives', 0),
                           message="", win=None)

@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
