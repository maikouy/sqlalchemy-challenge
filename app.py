import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify

start_date = ['2016-07-04']
end_date = ['2016-07-31']

#Database Setup
engine = create_engine("sqlite:///Resources/Hawaii.sqlite")


#Reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

#Save reference to the table
Base.classes.keys()
Measurement = Base.classes.measurement
Station = Base.classes.station

#Create our session (link) from Python to the DB
session = Session(engine)

#Collect the names of columns with inspector
inspector = inspect(engine)
inspector.get_table_names()


#Flask Setup
app = Flask(__name__)


#Flask Routes:
# Index Route (Always first page)
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/startend<br/>"
    )

#Percipitation route page:

@app.route("/api/v1.0/precipitation")
def precipitation():
    #Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of precipitation"""
    #Query all Percipitation
    results = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    #Create a dictionary from the row data and append to a list of all_Percipitation
    all_measurements = []
    for date, prcp in results:
        measurement_dict = {}
        measurement_dict["date"] = date
        measurement_dict["prcp"] = prcp
        all_measurements.append(measurement_dict)
    
    return jsonify(all_measurements)


#Stations route page:

@app.route("/api/v1.0/stations")
def stations():
    #Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of stations and names"""
    #Query all passengers
    results = session.query(Station.station, Station.name).all()

    session.close()

    #Convert list of tuples into normal list
    stations_list = list(np.ravel(results))

    return jsonify(stations_list)


#Tobs route page:

@app.route("/api/v1.0/tobs")
def tobs():
    #Create our session (link) from Python to the DB
    session = Session(engine)

    """"Return a list of dates and temperatures of the most active station"""
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= "2016-08-23").filter(Measurement.station == "USC00519281").order_by(Measurement.date).all()
    
    session.close()

     #Convert list of tuples into normal list
    tobs_list = list(np.ravel(results))

    return jsonify(tobs_list)


#Start date(start) route page:

@app.route("/api/v1.0/start")
def beginning_date():

    #Create our session (link) from Python to the DB
    session = Session(engine)

    """"Return a list of min, avg, max temp for random start date for all dates greater than & equal to start date"""
    sel = [Measurement.date, func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]

    results = session.query(*sel).filter(Measurement.date >= "2016-07-04").group_by(Measurement.date).all()

    session.close()

    #Create a dictionary from the row data and append to a list the start date with min, max, avg
    all_dates = []
    for date, min, max, avg in results:
        date_dict = {}
        date_dict["date"] = date
        date_dict["min"] = min
        date_dict["max"] = max
        date_dict["avg"] =avg
        all_dates.append(date_dict)

    return jsonify(all_dates)


#Start date(startend) route page:

@app.route("/api/v1.0/startend")
def ending_date():

    #Create our session (link) from Python to the DB
    session = Session(engine)

    """"Return a list of min, avg, max temp for random start date for all dates between start and end date"""
    sel = [Measurement.date, func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]

    results = session.query(*sel).filter(Measurement.date >= "2016-07-04", Measurement.date <= "2016-07-31").group_by(Measurement.date).all()

    session.close()

    #Create a dictionary from the row data and append to a list the start date - end date with min, max, avg
    all_dates = []
    for date, min, max, avg in results:
        date_dict = {}
        date_dict["date"] = date
        date_dict["min"] = min
        date_dict["max"] = max
        date_dict["avg"] =avg
        all_dates.append(date_dict)

    return jsonify(all_dates)

# The last piece
if __name__ == "__main__":
    app.run(debug=True)