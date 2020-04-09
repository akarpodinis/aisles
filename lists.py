import json
from functools import wraps

from flask import jsonify, request
from flask.views import MethodView
from werkzeug.exceptions import Conflict, NotFound

from cache import cache


class ListAPI(MethodView):
    def get(self, name):
        if not name:
            return jsonify(lists=cache.keys())
        if not cache.exists(name):
            raise NotFound
        return jsonify(name=name, items=json.loads(cache.get(name)))

    def post(self, name):
        if not cache.exists():
            raise NotFound
        cache.set(name, request.json['items'])
        return jsonify(name=name, items=json.loads(cache.get(name)))

    def delete(self, name):
        cache.delete(name)

    def put(self, name):
       self.delete(name)
       return self.post(name)
