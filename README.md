# OpenCVCricketerFaceRecognizer

### Face recognition is a method of identifying or verifying the identity of an individual using their face.
The Model is build using OpenCV, Sci-kitlearn,PyWavelet. The dataset used in this model contain around 800 images of 15 top Indian cricket players (who have participated in the 2019 ICC Men's Cricket World Cup). There are 50-60 images per player.

#### Unknown ~  
*The human face is a dynamic object and has a high degree of variability in its appearance,which makes face detection a difficult problem in computer vision.*

### OpenCV - 
OpenCV is an open-source library used by most of the Developers because of its simplicity. I have used OpenCV in here to read image and Capturing image 

For Model processing I used Linear Regression, SVM, Random Forest, XGBRegerssor, ExtraTreesRegressor, GridSearchCV and then select the best from them.

The Training Dataset used contain 600 images and test dataset contain 200 images of these cricketer.

I converted The Image in Wavelet tranform and the combined original with it. The wavelet transform is a way of expressing a signal as a collection of smaller
wavelets. 

<img src="https://user-images.githubusercontent.com/54480904/119136586-7c981a80-ba5d-11eb-9197-90589c72e275.png" heigth=322px width=322px> &nbsp;   &nbsp;   &nbsp;   &nbsp;   &nbsp;  &nbsp;   &nbsp;   &nbsp;   &nbsp;   &nbsp;  <img src="https://user-images.githubusercontent.com/54480904/119136589-7dc94780-ba5d-11eb-8a1d-368f34395d3a.png" heigth=300px width=300px>

&nbsp;   &nbsp;   &nbsp;  This is original Image of Virat Kohli &nbsp;   &nbsp;   &nbsp;    &nbsp;   &nbsp;   &nbsp;   &nbsp;   &nbsp;    &nbsp;   &nbsp; &nbsp;   &nbsp;   &nbsp;    &nbsp;   &nbsp;   &nbsp;   &nbsp;   &nbsp;    &nbsp; And This is its Wavelet Transformation

<br/>
Like here is a ScreenShot of XGBRegeressor Confusion Matrix. We can clearly see the uncertainity.


<img src="https://user-images.githubusercontent.com/54480904/119136597-7efa7480-ba5d-11eb-814d-68d6277beb1b.png" heigth=500px width=500px>

#### And Here is Extra Tree Regressor
 
<img src="https://user-images.githubusercontent.com/54480904/119136600-7f930b00-ba5d-11eb-9698-25b26fa83317.png" heigth=500px width=500px>

### SO to sum up I tried different approach to gain good acccuracy.

## Finally I Choose SVM and here are the result

![Best Classifier](https://user-images.githubusercontent.com/54480904/119136593-7e61de00-ba5d-11eb-958a-5a8e38180417.png)



![Screenshot (114)](https://user-images.githubusercontent.com/54480904/119136601-802ba180-ba5d-11eb-96fe-f2156c02ecec.png)


***Contact***

```
Name: - Rahul Amarwal 
Email:- rahulamarwal418@gmail.com
Phone :- 8505065521
```

To use dataset click [Here](https://drive.google.com/file/d/1K_OUszvCKLtvQv_DCHfZBRJEkQa173qH/view).
