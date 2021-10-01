EDA Project Summary: Determining the Best Way to Deploy Survey Teams to Subway Stations

Alika Ziker

Abstract

The guiding question for this Linear Regression project was what makes a soccer player valuable on the transfer market and can we identify key statistics that
would allow for accuracte predictions of a players worth.  Using estimated transfer values from the web as our target, along with performance statistics specific and
characteristics as our features, player data was scraped from the web.  Because of the lack of a universal performance metric, I split the data into data for strikers and
forwards, and data for midfielders, and made seperate models for each postion on the pitch.  Due to the fact that data is heavily skewed towards average performing soccer
players (left-skew), and the fact that there cannot be a negative value for an athlete, linear regression was not the best fitting model and did not provide a high R2 or MAE. However,
Through Lasso and Ridge regression key features were identified for both forwards and midfielders. In conclusion the data provided some insight into what may make players of a 
certain position value, but failed to accurately predict their value, likely due to the small sample size as well as viloation of 2 assumptions of linear regresson.  Future
studies should look to add more features that create a more wholistic picture of a players contribution to the field, while also utilizing an WSL model to better fit the skewed data.

Design

The economy of world soccer is massive, with clubs from the top five leagues in europe's spending over 3.5 billion dollars in the summer of 2021 on new players.  Accurately
projecting a players value on the transfer market, along with identifying key characteristics that have a large impact on their value, would be of interest to soccer managers,
directors of sport, owners, and fans alike.  Being able to buy or sell players for a good price is something that keeps the finances of the club improving, helping to lead
to performance on the pitch. While still relatively new to analytics, data exists on the shooting, passing, and defending for players in Europe's top leagues.  Using these stats as features,
and the players value as the target, a model will be made to try and represent the relationships that exist.

Data

Data used for this analysis was acquired from 2 places, https://www.transfermarkt.us provided the player's estimated transfer value and was scraped using selenium,
Data for player statistics was provided by https://fbref.com/en in the form of CSV files

Algorithms

EDA techniques included ensuring no NaN values were present, and that the statics of the player were merged onto the correct transfer value.  Initial linear modeling was done prior to any further enhancement
to provide a baseline.  After that was established, data was standardized so that lasso and ridge regression could be done to help evaluate for important features and co-linearity.
Once that had taken place, terms that appeared to need polynomial terms were given, and others were boxcoxed to accomidate skew.  In the end, a cobination of R2, MAE, and model bias/variance
was used to determine the best model avaiable



Tools

-Selenium and Beautiful Soup for webscraping

-Pandas for data manipulation

-sklearn and statsmodels.api for fitting and modeling

-Matplotlib and Seaborn for plotting and visualization

Communication

The slides that are presented contain relavent visualization of data and conclusions drawn from that data
