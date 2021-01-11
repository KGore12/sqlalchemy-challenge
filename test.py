

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    session.close()
    
    # Perform a query to retrieve the data and temp scores
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= year_ago).\
            filter(Measurement.station == "USC00519281").all()
    session.close()

    # Convert list of tuples into normal list
    temperature_list = list(np.ravel(results))

    return jsonify(temperature_list)