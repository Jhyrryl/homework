import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# ================================= #

engine = create_engine("sqlite:///Resources/hawaii.sqlite", echo=False)

Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station

# ================================= #

app = Flask(__name__)

@app.route("/")
def home():
    return (
        f""
        f""
        f""
        f""
        f""
        f""
    )

@app.route("/api/v1.0/precipitation")
def precipitation_v1_0():
    session = Session(engine)

@app.route("/api/v1.0/stations")
def stations_v1_0():
    session = Session(engine)

@app.route("/api/v1.0/tobs")
def tobs_v1_0():
    session = Session(engine)

@app.route("/api/v1.0/<start>")
def start_v1_0():
    session = Session(engine)

@app.route("/api/v1.0/<start>/<end>")
def start_end_v1_0():
    session = Session(engine)
