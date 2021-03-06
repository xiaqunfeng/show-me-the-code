# encoding: utf-8
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import time

app = Flask(__name__)


class Config(object):
    DEBUG = True
    USERNAME='admin'
    PASSWORD='1234'
    DATABASE='/tmp/flaskr.db'
    DATABASE_URI = 'sqlite://:memory:'
    SECRET_KEY='shdjkandscbowduAIJNnjas9aSKAJSka'

app.config.from_object(Config)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_db()
    return db

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
    g.db.close()

@app.template_filter('format_time')
def format_time_filter(t):
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(t))

@app.route('/')
def show_entries():
    cur = g.db.execute('select title, text, created_at from entries order by id desc')
    entries = [dict(title=row[0], text=row[1], created_at=row[2]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text, created_at) values (?, ?, ?)',
                 [request.form['title'], request.form['text'], time.time()])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

if __name__ == '__main__':
    init_db()
    app.run()
    #app.run(debug=True)
