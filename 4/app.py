#Simple admin-panel
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/admin')
def helloAdmin():
    return 'Hello Admin!'

@app.route('/guest/<name>')
def helloGuest(name):
    return 'Hello %s!' % name

@app.route('/user/<user>')
def helloUser(user):
    if user == 'admin':
        return redirect(url_for('helloAdmin'))
    else:
        return redirect(url_for('helloGuest', name = user))

if __name__ == "__main__":
    app.run(debug=True)
