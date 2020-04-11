import json

from flask import jsonify

from aisles.cache import cache


def seed(delete):
    if cache.exists('seeded') and delete:
        cache.delete('seeded')
        cache.delete('Shopping on Friday')
        return 'Seed deleted', 200
    if cache.exists('seeded'):
        return jsonify(json.loads(cache.get('Shopping on Friday')))
    cache.set('Shopping on Friday', json.dumps(
        [
            {'Produce': [{'item': '2 Onions'}, {'item': '2 Squash'}, {'item': '2 Potatoes'}]},
            {'Aisle 4': [{'item': '5 lbs Flour'}]}
        ]
    ))
    cache.set('seeded', 1)
    return jsonify(json.loads(cache.get('Shopping on Friday')))
