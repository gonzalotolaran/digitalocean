from app import app, db
from flask import render_template
from app.schemas import User

@app.route('/insert/<string:username>')
def insert(username):
    newUser = User(username=username, password='123456')
    db.session.add(newUser)
    db.session.commit()
    return 'Username: {} correctamente creado'.format(username)

@app.route('/users')
def selectUsers():
    user = User.query.filter_by(username='gonzalotolaran').first()
    return 'id {}, username: {}, password: {}'.format('1', user.username, user.password)

@app.route('/')
def index():
    titulo = 'Probando'
    lista = ['uno', 'dos', 'tres']
    return render_template('index.html', titulo=titulo, lista=lista)