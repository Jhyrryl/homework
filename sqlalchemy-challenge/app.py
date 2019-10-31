import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime as dt
import json

# ================================= #

engine = create_engine("sqlite:///Resources/hawaii.sqlite", echo=False)

Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station

# ================================= #

app = Flask(__name__)

# ================================= #

@app.route("/")
def home():
    return (
        "<h1>Available API Routes:</h1>"
        "<a href='/api/v1.0/precipitation' target='_blank'>/api/v1.0/precipitation</a><br/>"
        "<a href='/api/v1.0/stations' target='_blank'>/api/v1.0/stations</a><br/>"
        "<a href='/api/v1.0/tobs' target='_blank'>/api/v1.0/tobs</a><br/>"
        "/api/v1.0/&lt;start&gt; (e.g., <a href='/api/v1.0/2016-08-23' target='_blank'>/api/v1.0/2016-08-23</a>)<br/>"
        "/api/v1.0/&lt;start&gt;/&lt;end&gt; (e.g., <a href='/api/v1.0/2011-01-01/2011-12-31' target='_blank'>/api/v1.0/2011-01-01/2011-12-31</a>)"
    )

# ================================= #

@app.route("/api/v1.0/precipitation")
def precipitation_v1_0():
    session = Session(engine)

    ts = session.query(Measurement.date).order_by(Measurement.date.desc()).first()

    most_recent = dt.datetime.strptime(ts[0],'%Y-%m-%d').date()
    year_previous = most_recent - dt.timedelta(365)
    start_date = year_previous.strftime('%Y-%m-%d')
    precip_data = session.query(Measurement.date, Measurement.prcp).\
                    filter(Measurement.date >= start_date).\
                    order_by(Measurement.date).\
                    all()
    return jsonify({tpl[0]:tpl[1] for tpl in precip_data})

# ================================= #

@app.route("/api/v1.0/stations")
def stations_v1_0():
    session = Session(engine)
    stations = session.query(Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation).all()
    return jsonify([{tpl[0]:{'name':tpl[1], 'loc':{'lat':tpl[2], 'lng':tpl[3]}, 'elev':tpl[4]}} for tpl in stations])

# ================================= #

@app.route("/api/v1.0/tobs")
def tobs_v1_0():
    session = Session(engine)

    ts = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    most_recent = dt.datetime.strptime(ts[0],'%Y-%m-%d').date()
    start_date = most_recent - dt.timedelta(365)
    tobs_data = session.query(Measurement.station, Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= start_date).\
        order_by(Measurement.station, Measurement.date).\
        all()
    return jsonify([{'station': tpl[0], 'date': tpl[1], 'tobs': tpl[2]} for tpl in tobs_data])

# ================================= #

def getTemperatureData(start, end=None):
    session = Session(engine)

    start_date = dt.datetime.strptime(start,'%Y-%m-%d').date()

    end_date = None
    if end == None:
        ts = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
        end_date = dt.datetime.strptime(ts[0],'%Y-%m-%d').date()
    else:
        end_date = dt.datetime.strptime(end,'%Y-%m-%d').date()

    min_temp_data = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= start_date, Measurement.date <= end_date).\
        order_by(Measurement.date).\
        group_by(Measurement.date).\
        having(func.min(Measurement.tobs)).\
        all()

    avg_temp_data = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= start_date, Measurement.date <= end_date).\
        order_by(Measurement.date).\
        group_by(Measurement.date).\
        having(func.avg(Measurement.tobs)).\
        all()

    max_temp_data = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= start_date, Measurement.date <= end_date).\
        order_by(Measurement.date).\
        group_by(Measurement.date).\
        having(func.max(Measurement.tobs)).\
        all()

    temp_data = tuple(zip(min_temp_data, avg_temp_data, max_temp_data))

    temps = [{'date': tpl[0][0], 'temps': {'min':tpl[0][1], 'avg':tpl[1][1], 'max':tpl[2][1]}} for tpl in temp_data]    
    return jsonify(temps)

# ================================= #

@app.route("/api/v1.0/<start>")
def start_v1_0(start):
    return getTemperatureData(start)

# ================================= #

@app.route("/api/v1.0/<start>/<end>")
def start_end_v1_0(start, end):
    return getTemperatureData(start, end)

# ================================= #

if __name__ == "__main__":
    app.run(debug=True)
