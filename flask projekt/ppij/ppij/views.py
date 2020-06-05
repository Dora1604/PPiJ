"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from ppij import app
from flask import Flask, render_template, request, redirect, Response
import random, json 

@app.route('/')
def home():
    """Renders the home page."""
    return render_template(
        'probaindex.html',
        title='Home Page',
        year=datetime.now().year,
        #name = tony.istina()
    )


@app.route('/handle_data', methods=('GET', 'POST'))
def handle_data():
    tony3 = request.form['tony']
    tonyNovi = tony3 + "je lijep"
    tony4 = analiziraj(tonyNovi)
    return tony4
def analiziraj(tonyNovi):
    t = tonyNovi+"da"
    return t