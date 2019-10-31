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
        "<a href='/api/v1.0/precipitation' target='_blank'>/api/v1.0/precipitation</a><br/>"
        "<a href='/api/v1.0/stations' target='_blank'>/api/v1.0/stations</a><br/>"
        "<a href='/api/v1.0/tobs' target='_blank'>/api/v1.0/tobs</a><br/>"
        "/api/v1.0/&lt;start&gt; (e.g., <a href='/api/v1.0/2016-08-23' target='_blank'>/api/v1.0/2016-08-23</a>)<br/>"
        "/api/v1.0/&lt;start&gt;/&lt;end&gt; (e.g., <a href='/api/v1.0/2016-08-23/2017-08-23' target='_blank'>/api/v1.0/2016-08-23/2017-08-23</a>)"
    )


# @app.route("/api/v1.0/precipitation")
# def precipitation_v1_0():
#     session = Session(engine)

# @app.route("/api/v1.0/stations")
# def stations_v1_0():
#     session = Session(engine)

# @app.route("/api/v1.0/tobs")
# def tobs_v1_0():
#     session = Session(engine)

# @app.route("/api/v1.0/<start>")
# def start_v1_0():
#     session = Session(engine)

# @app.route("/api/v1.0/<start>/<end>")
# def start_end_v1_0():
#     session = Session(engine)

if __name__ == "__main__":
    app.run(debug=True)