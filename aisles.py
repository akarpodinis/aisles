from flask import Flask

app = Flask('aisles')


@app.route('/')
def index():
    return 'Working!'
