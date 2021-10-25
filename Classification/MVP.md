After successfully importing the data into Pandas, some cleaning exploration was done prior to modeling. Namely, undesired columns were dropped, and N/A values
for certain features were dropped if they did not make sense as a value. The next step was to replace the integer values in certain columns (such as shot_outcome)
with a string object so that dummy variables could be created for those columns.

After the cleaning, trimming, and creation of dummy variables I visualiuzed the distribution of my target values. I 
ran a basic logistic regression as well as a 10 fold cross validation to evaluate for f1, as
accuracy isn't particularly relavent given the imbalanced classes for the target. 



![Screenshot from 2021-10-25 14-57-02](https://user-images.githubusercontent.com/87049486/138777628-17322a5b-d995-4b4f-bc4b-e1e7fbe709e9.png)
![Screenshot from 2021-10-25 15-05-16](https://user-images.githubusercontent.com/87049486/138777632-2788bf23-4eee-4fea-877e-7752857a4bba.png)

There is a lot of potential feature engineering as well as model selection to be done. The goal is to have an interpretable model so I will look to evaluate other models
with that in mind. A combination of f1, interpretability of coeficients, and cross-entropy will be used to determine the ideal model. 
Additionally, futher data manipulation using undersampling from the majority class to create more balance. This will also help with any potential over fitting from
decision trees and similar models.
