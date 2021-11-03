## Project Proposal

The purpose of this project is to use written reviews posted on Yelp of various coffee shops to build a recommendation model for users based on what attributes
they seek in a coffee shops.  Coffee enthusiasts, people who want a place to meet friends, and those who want a quiet place to work would all benefit from
knowing which coffee shops would fit their needs the best.

The dataset I am using is a collection of ~7000 written coffee shop reviews on yelp, with each row of data containing the name of the coffee shop, the users written
review of the coffee shop, and the user's rating of the shop out of 5 stars. I will look to model and cluster topics such as the type of atmosphere, and the kind of
coffee the shop serves.  

I wil be using a combination of scikit-learn, nltk, and spaCy to pre-process these documents. I will also be using visualization tools such as matplotlib and seaborn.

An minimum viable product for this project would be to create topic vectors via topic modeling and identify key topics within this dataset that could be used for 
further EDA and clustering.
