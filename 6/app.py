from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/result/<name>/<int:score>', methods = ['GET', 'POST'])
def result(name, score):
    return render_template('index.html', nm = name, marks = score)


@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        marks = request.form['marks']
        user = request.form['name']
        return redirect(url_for('result', name = user, score = marks))
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug = True)