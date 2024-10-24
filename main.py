from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)




@app.route("/")
@app.route("/index")
def index2():
    user = "User"
    return render_template('index.html', title='Главная', username=user)

@app.route("/stati")
def index1():
    user = "User"
    return render_template('stati.html', title='Главная', username=user)


@app.route("/contact")
def index4():
    user = "User"
    return render_template('contact.html', title='Главная', username=user)

@app.route("/razrab")
def index5():
    user = "User"
    return render_template('razrab.html', title='Главная', username=user)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Модель данных для пользователей
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    profession = db.Column(db.String(100), nullable=False)
    expierence = db.Column(db.String(10), nullable=False)


# Создать таблицы в базе данных (выполнить один раз)
with app.app_context():
    db.create_all()

# Главная страница с регистрационной формой
@app.route('/volunteers', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        profession = request.form['profession']
        experience = request.form['experience']


        # Создание нового пользователя
        new_user = User(
            username=username,
            email=email,
            password=password,
            profession=profession,
            experience=experience

        )

        # Добавление пользователя в базу данных
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect('/auto_answer')  # Перенаправление после успешной регистрации
        except:
            return 'Ошибка при добавлении данных в базу'

    return render_template('volunteers.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)