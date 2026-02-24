from flask_restful import Resource, request
from flask import jsonify
import csv
import json

class Ingredients(Resource):
    def get(self):
        csvfile = open('src/mock_db/ingredients.csv', 'r', encoding='utf-8')
        json_file = open('src/mock_db/ingredients.json', 'w', encoding='utf-8')
        columns = ("Ingredient", "IsVegan")
        reader = csv.DictReader(csvfile, columns)
        out = json.dumps([row for row in reader])
        return out