"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from ppij import app
from flask import Flask, render_template, request, redirect, Response
import random, json 
from datetime import datetime

@app.route('/')
def home():
     return render_template(
        'probaindex.html',
    )

@app.route('/probaindex', methods=('GET', 'POST'))
def probaindex():
     datum = request.form['datum']
     datumi = datum.split('-')
     datumi[0] = datumi[0].strip()
     datumi[1] = datumi[1].strip()
     durationBetweenDates = find_duration(datumi[0], datumi[1])
     fourthOfJune = "04.06.2020"
     dat1ToFourthOfJune = find_duration(datumi[0], fourthOfJune)
     map = {'zagreb': 11.4, 'osijek': 11.4, 'pula': 11.4, 'split': 11.4, 'dubrovnik': 11.4, 'zadar': 11.4, 'rijeka': 11.4, 'sibenik': 11.4, 'varazdin': 11.4}
     return render_template(
        'probaindex.html',
    )

def find_duration(dat1, dat2):
    date1 = datetime.strptime(dat1, '%d.%m.%Y').date()
    date2 = datetime.strptime(dat2, '%d.%m.%Y').date()
    return abs((date2 - date1).days)+1




