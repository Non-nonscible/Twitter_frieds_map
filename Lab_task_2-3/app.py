from flask import Flask, render_template, request
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
        data = get_json.get(username)
        friends_map.create_map(data)
        return render_template('Friends_map.html')

if __name__ == '__main__':
    app.run(debug=True)



