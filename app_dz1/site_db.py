import os.path
import sqlite3

from flask import Flask, render_template, request, flash, g

from TWO.site_db import SECRET_KEY
from fdatab import FDataB

DATABASE = 'project.db'
DEBUG = True
SECRET_KEY = ''

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(DATABASE=os.path.join(app.root_path, 'project.db'))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'prog_db'):
        g.prog_db = connect_db()
    return g.prog_db


@app.route("/")
def index():
    db = get_db()
    dbase = FDataB(db)
    return render_template('index.html', menu=dbase.get_menu(),
                           posts=dbase.get_post_anonce())


@app.route("/add_post", methods=["POST", "GET"])
def add_post():
    db = get_db()
    dbase = FDataB(db)

