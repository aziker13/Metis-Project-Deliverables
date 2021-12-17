# Abstract:

For the project, the goal was to attempt to build an end-to-end coffee shop recommendation system for the Seattle area and accept user input. 
The start of this project involved the creation of a web scraper that would scape reviews from yelp and store them into a mongoDB.  After this was completed, 
the data was queried from mongo DB into Pandas where data was cleaned for NLP and vectorization.  Topic modelling was done with NMF and a recommendation system was created.
This model, vectorizer, and dataframe were saved locally and written into a .py file for production on streamlit. In the end data was successfully scraped and saved to mongo, 
while the model worked on the steam lit webapp and provided users with recommendations based on their own keywords.

## Design:

The idea for this project came from a desire to build on a recommendation model previously built to recommend coffee shops on yelp. 
The question that was posed was could this model be fed data scraped from the web specific to Seattle, and then brought to production where users could
access the model and data in order to get their own recommendations for local coffee shops.  A successful recommender could help people both local and visiting find
a coffee shop to fit their liking more specifically than just a star rating could provide,

## Data:

Data for this project was scraped from yelp via a web scraping program written specifically for this project.  Data was scraped and stored into a MongoDB hosted locally,
where it could be pulled into python and then pandas for NLP.  Each document contains the name of the coffee shop and the text from a single review on yelp.  As of writing,
the dataset totals over 6000 reviews across 10 coffee shops.

## Algorithms:

For this project, review text was cleaned and tokenized using a combination of regex and spacy.  These tokens were then vectorized and used for topic 
modeling via scikit-learn packages. Unsupervised learning was used in tandem with word vectorization and NMF modeling to create a recommendation system
that can suggest a coffee shop based on user input of a keyword such as “latte” or “iced coffee”.

## Tools:

-selenium and beautiful soup for data acquisition

-mongoDB for data storage

-pandas, regex, and spacy for data cleaning and processing

-scikit-learn for machine learning

-streamlit for model deployment

## Communication

The slides that are presented contain relevant visualization of data and conclusions drawn form that data
