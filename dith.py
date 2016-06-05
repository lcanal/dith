from flask import Flask,url_for,render_template
from os import environ as env

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',apikey=env['STATTLESHIP_API_KEY'])


## Game 1 function
@app.route('/nbafinals-game1')
def nbafinalsGame1():
    return 'player,assist,point'
    #return render_template('game1.html')

if __name__ == "__main__":
    app.run()
