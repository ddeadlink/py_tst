from main import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    surname = db.Column(db.String(80), unique=False)
    department = db.Column(db.String(80), unique=False)
    position = db.Column(db.String(80), unique=False)
    mail = db.Column(db.String(80), unique=True)
    phone = db.Column(db.String(80), unique=True)
    birth = db.Column(db.Integer, unique=False)
    master = db.Column(db.Integer, unique=False)

    def __init__(self, name, surname, position, department, mail, phone, birth, master):
        self.name = name
        self.surname = surname
        self.position = position
        self.department = department
        self.mail = mail
        self.phone = phone
        self.birth = birth
        self.master = master


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    description = db.Column(db.String(80), unique=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    head = db.Column(db.String(80), unique=False)
    parent = db.Column(db.String(80), unique=False)
    description = db.Column(db.String(80), unique=False)

    def __init__(self, name, head, parent, description):
        self.name = name
        self.head = head
        self.parent = parent
        self.description = description
