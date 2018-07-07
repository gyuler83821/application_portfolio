# Star Prediction 商家星等預測

In this program, it's aiming to build a model to predict stores' star level by comments. 
Moreover, the accuracy of prediction is by using RMSE (root-mean-square error).
> 在藉由文字評論去進行星等預測的過程當中，在這個程式當中會運用不同演算法進行準確度的比較。而在程式當中作為準確度評估的方法是**方均根差**。  

* `training_data.csv` : training data  
  * review_id : number
  * business_id : store id
  * user_id : users id
  * **text** : users comment
  * date : the date of the comment
  * **stars** : star level the user gave
  
* `test_data.csv` :　test data (lack of the **stars** column)  

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
> 在其它嘗試的部份，也運用其它演算法轉換字詞至向量及模型進行預測並比較RMSE的高低  

### classification by part of speech (詞性)
The feedback text is composed of several parts of speech (NOUN, ADJ, ADV…) with different meaning and emotion.  

Therefore, excluding stop words is an important thing to filter out the meaningless words or vocabularies of helpless forprediction. 
And selecting those words with emotion like “disgusting”(negative) or “pleasure”(positive) must be the mission prior to deciding which algorithm to use.  

Consquently, this program merges the prediciton we did before with numbers of part of speech and does the second prediction 
by using `LinearRegression` to get another prediciton.

To get more information about the text, I apply `pos_tag` function in `NLTK` module to mark each part of speech of word and count the number of them with the text as the new feature. 
Among the several part of speech, I choose some significant part of speech such as **ADJ, NOUN, VERB, ADV** which might be with more information about the clients’ viewpoint to the store. 
However, the common part of speech have detailed category such as “JJ”, “JJR”, and “JJS” but all of them stands for “ADJ”. As a result, I add the similar part of speech together shown in the picture list type─ **pos_list**.  
> 為了得到那些具備擁有情緒資訊的詞，`pos_tag`可以幫註標記詞性，而同時我們也把相似的詞性匯整(比如JJ,JJR,和JJS都是代表形容詞)，
並統計數字並作為另一個預測屬性，再用`LinearRegression`進行星等預測。

 
 
