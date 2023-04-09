from flask import Flask, request
from flask_restful import Api, Resource, reqparse, inputs

app = Flask(__name__)
api = Api(app)

class Sum(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('numbers', type=inputs.positive, action='append', required=True, help='Invalid input. Please provide a list of valid numbers. Note: Positive Numbers only.')
        args = parser.parse_args()
        try:
            result = sum(args['numbers'])
            return {'result': result}, 200
        except TypeError:
            return {'error': 'Invalid argument. Please provide a list of valid numbers.'}, 400

class Concat(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('string1', type=str, required=True, help='Invalid argument. Please provide a valid string.')
        parser.add_argument('string2', type=str, required=True, help='Invalid argument. Please provide a valid string.')
        args = parser.parse_args()
        try:
            result = args['string1'] + args['string2']
            return {'result': result}, 200
        except TypeError:
            return {'error': 'Invalid argument. Please provide valid strings'}

api.add_resource(Sum, '/sum')
api.add_resource(Concat, '/concat')

if __name__ == '__main__':
    app.run(debug=True)