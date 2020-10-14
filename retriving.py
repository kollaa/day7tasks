from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import csv

app = Flask(__name__)
api = Api(app)


class Retriving(Resource):

    def get(self):
        with open('students.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
              return(row)

api.add_resource(Retriving, '/retriving')

if __name__ == '__main__':
    app.run(port = 5000 , debug = True )