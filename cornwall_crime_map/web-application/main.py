#!/usr/bin/env python
from flask import Flask, render_template, flash, request
import logging, io, base64, os, datetime
from datetime import timedelta

# global variables
crime_horizon_df = None

app = Flask(__name__)

def LoadCrimeHorizon():
    from numpy import genfromtxt
    crime_horizon_df = genfromtxt(src, delimiter=',', names = True, dtype = None,)
    return crime_horizon_df


def GetCrimeEstimates(horizon_date):
    Month_of_year = horizon_date
    crime_horizon_df_tmp = crime_horizon_df[(crime_horizon_df['Month']==Month_of_year)]
    
    # build latlng string for google maps
    LatLngString = ''
    for lat, lon in zip(crime_horizon_df_tmp['Latitude'], crime_horizon_df_tmp['Longitude']): 
        LatLngString += "new google.maps.LatLng(" + str(lat) + "," + str(lon) + "),"
     
    return (LatLngString)


@app.before_first_request
def startup():
    global crime_horizon_df
     # prepare crime data
    crime_horizon_df = LoadCrimeHorizon()


@app.route("/", methods=['POST', 'GET'])
def build_page():

    if request.method == 'POST':
        horizon_date_int = int(request.form.get('slider_crime_horizon'))
        date_int = int(horizon_date_int)

        return render_template('index.html',
            date_horizon = date_int,
            crime_horizon = GetCrimeEstimates(date_int),
            current_value=date_int)

    else:
        # set default crime settings
        return render_template('index.html',
            date_horizon = 1,
            crime_horizon = '',
            current_value=1)

 
if __name__=='__main__':
    # when running on local machine override with local directory path
    src = 'static//devon_cornwall_crime_horizon.csv'
    app.run(debug=True)


