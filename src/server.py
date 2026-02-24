from flask import Flask
from flask_restful import Resource, Api
from api.vegan_or_not import VeganOrNot
from api.ingredients import Ingredients

app = Flask(__name__)
api = Api(app)

api.add_resource(VeganOrNot, '/') 
api.add_resource(Ingredients, '/ingredients')

if __name__ == '__main__':
    app.run(debug=True, port=8080)