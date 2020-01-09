from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return render_template('index.html', user = name)

@app.route('/', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('success', name = user))
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)

