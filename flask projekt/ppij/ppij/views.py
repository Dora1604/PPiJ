"""
Routes and views for the flask application.
"""

from datetime import datetime
from datetime import date
from datetime import timedelta
from urllib import response

from dateutil.utils import today
from flask import render_template
from ppij import app
from flask import Flask, render_template, request, redirect, Response, make_response
import random, json
from datetime import datetime
from pandas import read_csv
from statsmodels.tsa.arima_model import ARIMA
import numpy
import pdfkit

@app.route('/')
def home():
     mapa = {}
     mapa2 = {}
     return render_template(
        'tony.html',
        mapa = mapa,
        mapa2 = mapa2
    )

@app.route('/tony')
def tony():
    return render_template(
        'tony.html'
    )
@app.route('/nesto1',methods=["GET"])
def nesto22():
    mapa = {}
    mapa2 = {}
    return render_template(
        'nesto1.html',
        mapa = mapa,
        mapa2 = mapa2
    )

@app.route('/nesto1' ,methods=['POST'])
def nesto1():
    mapa = {}
    mapa2 = {}
    datum = request.form['datum']
    datumi = datum.split('-')
    datumi[0] = datumi[0].strip()
    datumi[1] = datumi[1].strip()
    durationBetweenDates = find_duration(datumi[0], datumi[1])
    fourthOfJune = "04.06.2020"
    dat1ToFourthOfJune = find_duration(datumi[0], fourthOfJune)
    lista_gradova = ["dubrovnik","gospic","zadar","sibenik","osijek","pula","rijeka","split","varazdin","zagreb"]
    lista_gradova.sort()
    for grad in lista_gradova:
        mapa[grad] = first_option(grad,durationBetweenDates,dat1ToFourthOfJune)   
    return render_template(
        'nesto1.html',
        mapa = mapa,
        mapa2 = mapa2
    )
@app.route('/nesto2',methods=['GET'])
def nesto222():
    mapa = {}
    mapa2 = {}
    return render_template(
        'nesto2.html',
        mapa = mapa,
        mapa2 = mapa2
    )
@app.route('/nesto2',methods=['POST'])
def nesto2():
    mapa2 = {}
    mapa = {}
    city = request.form['city']
    season = request.form['season']
    mapa2 = second_option(city,season)
    mapa2 = reformatiraj_mapu(mapa2,season)
    return render_template(
        'nesto2.html',
        mapa = mapa,
        mapa2 = mapa2
    )

@app.route('/<project>/<location>') #http://127.0.0.1:5555/PPiJ/Zagreb
def pdf_template(project, location):
    rendered = render_template('pdf_template.html', project=project, location=location)
    pdf = pdfkit.from_string(rendered, False)
    resp = make_response(pdf)
    resp.headers['Content-Type'] = 'application/pdf'
    resp.headers['Content-Disposition'] = 'attachment; filename=output.pdf'
    return resp

@app.route('/probaindex', methods=('GET', 'POST'))
def probaindex():
    mapa = {}
    mapa2 = {}
    datum = request.form['datum']
    city = request.form["city"]
    season = request.form["season"]
    if datum != "" and city=="" and season=="":
        datumi = datum.split('-')
        datumi[0] = datumi[0].strip()
        datumi[1] = datumi[1].strip()
        durationBetweenDates = find_duration(datumi[0], datumi[1])
        fourthOfJune = "04.06.2020"
        dat1ToFourthOfJune = find_duration(datumi[0], fourthOfJune)
        lista_gradova = ["dubrovnik","gospic","zadar","sibenik","osijek","pula","rijeka","split","varazdin","zagreb"]
        lista_gradova.sort()
        for grad in lista_gradova:
            mapa[grad] = first_option(grad,durationBetweenDates,dat1ToFourthOfJune)
    if city!="" and season!="" and datum=="":
        mapa2 = second_option(city,season)
        mapa2 = reformatiraj_mapu(mapa2,season)
       
    return render_template(
        'probaindex.html',
         mapa = mapa,
         mapa2 = mapa2
    )
def reformatiraj_mapu(mapa,season):
    novamapa = {}
    #novamapa = {"JANUARY":{},"FEBRUARY":{},"MARCH":{},"APRIL":{},"MAY":{},"JUNE":{},"JULY":{},"AUGUST":{},"SEPTEMBER":{},"OCTOBER":{},"NOVEMBER":{},"DECEMBER":{}}
    if season == "spring":
        s_list = ["MARCH","APRIL","MAY","JUNE"]
    elif season == "summer":
        s_list = ["JUNE","JULY","AUGUST","SEPTEMBER"]
    elif season == "autumn":
        s_list = ["SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER"]
    else:
        s_list = ["DECEMBER","JANUARY","FEBRUARY","MARCH"]
    counter = 1
    sec_counter = 1

    for key in mapa:
        if key in s_list:
            novamapa[key] = mapa[key]
    return novamapa


