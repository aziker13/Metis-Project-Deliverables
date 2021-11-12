## Abstract:

The goal of this project was to take text reviews from yelp regarding coffee shops in Austin, 
TX, and create a content-based recommendation system.  Yelp review data was previously compiled 
on Kaggle and the dataset contained ~7600 reviews along with the name of the shop being reviewed and
a star rating.  Text per-processing and vectorization was optimized for topic modeling via NMF.
document/topic scores were then aggregated to create a coffee shop/topic matrix, which was then used 
for the recommendation system. The system successfully provided coffee shop recommendations, as well as 
the shop’s yelp average star rating, when given a keyword to search on. 

## Design:

The motivation for this project comes from a desire to be able to recommend a coffee shop based on what
a user is interested. With less companies requiring employees to be in the office, coffee shops are quickly 
becoming very popular places to work, in addition to their usual appeal as a place to get a hot drink or a
meeting place.  Being able to harness machine learning and data science to recommend a shop to fit any one 
of those desires is something that could prove valuable, and a successful model could be applied to recommending 
other types of food and beverage places as well.

## Data:

Data for this project was acquired from a Kaggle dataset called “Yelp Coffee Reviews.” The data contains 
7616 text reviews originating from yelp, with additional metadata including the name of the coffee shop being 
reviewed as well as that user’s rating for the coffee shop on a scale of 1 to 5

## Algorithms:

For this project a complete recommendation model was created by way of an unsupervised learning model.  
The initial pre-processing was done with a combination of spaCy and regex.  The original reviews had punctuation 
removed, while words were lemmatized and tokenized into uni-grams as well as bi-grams. The clean documents were
then vectorized via scikit-learn Tfidf and topic modeling was done via NMF. 

Evaluation of topics was done via a combination of looking at top words and top documents,
with pre-processing and hyper-parameters tuned to create more relevant topics after each iteration. 
Once satisfactory, document/topic vectors were then aggregated across all reviews for a given coffee shop, 
and pair distances were measured via euclidean distance to create coffee shop affiliations with each topic.  
This is the foundation of this content-based recommendation system, where a new word was evaluated for its 
relative distance to each coffee shop and a recommendation could be made using the closet coffee shop.

## Tools:

-spaCy, regex, and scikit-learn for text preprocessing and data handling

-Numpy and Pandas for data manipulation

## Communication:

The slides that are presented contain relevant visualization of data and conclusions drawn from that data
