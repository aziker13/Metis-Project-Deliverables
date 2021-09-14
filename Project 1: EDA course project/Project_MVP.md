## New York Subway Turnstile Data Analysis 

The question I've looked to answer with this EDA project has been what subway station our clinet should be sending their survey teams to in order to maximize
their gala attendance.

I started with using data from the MTA website, and used the 13 weeks of most recent data (05/29/21 - 08/27/21) for this analysis. 

![Screenshot from 2021-09-14 09-34-03](https://user-images.githubusercontent.com/87049486/133297915-7571fa9c-f822-4241-8322-df02ca6ac9a4.png)


Using this data, I created a bar graph displaying the stations with the 10 largest totals of entries for the stated time period. Given the results from this plot, Penn St station has seen the most traffic over this time.

I decided to take a closer look at that particular station, to see if there was a day of
the week that sees more traffic than the others


![Screenshot from 2021-09-13 20-24-04](https://user-images.githubusercontent.com/87049486/133190398-85ca1fc3-49ec-4e4d-ab7d-bbefe9523fd7.png)

This is a histogram, with each bin representing a day of the week, and the value on the y-axis being the mean entries for the corresponding day of the week 
at Penn St Station.  It appears that Wednesday has seen the most foot traffic on average during the summer of 2021.

Using this information, my next steps are to see if there is a time of day on Wednesdays that net the most traffic, and look into the demographic data of the neighborhood surrounding this station.
