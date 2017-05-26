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
    return render_template("layout.html", contentTemplate="repos.html",
                           analyzed=app.config['ANALYZED'],
                           extracted=app.config['EXTRACTED'],
                           nbAnalyzed=app.config['NBANALYZED'],
                           nbExtracted=app.config['NBEXTRACTED'])

@app.route("/dlAnalyzed")
def dlAnalyzed():
    return send_from_directory('static', 'analyzed.json')

@app.route("/dlExtracted")
def dlExtracted():
    return send_from_directory('static', 'extracted.json')

@app.errorhandler(403)
def unauthorized(e):
    return render_template("layout.html", content="Error 403"), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template("layout.html", content="Error 404"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("layout.html", content="Error 500"), 500

def run(ip="127.0.0.1", port=5555, analyzed={}, extracted={}, nbAnalyzed=0, nbExtracted=0):
    app.config['ANALYZED'] = analyzed
    app.config['EXTRACTED'] = extracted
    app.config['NBANALYZED'] = nbAnalyzed
    app.config['NBEXTRACTED'] = nbExtracted
    app.run(host=ip, port=port)
