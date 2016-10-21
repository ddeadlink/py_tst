from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:connect565@localhost/test_task'

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    surname = db.Column(db.String(80), unique=False)
    position = db.Column(db.String(80), unique=False)
    mail = db.Column(db.String(80), unique=True)
    phone = db.Column(db.Integer, unique=True)
    birth = db.Column(db.Integer, unique=False)

    def __init__(self, name, surname, position, mail, phone, birth):
        self.name = name
        self.surname = surname
        self.position = position
        self.mail = mail
        self.phone = phone
        self.birth = birth


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
    description = db.Column(db.String(80), unique=False)

    def __init__(self, name, head, description):
        self.name = name
        self.head = head
        self.description = description

@app.route('/')
def index():
    return render_template('main.html')


@app.route('/view/<arg>')
def view(arg):
    if arg == 'user':
        res = Users.query.all()
    elif arg == 'position':
        res = Profile.query.all()
    return render_template('view.html', res = res, arg = arg)

@app.route('/create/<arg>')
def create(arg):
    positions = Profile.query.all()
    return render_template('create_new.html', arg = arg, positions = positions)

@app.route('/post/<arg>',methods=['POST'])
def post(arg):
    if arg == 'user':
        user = Users(request.form['name'],request.form['surname'],request.form['position'],request.form['mail'],request.form['phone'],request.form['birth'])
        db.session.add(user)
        db.session.commit()
    elif arg == 'position':
        position = Profile(request.form['name'],request.form['description'])
        db.session.add(position)
        db.session.commit()

    return redirect(url_for('index'))

@app.route('/ajax', methods=['POST'])
def ajax():
    if str(request.form['key']) == 'user':
        res = Users.query.filter_by(id=str(request.form['id'])).first()
        db.session.delete(res)
        db.session.commit()
    elif str(request.form['key']) == 'position':
        res = Profile.query.filter_by(id=str(request.form['id'])).first()
        db.session.delete(res)
        db.session.commit()
    return str(res.name)

if __name__ == "__main__":
    app.run(debug=True)