def first_option(dataset,days,difference1):
    openfile = "/Users/ancip/Desktop/dataset/{}.csv".format(dataset)        
    series = read_csv(openfile, header=None)
    series.dropna(inplace=True)
    # seasonal difference
    X = series.values
    days_in_year = 365
    differenced = difference(X, days_in_year)
    # fit model
    model = ARIMA(differenced, order=(7,0,1))
    model_fit = model.fit(disp=0)
    # multi-step out-of-sample forecast
    start_index = len(differenced)
    end_index = start_index + days + difference1
    start_index = start_index 
    forecast = model_fit.predict(start=start_index, end=end_index)
    # invert the differenced forecast to something usable
    history = [x for x in X]
    day = 1
    sum = 0
    num_of_days = 0
    mapa = {}
    counter = 1
    for yhat in forecast:
        inverted = inverse_difference(history, yhat, days_in_year)
        if counter > difference1-1:
            sum += inverted
            num_of_days += 1
        history.append(inverted)
        day += 1
        counter +=1
    avg = sum/num_of_days
    return avg
def second_option(dataset,season):
    openfile = "/Users/ancip/Desktop/dataset/{}.csv".format(dataset)  
    curr_year = str(today())[:4]
    ljeto = datetime.strptime("21.06.{}".format(curr_year),'%d.%m.%Y').date()
    proljece =  datetime.strptime("21.03.{}".format(curr_year),'%d.%m.%Y').date()
    jesen = datetime.strptime("23.09.{}".format(curr_year),'%d.%m.%Y').date()
    zima =  datetime.strptime("21.12.{}".format(curr_year),'%d.%m.%Y').date()
    curr_date = date.today()
    if season == "summer":
        diff = (curr_date - ljeto).days
        if diff < 0:
            year = curr_year
        else:
            year = str(int(curr_year)+1)
        ljeto = datetime.strptime("21.06.{}".format(year),'%d.%m.%Y').date()
        razlika = abs(datetime.strptime("04.06.{}".format(curr_year),'%d.%m.%Y').date() - ljeto).days
        days_of_season = 92
    elif season == "autumn":
        diff = (curr_date - jesen).days
        if diff < 0:
            year = curr_year
        else:
            year = str(int(curr_year)+1)
        jesen = datetime.strptime("23.09.{}".format(year),'%d.%m.%Y').date()
        razlika = abs(datetime.strptime("04.06.{}".format(curr_year),'%d.%m.%Y').date() - jesen).days
        days_of_season = 87
    elif season == "spring":
        diff = (curr_date - proljece).days
        if diff < 0:
            year = curr_year
        else:
            year = str(int(curr_year)+1)
        proljece = datetime.strptime("21.03.{}".format(year),'%d.%m.%Y').date()
        razlika = abs(datetime.strptime("04.06.{}".format(curr_year),'%d.%m.%Y').date() - proljece).days
        days_of_season = 90
    else:
        diff = (curr_date - zima).days
        if diff < 0:
            year = curr_year
        else:
            year = str(int(curr_year)+1)
        zima = datetime.strptime("21.12.{}".format(year),'%d.%m.%Y').date()
        razlika = abs(datetime.strptime("04.06.{}".format(curr_year),'%d.%m.%Y').date() - zima).days
        days_of_season = 88   
    series = read_csv(openfile, header=None)
    series.dropna(inplace=True)
    # seasonal difference
    X = series.values
    days_in_year = 365
    differenced = difference(X, days_in_year)
    # fit model
    model = ARIMA(differenced, order=(7,0,1))
    model_fit = model.fit(disp=0)
    # multi-step out-of-sample forecast
    start_index = len(differenced)
    end_index = start_index + razlika + days_of_season
    forecast = model_fit.predict(start=start_index, end=end_index)
    # invert the differenced forecast to something usable
    history = [x for x in X]
    fourth_of_june = datetime.strptime("04.06.{}".format(year),'%d.%m.%Y').date()
    day = 1
    counter = 1
    mapa = {"JANUARY":{},"FEBRUARY":{},"MARCH":{},"APRIL":{},"MAY":{},"JUNE":{},"JULY":{},"AUGUST":{},"SEPTEMBER":{},"OCTOBER":{},"NOVEMBER":{},"DECEMBER":{}}
    for yhat in forecast:
        inverted = inverse_difference(history, yhat, days_in_year)
        if counter > razlika-1:
            datum = fourth_of_june + timedelta(days=day)
            key = pretvori(datum.month)
            mapa[key][str(datum)] = inverted
            #print('Day %d: %f' % (day, inverted))
        history.append(inverted)
        counter+=1
        day += 1
    return mapa
def pretvori(mjesec):
    if mjesec==1:
        return "JANUARY"
    elif mjesec==2:
        return "FEBRUARY"
    elif mjesec==3:
        return "MARCH"
    elif mjesec==4:
        return "APRIL"
    elif mjesec==5:
        return "MAY"
    elif mjesec==6:
        return "JUNE"
    elif mjesec==7:
        return "JULY"
    elif mjesec==8:
        return "AUGUST"
    elif mjesec==9:
        return "SEPTEMBER"
    elif mjesec==10:
        return "OCTOBER"
    elif mjesec==11:
        return "NOVEMBER"
    else:
        return "DECEMBER"

def difference(dataset, interval=1):
	diff = list()
	for i in range(interval, len(dataset)):
		if i-interval != 0:
			value = float(dataset[i]) - float(dataset[i - interval])
			diff.append(value)
	return numpy.array(diff)

# invert differenced value
def inverse_difference(history, yhat, interval=1):
	return float(yhat) + float(history[-interval])

def find_duration(dat1, dat2):
    date1 = datetime.strptime(dat1, '%d.%m.%Y').date()
    date2 = datetime.strptime(dat2, '%d.%m.%Y').date()
    return abs((date2 - date1).days)+1




