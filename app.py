from flask import Flask, render_template, url_for, flash, redirect
from flaskext.mysql import MySQL
from forms import SignInForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e10afc8bf64730d5b6c370c8c2c4fe35'

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'saddique'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'hospital'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)
connect = mysql.connect()

@app.route("/test")
def testing():
    cursor = connect.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    return render_template('test.html', tables = tables)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/signin", methods=['GET', 'POST'])
def signin():
    form = SignInForm()
    if form.validate_on_submit():
        flash(f'{form.fullname.data} has been signed in!', 'success')
        cursor = connect.cursor()
        cursor.execute(''' INSERT INTO patient VALUES (%s, %s, %s, %s, %s, %s, %s)''',
                (form.ssn.data, form.fullname.data, form.gender.data, form.date_of_birth.data,
                form.address.data, form.phone_number.data, form.emergency_contact_number.data))
        connect.commit()
        cursor.execute(''' INSERT INTO emergencycontact VALUES(%s, %s, %s)''',
                (form.ssn.data, form.emergency_contact_name.data, form.emergency_contact_number.data))
        connect.commit()
        return redirect(url_for('hello'))
    return render_template('signin.html', form = form)

if __name__ == '__main__':
    app.run(debug=True)
