## Abstract:

The goal of this model was to use 2D images of plant leaves as data and build a Convolutional Neural Network model that could classify images of leaves to the appropriate species.
A dataset of 3300 leaves from 40 different species (including ground truths) was imported into python and then split into train and test data.  Rigorous model testing and 
hyperparameter tuning was done to improve validation set accuracy while reducing the score of the loss function. The best performing model scored 71% accuracy on unseen data while scoring
1.15 on the loss function.  Given the success of the model with the relative lack of data, there are implications that performance can still be improved by incresing the sample size and improving
computing power to allow for higher quality images to be processed.

### Design:


This project originated from the fact that there has been a great increase in the purchases of houseplants, and a desire to be able to identify the species of plant can be challenging 
if the plant's name is not known.  Deep learning is an ideal canidate for this sort of task, as a image dataset of leaves or other identifying features could be used to train a model that would be able to 
classify plant images by species.  Successful implementation of this model could allow for users to identify plants of interest so that they could look to purchase those plants, or better 
take care of a plant they own but did not previously know the identity of. 


### Data:

Data for this project was downloaded through gigadb.  The dataset contains 3,294 2D leaf images all withing the Passiflora species but of 40 different genuses
, with ground truths identifying the specific genus. The original images are black and white and are 1000 by 1000 pixels. Imagesnet images were also indirectly used, as the Xception
transfer learning model was applied to this project.

### Algorithms:


For this model a convolutional neural network was constructed in python to be able to classify image data and indentify the genus of plant within the dataset. A base model was produced using
a simple arcitecture containing convolution layers and pooling layers to better capture the structure of the leaves, followed by a flattening layer and then fully connected top layers which output
to 40 different nodes for each of the 40 genuses of plant in the dataset. Given that the problem was multi-classification, accuracy was chosen as the evaluation metric, with categorical crossentropy
the desired loss fuction to evaluate on.  Using feedback on the validation set, regularization was done to improve overfitting, while transfer learning was done to help account for a 
lack of data and to provide a more robust architecture. Hyperparameters were tuned to improve scores in both accuracy and categorical crossentropy. Rigorous model selection was done to maximize validation
set accuracy while reducing validation set loss. In the end a model using Xception architecture as the base with a custom top layer was used as the final model.



### Tools:
-Keras packages were used for CNN model creation and testing
-OS for data entry to python
-Numpy and Pandas for data manipulation
-Google colab for cloud computing 

### Communication:
The slides that are presented contain relevant visualization of data and conclusions drawn from that data
