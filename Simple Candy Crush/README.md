# Basic Candy Crush 

This program is about implementing a basic elimination for Candy Crush. 
Given a 2D integer array board representing the grid of candy, different positive integers `board[i][j]` represent different types of candies. 
A value of `board[i][j]`=0 represents that the cell at position (i, j) is empty.
The given board represents the state of the game following the player's move. 
Then the program implement crushing candies according to the following rules:

* If three or more candies of the same type are adjacent vertically or horizontally, "crush" them all at the same time ‐ these positions become empty.  
> 三個或三個以上的數字連在一起，則把它們合在一起

* After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. (No new candies will drop outside the top boundary.)  
> 如果格子內為0，則自動讓上面的數字掉下

* After the above steps, there may exist more candies that can be crushed. If so, repeat the above steps.  
> 如果一次合併後還有新的連線，則重覆消除動作

* If there does not exist more candies that can be crushed (ie. the board is stable), then return the current board.  
> 重覆執行到格子內的數字是穩定狀態(沒有相同三個以上數字相連)，輸出檔案

## Getting Started
* **table / newtable:** the matrix storing numbers  
* **booltable:** the boolean matrix storing if the position has number  

* `check` : it's the function check if there is any pair of same number.  
If there is no pair, then return False to determinate the loop. If there is some pairs, then implement `move` function.
* `move` : after eliminating the numbers, fill blanks by dropping above numbers
