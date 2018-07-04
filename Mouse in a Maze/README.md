# Mouse in a Maze 老鼠走迷宮(遞迴)

## Algorithm Introduction
This algorithm is aiming finding the path to the exit. Moreover, the road which was passed before will not be passed again. 
Therefore, this algorithm can find the exit in the end.  
> 此演算法的規則是會記錄走過的路，並且不會再次走死胡同的路，如果遇到死路則會回頭找還沒走過的路當路徑

## Program Introduction
`getNumExit Function` : It can check the next step of eight cobinations if is valid.   
If the next step is valid, and it will compute the exists the next step owns then return the value.  
If the next step is invalid, and it will allow return -1 meaning that the step can not be pass.  

`output` : It's a function only when the knight has no exit to go will be called.  

`main` : Firstly, we initialize the disk 8x8 and its value all of 0. Then according to the situation change the value of unused cells to -1. Secondly, we enter the `getNumExit` function to find out the next step knight should go.  
**Noted** : But if all next steps can not be passed (numFalse:number of cannot-pass), call the output function, and end the program.  

If the process confirms that the knight has the road, then we find out the next step owning least exits.
Recording every step, and print out the result in th end.
