from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "eh"

@app.route('/vaa')
def vaa():
    os.system('python3 eat.py')
    return '<h2>vaa</h2>'

if __name__=="__main__":
    app.run(debug=True)