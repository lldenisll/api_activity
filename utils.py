from models import Persons

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

if __name__ == '__main__':
    #delete_person()
    insert_person()
    change()
    consult()