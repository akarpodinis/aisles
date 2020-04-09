from os import path

from flask import Flask, render_template, send_from_directory

from cache import cache

app = Flask('aisles')


@app.route('/')
def index():
    lists = cache.get('lists')

    lists = ['First', 'Second', 'Third']

    list_status = 'Found a list!' if lists else 'No lists yet!'

    return render_template('status.html', list_status=list_status, lists=lists)
