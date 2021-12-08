The purpose of this project is to go back to a previously created recommendation model, and complete an
end-to-end product.  The benefit of this end-to-end product would be a usable coffee-shop
recommendation system that is customizable for what the user seeks in a coffee shop.

The dataset that will be use will reviews from google business.  This data will be aquired by creating
a real-time datapipeline via their API and storing this data in a MongoDB. An individual row of data will
contain the name of the coffee shop and the text of the review.

For this project I will be using MongoDB for data storage, as well as streamlit to create a web application that 
users can interact with to generate recommendations for themselves.  I will also be using APIs as a 
means for data aquisition.

A minimum viable product for this project would be to execute a one-time run of my datapipeline and succesfully
store the data in a mongoDB.
