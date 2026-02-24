from flask_restful import Resource, request
from flask import jsonify
import csv
import json

class VeganOrNot(Resource):
    def get(self):
        return "Vegan Or Vegan't?"
    
    def post(self):
        data = request.json
        food = data.get("food")

        return jsonify({"vegan?":"pending...","input": food})
    

    """
    resources:
    ingredientsResource - post new ingredient, put to update exisiting ingredient, delete, get (vegan, not vegan, expand to more diets)
    lookupResource - post item query,
    nutritionInfoResource? - put to update existing ingredient, delete, get ingredient info
    publicApiResource?
    
    """