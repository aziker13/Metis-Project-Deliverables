The objective of this model is to be able to classify 2D pictures of leaves to the species of plant.  After importing the images and ground truths into python, a simple 
CNN was created from scratch to establish to establish a baseline model.

![Screenshot from 2021-11-30 17-04-58](https://user-images.githubusercontent.com/87049486/144153709-0b0f97b3-f4c2-4bbf-a099-50bd4e3326e2.png)

Given that there are 40 different classes within this dataset, 34% accuracy is better than random. Additionally, the model was improving consistantly across 10 epochs,
indicating that the model is a good foundation to build off of. The next steps are to try and see if any transfer learning could be implimented to help improve the model, while
also looking at other techniques such as RNN or LSTM.
