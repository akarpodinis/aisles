from flask import Flask, render_template

from cache import cache

app = Flask('aisles')


@app.route('/')
def index():
    lists = cache.get('lists')

    list_status = 'Found a list!' if lists else 'No lists yet!'

    return render_template('status.html', list_status=list_status)
