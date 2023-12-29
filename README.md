# DELTER
DELTER refers to Deep Learning Terrain Recognition 
It currently has 4 classes- Rocky, Sandy, Marshy, Grass
This project has three parts:

1) The frontend
   
   It has been designed by just using simple html,css and javascript.
   
2) Backend Server
   
   Functioning:-
   
   It takes the image submitted through the frontend to the the DELTER model and then DELTER makes it's prediction.
   This prediction is then send to the server from where the frontend can take the prediction by using a simple get request.
   It uses a byte file created by DELTER to get the prediction of the input image.
   
   About the Server:-
   
   This backend server is made using python and fastapi framework.
   It is made functional after a lot of experiments so it may a have a lot of messy code.
   The code for this server is in try.py
   
3) Backend deep learning model:
   
   Data:-
   
   Its data comprises of more than 12000 images of 4 different terrains and each terrain has 300+ images.
   These terrain images are being taken from kaggle.
   I have used data argumentation techniques to further increase the dataset.
   
   Model:-
   
   For the training of data, I have used transfer learning. I have made use of a pretrained model called ResNet 50.
   On top of ResNet 50 I have applied some layers, for adding relu function, a layer for regularization, a layer for categorizing different classes of dataset.
   I have trained the data for 10 epochs after which overfitting was observed.
   The highest accuracy of the model is 90%.
   After training the model with the dataset, the model was ready for making inference so I converted it into a byte file using model.save .

   Code for the DELTER model in terrainRecModel.ipynb
   
   
It is a small project but I have some future plans to work on, which would add some more functionality to the project

Future Scope:-

1) Give the roughness of the terrain form the submitted image:
   
   In this a linear regression model is required to be trained on some data to give the measure of roughness.
   I know a dataset on kaggle which has been made by moving vechiles on different terrain and these vechile had sensors to measure the roughness of the terrain.
   
2) Using the open source LLaMA model:
   
   Meta's LLaMA model can be used to get the descriptive analysis of the submitted terrain.
   
Any contributions would be appriciated.

This project has been made with the contributions of:

  1) Mradul Bhardwaj                   Contact:- https://www.linkedin.com/in/mradul-bhardwaj-61a9aa22a/
  2) Abhishek Shandilya                Contact:- https://twitter.com/shandilyabh

   
   
   
   
