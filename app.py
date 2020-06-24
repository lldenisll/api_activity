from flask import Flask, request
from flask_restful import Resource, Api
from models import Persons, Activity, Users
import json
from flask_httpauth import HTTPBasicAuth

auth=HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

#users = {
#    'Denis':'123',
#    'denis':'321'
#}

@auth.verify_password
def verify(login, password):
    if not (login,password):
        return False
    return Users.query.filter_by(login=login, password=password).first()

class Person(Resource):
    @auth.login_required
    def get(self, name):
        person = Persons.query.filter_by(name=name).first()
        try:
            response={
                'name': person.name,
                'age': person.age,
                'id': person.id
            }
            return response
        except AttributeError:
            response={
                'status': 'error',
                'message': 'person not found'
            }
    def put(self,name):
        person=Persons.query.filter_by(name=name).first()
        data = request.json
        if 'name' in data:
            person.name=data['name']
        if 'age' in data:
            person.age = data['age']
        person.save()
        response = {
            'id': person.id,
            'name': person.name,
            'age': person.age,
        }
        return response
    def delete(self, name):
        person = Persons.query.filter_by(name=name).first()
        person.delete()
        return {'status':'sucess','message': 'person deleted'}
class List_persons(Resource):
    @auth.login_required
    def get(self):
        person = Persons.query.all() #big data never use this
        response = [{'id':i.id,'name':i.name,'age':i.age} for i in person]
        return response
    def post(self):
        data = request.json
        person = Persons(name=data['name'],age=data['age'])
        person.save()
        response={
            'id': person.id,
            'name': person.name,
            'age': person.age,
        }
        return response
class ListActivity(Resource):
    def get(self):
        activity=Activity.query.all()
        response = [{'id': i.id,'name':i.name,'person':i.person.name} for i in activity]
        return response
    def post(self):
        data = request.json
        person = Persons.query.filter_by(name=data['person']).first()
        activity = Activity(name=data['name'], person = person)
        activity.save()
        response = {
            'person':activity.person.name,
            'name': activity.name
        }
        return response


api.add_resource(Person,'/person/<string:name>/')
api.add_resource(List_persons, '/person/')
api.add_resource(ListActivity,'/activity/')
if __name__ == '__main__':
    app.run(debug=True)