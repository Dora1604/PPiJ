"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from ppij import app
from flask import Flask, render_template, request, redirect, Response
import random, json 

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'probaindex.html',
        title='Home Page',
        year=datetime.now().year,
        #name = tony.istina()
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/proba')
def proba():
    """Renders the contact page."""
    return render_template(
        'proba.html',
        title='Proba',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/novi')
def novi():
    """Renders the contact page."""
    return render_template(
        'noviindex.html',
        title='Index',
        year=datetime.now().year,
        message='Your contact page.'
    )


@app.route('/opcija1')
def opcija1():
    """Renders the contact page."""
    return render_template(
        'opcija1.html',
        title='Index',
        year=datetime.now().year,
        message='Your contact page.'
    )


@app.route('/opcija2')
def opcija2():
    """Renders the contact page."""
    return render_template(
        'opcija2.html',
        title='Index',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/probaindex')
def probaindex():
    """Renders the contact page."""
    return render_template(
        'probaindex.html',
        title='Index',
        year=datetime.now().year,
        message='Your contact page.'
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