from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/fail')
def fail():
    return render_template('fail.html')

@app.route('/', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['name'] and request.form['pass']:
            return redirect(url_for('success'))
        else:
            return redirect(url_for('fail'))
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)