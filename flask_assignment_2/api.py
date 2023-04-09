from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = {}

class Register(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help='Username is required.')
        parser.add_argument('password', type=str, required=True, help='Password is required.')
        args = parser.parse_args()
        print(users)

        if args['username'] in users:
            return {'message': 'Username already exists. Please choose a different username.'}, 400

        users[args['username']] = args['password']
        return {'message': 'User registered successfully.'}, 201

class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help='Username is required.')
        parser.add_argument('password', type=str, required=True, help='Password is required.')
        args = parser.parse_args()
        print(users)

        if args['username'] not in users or users[args['username']] != args['password']:
            return {'message': 'Access denied.'}, 401

        return {'message': 'Access granted.'}, 200

api.add_resource(Register, '/register')
api.add_resource(Login, '/login')

if __name__ == '__main__':
    app.run(debug=True)
