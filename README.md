# X-ray Image Classification for Pneumonia using Transfer Learning (VGG16) with Convolutional Neural Network

## Purpose:

- The purpose of this project is to use convolutional neural network to classify chest X-ray images of normal and pneumonia cases. 

## Goal:
- Classify x-ray images for normal and pneumonia cases.

## Dataset Description:
- The dataset used for this image classification analysis is from Kaggle (https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia). 

- There are three directories in this dataset, which include: train, test, and validation. The train directory has 5216 jpg images (NORMAL: 1341, PNEUMONIA: 3875), the test directory has 624 jpg images (NORMAL: 234, PNEUMONIA: 390), and validation directory has 16 (NORMAL: 8, PNEUMONIA: 8). Under each directory, there are two categories: NORMAL and PNEUMONIA, where PNEUMONIA can be further splitted into bacterial pneumonia and viral pneumonia. 

- However, considering the images included in the validation directory is quite small, I first combined all the images from train, test, and validation directories, and splited them into model set (80%) and testing set (20%), then further splited the model set into training set (80%) and validation set (20%). So the final training, testing, and validation sets include 3747, 1172, and 937 images, respectively.

## Results:
- 88% of total pneumonia cases were correctly classified by the transfer learning model (recall rate).

## Application:
- Built an app for X-ray image classification.
- https://whispering-gorge-65529.herokuapp.com/

## Reference:
- https://www.mayoclinic.org/diseases-conditions/pneumonia/symptoms-causes/syc-20354204
- https://www.kaggle.com/deadskull7/best-score-on-kaggle-96-recall
- https://github.com/gabrielpierobon/cnnshapes/blob/master/README.md
