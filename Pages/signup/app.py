# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'kanpur'
app.config['MYSQL_DB'] = 'project'

mysql = MySQL(app)

@app.route('/')
def SighnUp():
    return render_template('SighnUp.html')

@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        email = request.form['email']
        name = request.form['name']
        password = request.form['password']


        # Create a cursor
        cur = mysql.connection.cursor()

        # Execute query to insert data
        cur.execute("INSERT INTO users (username,name, email, password) VALUES (%s, %s, %s, %s)", (username,name, email, password))

        # Commit to database
        mysql.connection.commit()

        # Close connection
        cur.close()

        return redirect(url_for('home'))

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
