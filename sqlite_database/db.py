from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask("SawanDB")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite'

#ORM (Object Relation Mapping)
db = SQLAlchemy(app)
print(db)
class SawanDB(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.TEXT)
    age = db.Column(db.Integer)
    remarks = db.Column(db.TEXT)

    def __init__(self,name,age,remarks):
        self.name = name
        self.age = age
        self.remarks = remarks

db.create_all()

#Create Rows
sonu = SawanDB("sonu",15,"good")
db.session.add(sonu)
db.session.commit()
