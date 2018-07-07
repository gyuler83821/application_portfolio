# Star Prediction 商家星等預測

In this program, it's aiming to build a model to predict stores' star level by comments. 
Moreover, the accuracy of prediction is by using RMSE (root-mean-square error).
Therefore, in my program 

## Final Code
Allowing the `HashingVectorizer` to have two parameters:  

`n_features` : the amount of the total features we want to select  

`stop_words` : whether neglect stop words, it can be a **list** →the words we want to neglect or just “english” standing for choosing language of English’s stop words  

And then split the training data and use `fit_transform` to turn the pure text into **vector** type (for training data) 
and `transform` (for test data).

The method I use to predict the stars is `LinearSVR` because the linear models (the predictions are float type) show the better prediction than logistic models (the prediction are integer type) when testing accuracy in **RMSE** among several testing I have tried.  

`RMSE` : This part is the demonstration of computing RMSE.  

## Another Try
There are other ways to build this prediction model by using different algorithm about vectorizing words 
such as `CountVectorizer` and `TfidfVectorizer`. 
Besides, I also implement otherprediciton medel such as `LinearRegression` and `LinearSVR` looking forward to 
finding the best model of prediction.  
