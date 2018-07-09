# Kobe's Shot Type Prediction 柯比·布萊恩的投籃預測   

## Description  
*	loc_x:  
Because the loc_x in this data means the x-axis location of the shot (values from 0 to 250 standing for the left side to the right side), it does not mean the truly distance from the basket. We decide to convert it by computing absolute value of **abs(loc_x)-125** 
(125 is the x-axis location of the basket if it’s on the center. Value of loc_x might be minus.). 
By doing this, the values we use will be the distance to center in fact.  

*	period:  
In normal basketball games, there are 4 periods in a game. However, it still emerges some games with 5,6 or 7 periods in the game. To define the column of period, we allow the number of period more than 4 to be unified number 5 representing the game has longer than formal. 

*	loc_y:  
In data, some of loc_y represent the negative values. 
However, it just means that the shot is “behind” the basket rather than the distance is negative. 
Consequently, we convert it to **positive** value by using the function `abs()` .

*	seconds_remaining:  
"Seconds_remaining" in this data just stands for the left seconds in "this" minute. 
We consider it should be the total remaining time to present the property of the column, time. 
And we replace it with the values of computing **(minutes_remaining x 60+seconds_remaining)/10** as a result. 
Then we are afraid of the values of seconds_remining too large, so we divide 10 to it.  

* game_date:  
For the column "game_date", it clearly represents the date of the game. 
However, the whole kinds of the game_date is too much to classify data. 
Then we decide to discard the date of the game and maintain the year and month as the column information like the form of **(yyyy/mm)** by using function defined by myself called `date()` .  

* (Created) **behind**:  
Considering the shot might occur behind the basket, we decide to create a new column called "behind" containing Boolean values standing for whether the shot being behind the basket. (To create this column is because I think that the players may have the **certain types of shot to manage the situation of being behind the basket**.) And we use the data of loc_y to define the column.  

*	(Created) **side** :  
During the game, most of shots are taken form the area near by the basket. However, there are also some surprising shot taken in long distance. According to the thought mentioned above, I believed that for **long distance players would prefer to some kinds of shot**. Therefore, I define it as the player on the other side of the court. If he is on his team side, the Boolean will be True.  

In some features, they are usually represented by continuous value such as distance or seconds. 
However, some features would be considered as classification, type, period, opponent, for instance. 
Therefore, we should separate them to allow the column to be more useful. 
And I think that `period`, `opponent`, `shot_zone_area`, `behind, playoffs`, `season`, `game_date` and `shot_made_flag` would be the classification type. 
After doing classify the columns, then we impute the nan value by using function called `Imputer()`.
As all preprocessing finished, we import the algorithm called **`Random Forest`** to train the model of analysis and predict data.  

## Program  

