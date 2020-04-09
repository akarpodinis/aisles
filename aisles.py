from flask import Flask

from cache import cache

app = Flask('aisles')


@app.route('/')
def index():
    lists = cache.get('lists')
    if lists:
        return 'Found a list!'
    else:
        return 'No lists yet!'
