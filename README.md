# sqlalchemy-challenge
Surfs up homework


## Background

Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you need to do some climate analysis on the area. The following outlines what you need to do.

## Step 1 - Climate Analysis and Exploration
To begin, use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* Use the provided starter notebook and hawaii.sqlite files to complete your climate analysis and data exploration.
<br><br>
* Choose a start date and end date for your trip. Make sure that your vacation range is approximately 3-15 days total.
<br><br>
* Use SQLAlchemy create_engine to connect to your sqlite database.
<br><br>
* Use SQLAlchemy automap_base() to reflect your tables into classes and save a reference to those classes called Station and Measurement.
<br><br>

**_SQLAlchemy ORM Tables_**
<br><br>
![Summary](https://github.com/KGore12/sqlalchemy-challenge/blob/main/images/SQLAlchemy_ORM_tables.png)
<br><br>
<br><br>

**_Precipitation Analysis_**
<br><br>
![Summary](https://github.com/KGore12/sqlalchemy-challenge/blob/main/images/precipitation_analysis.png)
<br><br>
<br><br>

**_Min, Max, Avg Temperatures_**
<br><br>
![Summary](https://github.com/KGore12/sqlalchemy-challenge/blob/main/images/min_max_avg_temp.png)
<br><br>
<br><br>

**_Climate Analysis_**
<br><br>
![Summary](https://github.com/KGore12/sqlalchemy-challenge/blob/main/images/climate_analysis.png)
<br><br>
<br><br>

**_Last 12 Months of Temperatures for Station USC00519281**
<br><br>
![Summary](https://github.com/KGore12/sqlalchemy-challenge/blob/main/images/temp_station_USC00519281.png)
<br><br>
<br><br>

## Step 2 - Climate App
Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.

**_Example of app.py route**
<br><br>
![Summary](https://github.com/KGore12/sqlalchemy-challenge/blob/main/images/app-py_route-start&end_dates.png)
<br><br>
### Routes
* `/`

  * Home page.

  * List all routes that are available.

* `/api/v1.0/precipitation`

  * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.

  * Return the JSON representation of your dictionary.

* `/api/v1.0/stations`

  * Return a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * Query the dates and temperature observations of the most active station for the last year of data.
  
  * Return a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.
