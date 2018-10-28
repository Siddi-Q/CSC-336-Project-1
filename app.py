from flask import Flask, render_template, url_for, flash, redirect
from flaskext.mysql import MySQL
from forms import SignInForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e10afc8bf64730d5b6c370c8c2c4fe35'

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'saddique'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'mydb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/test")
def testing():
    cursor = mysql.connect().cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    return render_template('test.html', tables = tables)

@app.route("/")
def hello():
    return "<h1>Home Page<h1>"

@app.route("/signin", methods=['GET', 'POST'])
def signin():
    form = SignInForm()
    if form.validate_on_submit():
        flash(f'{form.fullname.data} has been signed in!', 'success')
        return redirect(url_for('hello'))
    return render_template('signin.html', form = form)

if __name__ == '__main__':
    app.run(debug=True)
