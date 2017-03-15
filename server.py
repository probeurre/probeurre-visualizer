#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This file is part of Probeurre.
"""
from flask import Flask, render_template, request, current_app

app = Flask(__name__)

global repos

# Routes

@app.route("/")
def root():
    return render_template("layout.html", contentTemplate="repos.html", repos=app.config['REPOS'])

@app.errorhandler(403)
def unauthorized(e):
    return render_template("layout.html", content="Error 403"), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template("layout.html", content="Error 404"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("layout.html", content="Error 500"), 500

def run(ip="127.0.0.1", port=5555, downloaded=[], db_host='localhost', db_user='uxie', db_pass='uxie'):
    app.config['DB_HOST'] = db_host
    app.config['DB_USER'] = db_user
    app.config['DB_PASS'] = db_pass
    app.config['REPOS'] = downloaded

    # connection = MySQL(db_host, db_user, db_pass, 'uxie')
    # connection.connect()

    app.run(host=ip, port=port)
