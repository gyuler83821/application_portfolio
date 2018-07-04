# Mouse in a Maze 老鼠走迷宮

## Algorithm Introduction
This algorithm is aiming finding the path to the exit. Moreover, the road which was passed before will not be passed again. 
Therefore, this algorithm can find the exit in the end.  
> 此演算法的規則是會記錄走過的路，並且不會再次走死胡同的路，如果遇到死路則會回頭找還沒走過的路當路徑

## Program Introduction
* `getNumExit` : It can check the next step of eight cobinations if is valid.   
If the next step is valid, and it will compute the exists the next step owns then return the value.  
If the next step is invalid, and it will allow return -1 meaning that the step can not be pass.  
> 進行路徑的擴張，如果發現不能通行則把位置標示-1，如果可以通行則計算下個可能的路徑的出口數

* `output` : It's a function only when the knight has no exit to go will be called.  
> 如果迷宮是死胡同則呼叫此函式

* `main` : Firstly, we initialize the disk 8x8 and its value all of 0. Then according to the situation change the value of unused cells to -1. Secondly, we enter the `getNumExit` function to find out the next step knight should go.  
**Noted** : But if all next steps can not be passed (numFalse:number of cannot-pass), call the `output` function, and end the program. 
> 即時更新走過的路徑並呼叫 `getNumExit`

If the process confirms that the knight has the road, then we find out the next step owning least exits.
Recording every step, and print out the result in th end.
