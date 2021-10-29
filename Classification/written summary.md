Abstract:

The focus of this project was to use a classification model to predict whether an attempted shot during a soccer match would result in a goal or not,
and have interpretability in the key features.  Data was provided through a Kaggle dataset call “football events”, containing categorical information on
the characteristics of each attempt on goal.  After cleaning and EDA, model testing and feature engineering was done to produce the final logistic regression model.  
This model provided insight and direction for further study into the desirable locations on the field and placement of shot attempts to maximize odds of a goal.

Design:

The idea for this project came from the recent uptick in soccer broadcasters referencing xG (expected goals) as a key statistic in 
evaluating the match and each team’s performance.  Coaches and team presidents are looking for ways to more accurately assess individual and
team performance as relates to scoring goals, and insight into what the data says about making high percentage shots could influence how coaches determine 
on-field strategy and training during practice. Additionally, players can be more accurately evaluated for their performance using a probability based metric, 
as other factors outside of the players control impacts the chances of a goal. 

Data:

The raw data contained 941,009 rows of data with 22 features.  After removing rows containing Nulls in columns that should have a value,
and removing rows that were not data regarding attempts on goal, 227,451 was the number of attempts on goal usable for this model. 
after creation of dummy variables for categorical features, 46 total features were used for the model.

Algorithms.

1)	Model selection was done along the basis of f1 scores, log loss, and feature interpretability.  Each model was lightly optimized via hyperparameter tuning to give a fair indication of model performance prior to selection of a final model

2)	Data was split into 60/20/20 train/validate/test, with test data remaining unused until the end of the notebook.  In instances of cross validation, train/validate data was combined so CV was done on 80% of the data. 

3)	Feature engineering was done to create new categorical variables given the information already in the dataset

4)	Class imbalance was present in the target data (90% negative, 10% positive), so balancing was attempted in 2 ways (independent of each other) and final use was based on performance. First was undersampling the majority to create a 50/50 distribution of the data, second was to adjust weights within the model.

Tools:

-Numpy and Pandas for EDA and feature engineering
-sklearn for modeling
-matplotlib and seaborn for visualizations

Communication:

The slides that are resented contain relevant visualization of data and conclusions drawn from that data
