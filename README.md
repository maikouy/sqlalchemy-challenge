# sqlalchemy-challenge

Vacation time! Trip to Honolulu, Hawaii! In order to start planning, we must know the climate there. Thus, we will use SQLAlchemy ORM queries, Pandas, and Matplotli to analyze the climate database.

Step 1: 
Percipitation Analysis:

-Start by finding the most recent date in the data set.
-Using this date, retrieve the last 12 months of precipitation data by querying the 12 preceding months of data.
-Select only the date and prcp values.
-Load the query results into a Pandas DataFrame and set the index to the date column.
-Sort the DataFrame values by date.
-Plot the results using the DataFrame plot method.
-Use Pandas to print the summary statistics for the precipitation data.


Station Analysis

-Design a query to calculate the total number of stations in the dataset.
-Design a query to find the most active stations (i.e. which stations have the most rows?).
-List the stations and observation counts in descending order.
-Which station id has the highest number of observations?
-Using the most active station id, calculate the lowest, highest, and average temperature.
-Design a query to retrieve the last 12 months of temperature observation data (TOBS).
-Filter by the station with the highest number of observations.
-Query the last 12 months of temperature observation data for this station.
-Plot the results as a histogram.


Step 2: 
Climate App

-Use Flask to create routes:
-/api/v1.0/precipitation
----Convert the query results to a dictionary using date as the key and prcp as the value.
----Return the JSON representation of your dictionary.
-/api/v1.0/stations
----Return a JSON list of stations from the dataset.
/api/v1.0/tobs
----Query the dates and temperature observations of the most active station for the last year of data.
----Return a JSON list of temperature observations (TOBS) for the previous year.
-/api/v1.0/<start>
----Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a start date
----Calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
-/api/v1.0/<start>/<end>
----Return a JSON list of the minimum temperature, the average temperature, and the max temperature for an end date.
----Calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
