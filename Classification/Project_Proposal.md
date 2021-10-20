## They shoot, they score! Making predictions on what attmepts will result in a goal

"Goals change games" is an old addage in soccer that states the obvious impact that scoring a goal has, but what factors make a shot attempt more or less likely to
go in? And could data science be used to predict the outcome of a shot given a few points of reference about the shot being taken? Being able to make accurate
predictions about goal scoring opportunities could help guide coaches in how they set-up tactics, and instruct players on where to take up positions on the 
field. Additionally it could help offices find value on the transfer market for players who get into the right positions on the field but maybe for factors not in their
control don't get the end result.  Lastly understanding the profile of where and how teams take changes could give insight into making predictions on games and
allow bettors to better assess who will win a game.

A data set on Kaggle had every attempt on goal recorded in all 5 of the top european leagues spanning 5 years from 2011/2012 to 2016/2017, and this will be
downloaded as a CSV file.  An individual row of data has 22 columns, and included in that are things relavent to goal scoring such as player name, time of the game, position on
the field, where at the goal the player is aiming, what body part they are shooting with, and how they recieved the ball to begin with. The end prediction of this model
will be a binary yes/no for whether or not the attempted shot resulted in a goal.

Classification models provided in python packages such as sklearn and xgboost will be utilized to create the model, along with other visualization tools such as 
matplotlib and seaborn.

A minimum viable product for this project would be a baseline model for predicting the outcome of a shot on goal with little feature engineering.
