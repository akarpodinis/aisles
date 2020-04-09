from functools import wraps

from flask import jsonify, request
from flask.views import MethodView
from werkzeug.exceptions import Conflict, NotFound

from cache import cache


class ListAPI(MethodView):
    def get(self, name):
        if not name:
            return jsonify(lists=cache.get('list_*'))
        list_name = 'list_' + name
        if not cache.exists(list_name):
            raise NotFound
        return jsonify(name=name, items=cache.get(list_name))

    def post(self, name):
        list_name = 'list_' + name
        if not cache.exists():
            raise NotFound
        cache.set('list_' + name, request.json['items'])
        return jsonify(name=name, items=cache.get(list_name))

    def delete(self, name):
        cache.delete('list_' + name)

    def put(self, name):
       self.delete(name)
       return self.post(name)
