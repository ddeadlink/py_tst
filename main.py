from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:connect565@localhost/test_task'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://osfqbysgftyykd:g6VxXCxQoi7trxPTkmMfgtv_x2@ec2-54-75-232-54.eu-west-1.compute.amazonaws.com/dbpb9v07deo1nu'
db = SQLAlchemy(app)

from models import *

@app.route('/')
def index():
    return render_template('main.html')


@app.route('/view/<arg>')
def view(arg):
    if arg == 'user':
        res = Users.query.all()
    elif arg == 'position':
        res = Profile.query.all()
    elif arg == 'department':
        res = Department.query.all()
    return render_template('view.html', res = res, arg = arg)

# create tpl for all components
@app.route('/create/<arg>')
def create(arg):
    positions = Profile.query.all()
    # query departments with no master
    departments = Department.query.filter_by(head=str('')).all()
    users = Users.query.filter_by(head=str('')).all()
    return render_template('create_new.html', arg = arg, positions = positions, users = users, departments = departments)

# to post data to db
@app.route('/post/<arg>',methods=['POST'])
def post(arg):
    if arg == 'user':
        user = Users(request.form['name'],request.form['surname'],request.form['position'],\
                request.form['department'],request.form['mail'],request.form['phone'],request.form['birth'])
        db.session.add(user)
        db.session.commit()

    elif arg == 'position':
        position = Profile(request.form['name'],request.form['description'])
        db.session.add(position)
        db.session.commit()

    elif arg == 'department':
        department = Department(request.form['name'],request.form['parent'],request.form['head'],request.form['description'])
        db.session.add(department)
        db.session.commit()

    return redirect(url_for('index'))

@app.route('/update/<arg>/<int:id>')
def update(arg,id):
    if arg == 'user':
        user = Users.query.filter_by(id=id).first()
        positions = Profile.query.all()
        # query departments with no master
        departments = Department.query.filter_by(head=str('')).all()
        return render_template('update.html', arg = arg, positions = positions, departments = departments, one = user)
    if arg == 'position':
        positions = Profile.query.filter_by(id=id).first()
        return render_template('update.html', arg = arg, positions = positions)


# ajax handler to delete components
@app.route('/ajaxDelete', methods=['POST'])
def ajaxDelete():
    if str(request.form['key']) == 'user':
        res = Users.query.filter_by(id=str(request.form['id'])).first()
        db.session.delete(res)
        db.session.commit()
    elif str(request.form['key']) == 'position':
        res = Profile.query.filter_by(id=str(request.form['id'])).first()
        db.session.delete(res)
        db.session.commit()
    return str(res.name)

@app.route('/post_update/<arg>/<int:id>', methods=['POST'])
def post_update(arg,id):
    if arg == 'user':
        db.session.query(Users).filter(Users.id == id).update({'name': request.form['name'],'surname': request.form['surname'],\
        'department': request.form['department'],'position': request.form['position'],'mail': request.form['mail'],'phone': request.form['phone'],\
        'birth': request.form['birth']})
        db.session.commit()
    elif arg == 'position':
        db.session.query(Profile).filter(Profile.id == id).update({'name': request.form['name'],'description': request.form['description']})
        db.session.commit()

    return redirect(url_for('view',arg=arg))


if __name__ == "__main__":
    app.run(debug=True)
