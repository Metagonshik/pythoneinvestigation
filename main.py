from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api()

courses = {1: {"name": "Руслан", "Батчаев": 32},
           2: {"name": "Екатерина", "Батчаева": 35}}

class Main(Resource):
    def get(self, course_id):
        if course_id == 0:
            return courses
        else:
            return courses[course_id]

    def delete(self, course_id):
        del courses[course_id]
        return courses



api.add_resource(Main, "/api/courses/<int:course_id>")
api.init_app(app)
if __name__ == "__main__":
    app.run(port=3000, host="127.0.0.1")
