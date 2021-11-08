The goal of this project is to use coffee shop reviews from yelp to build a recommender model.

![Screenshot from 2021-11-08 14-38-29](https://user-images.githubusercontent.com/87049486/140831921-ee2be268-3b57-4ad6-81d5-a4ddd217a1c8.png)

After some preprocessing and running the term-document matrix through  truncated SVD we have an initial 5 topics. 

From these topics, it's clear we have some solid terms to work with, but more pre-processing needs to be done to help
create more interpretable and distinct topics. Once this is achieved, each coffee shop's reviews will be aggregated and
what coffee shops are strong in each topic can be used to help make recommendations
