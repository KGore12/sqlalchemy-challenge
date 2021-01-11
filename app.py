# Import Flask
from flask import Flask

# Import any dependencies and setup
import numpy as np
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


#################################
# Database Setup
#################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station




#################################
# Flask Setup/Create an app
#################################
app = Flask(__name__)




#################################
# Flask Routes
#################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to the SQL-Alchemy APP API!<br/>"
        f"<br/>"
        f"Available Routes:<br/>"
        f"<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"<br/>"
        f"/api/v1.0/stations<br/>"
        f"<br/>"
        f"/api/v1.0/tobs<br/>"
        f"<br/>"
        f"/api/v1.0/[start_date format:yyyy-mm-dd]<br/>"
        f"<br/>"
        f"/api/v1.0/[start_date format:yyyy-mm-dd]/[end_date format:yyyy-mm-dd]<br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all Precipitation Data"""
    # Query all Precipitation
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= "2016-08-24").\
        all()

    session.close()

    # Convert the query results to a dictionary using date as the key and prcp as the value.
    all_precipitation = []
    for date,prcp  in results:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = prcp
               
        all_precipitation.append(precipitation_dict)

    return jsonify(all_precipitation)




if __name__ == "__main__":
    app.run(debug=True)
