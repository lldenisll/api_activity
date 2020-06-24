from models import Persons, Users

def insert_person():
    person = Persons(name='Denis', age = '27')
    print(person)
    person.save()

def consult():
    person = Persons.query.all()
    person = Persons.query.filter_by(name='Denis').first()
    print(person.age)

def change():
    person = Persons.query.filter_by(name='Denis').first()
    person.age = 21
    person.save()

def delete_person():
    person = Persons.query.filter_by(name='Denis').first()
    person.delete()

def inser_user(login, password):
    user = Users(login = login, password=password)
    user.save()

def consult_user():
    user = Users.query.all()


if __name__ == '__main__':
    #delete_person()
    #insert_person()
    #change()
    #consult()
    inser_user('denis','123')