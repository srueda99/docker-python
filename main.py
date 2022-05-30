from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)

# SQL Configuration
app.config['MYSQL_HOST'] = os.getenv("DB_HOST")
app.config['MYSQL_USER'] = os.getenv("DB_USER")
app.config['MYSQL_PASSWORD'] = os.getenv("DB_PASSWORD")
app.config['MYSQL_DB'] = os.getenv("DB_SCHEMA")
database = MySQL(app)

# Secret key declaration
app.secret_key = 'scrtKey'

# HTML pages
@app.route('/')
def Index():
    return render_template('index.html')
@app.route('/Management')
def Management():
    return render_template('management.html')

# Login with a user
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        usernm = request.form['username']
        pssword = request.form['password']
        dbconn = database.connection.cursor()
        dbconn.execute('CREATE TABLE IF NOT EXISTS users(id INT PRIMARY KEY AUTO_INCREMENT, username VARCHAR(15), password VARCHAR(15))')
        dbconn.execute('INSERT IGNORE INTO users VALUES(0, "admin", "admin")')
        dbconn.execute('SELECT * FROM users WHERE username = %s AND password = %s LIMIT 1', [usernm, pssword])
        query = dbconn.fetchall()
        if query:
            return redirect(url_for('Management'))
        else:
            flash('User not found')
            return redirect(url_for('Index'))

# Create a new user
@app.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        usernm = request.form['username']
        pssword = request.form['password']
        dbconn = database.connection.cursor()
        dbconn.execute('INSERT INTO users(username, password) VALUES(%s, %s)', [usernm, pssword])
        database.connection.commit()
        flash('User created')
        return redirect(url_for('Management'))

# Reset user's password
@app.route('/reset', methods=['POST'])
def reset():
    if request.method == 'POST':
        usernm = request.form['username']
        pssword = request.form['password']
        dbconn = database.connection.cursor()
        dbconn.execute('UPDATE users SET password = %s WHERE username = %s', [pssword, usernm])
        database.connection.commit()
        flash('Password updated')
        return redirect(url_for('Management'))

# Delete user
@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        usernm = request.form['username']
        dbconn = database.connection.cursor()
        dbconn.execute('DELETE FROM users WHERE username = %s', [usernm])
        database.connection.commit()
        flash('User deleted')
        return redirect(url_for('Management'))

# List all existing users
@app.route('/list', methods=['POST'])
def list():
    if request.method == 'POST':
        dbconn = database.connection.cursor()
        dbconn.execute('SELECT * FROM users')
        query = dbconn.fetchall()
        if query:
            flash('Users listed')
            return render_template('management.html', users = query)

# Running the service
if __name__ == '__main__':
    app.run(port = 80, debug = True, host='0.0.0.0')