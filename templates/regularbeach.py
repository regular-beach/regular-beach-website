from flask import Flask, render_template, request
from waitress import serve

app = Flask(__name__)


@app.route('/')

@app.route('/index')
def index():
    return 'Hello, World! Im Mclovin'

@app.route('/')
def work():
    return render_template('work.html', work_list = fname)

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)


    