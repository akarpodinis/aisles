from os import path

from flask import Flask, render_template, send_from_directory

from cache import cache
from lists import ListAPI

app = Flask('aisles')

app.add_url_rule('/lists/', view_func=ListAPI.as_view('lists'), methods=['GET'], defaults={'name': None})
app.add_url_rule('/lists/<name>', view_func=ListAPI.as_view('list'), methods=['GET', 'POST', 'PUT', 'DELETE'])


@app.route('/')
def index():
    lists = cache.get('lists')

    lists = ['First', 'Second', 'Third']

    if lists:
        lists.insert(0, f'Choose a list, out of {len(lists)}')
    else:
        lists = ['No lists. Go make some!']

    return render_template('status.html', lists=lists)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(path.join(app.root_path, 'static'),
                               'images\\favicon\\favicon.ico', mimetype='image/vnd.microsoft.icon')
