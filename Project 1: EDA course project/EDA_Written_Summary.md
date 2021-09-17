EDA Project Summary: Determining the Best Way to Deploy Survey Teams to Subway Stations

Alika Ziker 

Abstract

*This Analysis centered on the question of what subway station in New York City sees the most foot traffic, 
as determined by the MTA’s own Turnstile data.  Data was pulled into an SQL database, and then brought into the
python environment as a Pandas dataframe. After aggregation, testing, and multiple cleaning processes, 34th street/Penn 
Station was found to be the most used Station, with the busiest times being Wednesday from 16:00–20:00. The conclusion of this 
analysis was that this day, time, and location combination would be optimal for survey teams to get maximum exposure to subway users.
Future analyses would hope to incorporate the size of the station to get a density of people, which may have an impact on the reach of survey teams.*


Design

This project was brought as a request from WTWY International, in an effort to increase the attendance of their summer gala while increase the potential
for donations. The client needed data for the NYC subway system put to work in an effort to more strategically place their survey teams to maximize their 
recruiting to the gala.  From this data, it could be determined what subway station sees the most traffic and thus the most
potential signatures.  This can be further targeted down to the day of the week that this station is most busy, as well as the time of day.  All put 
together, a specific location, time, and day could be delivered for the client as the highest potential of maximizing exposure for their survey teams

Data

Data used for this analysis was acquired from the MTA website in the form of 2.7 million rows of data containing entry and exit information specific to station, control unit, turnstile, plus date and time.  Each station’s entries could be broken down to the individual turnstile

Algorithms

EDA techniques included removing duplicate entries, converting accumulative entries through the year into a daily entries number, and plotting daily entries to look for outliers.  Once daily entries for individual turnstiles were cleaned, turnstile entries were then summed to provide a station total for the day, and then a total for the duration of the data set. Further analysis was done on the highest trafficked station, following a similar methodology of cleaning, identifying outliers, and visualization to confirm trends and completion of cleaning.

Tools

-SQL for providing the database

-SQL Alchemy for transposing the database into python

-Pandas for data manipulation

-Matplotlib and Seaborn for plotting and visualization

Communication

The slides that are presented contain relavent visualization of data and conclusions drawn from that data
