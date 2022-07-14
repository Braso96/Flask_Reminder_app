from flask import Flask, render_template, redirect, request
import sqlite3

app = Flask(__name__)

# connection to the database and return of an html tamplate
@app.route('/') # URL
def index():
    connection = sqlite3.connect('database.db') # connect to database
    connection.row_factory = sqlite3.Row # database connection organized in rows
    posts = connection.execute('SELECT * FROM posts').fetchall() # all lines will be organized in a list
    connection.close()
    return render_template('index.html', posts=posts)

@app.route('/<int:idx>/delete', methods=('POST',)) # URL
def delete(idx):
    connection = sqlite3.connect('database.db')  # connect to database
    connection.row_factory = sqlite3.Row  # database connection organized in rows
    connection.execute(f'DELETE FROM posts WHERE id = ?', (idx,))
    connection.commit()
    connection.close()
    return redirect('/') # after having performed the delete, it automatically returns to the updated main page

# handles post requests
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        info = request.form['info']
        connection = sqlite3.connect('database.db')  # connect to database
        connection.row_factory = sqlite3.Row  # database connection organized in rows
        connection.execute(
            'INSERT INTO posts (title, info) VALUES (?, ?)',
            (title, info)
        )
        connection.commit()
        connection.close()
        return redirect('/')
    return render_template('create.html')

