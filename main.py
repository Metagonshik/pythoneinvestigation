from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api()

family = {1: {"name": "Руслан", "Батчаев": 32},
           2: {"name": "Екатерина", "Батчаева": 35}}

class Main(Resource):
    def get(self, family_id):
        if family_id == 0:
            return family
        else:
            return family[family_id]

    def delete(self, family_id):
        del family[family_id]
        return family



api.add_resource(Main, "/api/courses/<int:family_id>")
api.init_app(app)
if __name__ == "__main__":
    app.run(port=3000, host="127.0.0.1")
