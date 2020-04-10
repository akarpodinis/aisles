from os import path

from flask import Flask, render_template, send_from_directory

from cache import cache
from lists import ListAPI, ListEditView
from seed import seed

app = Flask('aisles')

app.add_url_rule('/lists/', view_func=ListAPI.as_view('lists'), methods=['GET'], defaults={'name': None})
app.add_url_rule('/lists/<name>', view_func=ListAPI.as_view('list'), methods=['GET', 'POST', 'PUT', 'DELETE'])
app.add_url_rule('/lists/edit', view_func=ListEditView.as_view('list_edit'), methods=['GET'])

# Seeding for testing, don't actually ship this later
app.add_url_rule('/seed/', view_func=seed, defaults={'delete': None})
app.add_url_rule('/seed/<delete>', view_func=seed)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(path.join(app.root_path, 'static'),
                               'images\\favicon\\favicon.ico', mimetype='image/vnd.microsoft.icon')
