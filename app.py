from flask import Flask, render_template, json, request

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/sobre.html')
def sobrepage():
    return render_template('sobre.html')

@app.route('/index.html')
def backhome():
    return render_template('/index.html')

if __name__ == '__main__':
    app.run('localhost')