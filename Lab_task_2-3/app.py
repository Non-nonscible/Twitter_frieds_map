import flask
from flask import Flask, redirect, render_template, url_for, request
import get_json
import friends_map
app = Flask(__name__)

@app.route('/')
def func():
    return render_template('index.html')
    
@app.route('/Map', methods = ['POST'])
def func1():
    if request.method == 'POST':

        username = request.form['n']
        get_json.get(username)
        friends_map.create_map()
        return render_template('Friends_map.html')

if __name__ == '__main__':
    app.run(debug=True)



