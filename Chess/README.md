# Chess 西洋棋

`getNumExit` :  
It can check the next step of eight cobinations is valid.  
If the next step is valid, and it will compute the exists the next step owns then return the value.  
If the next step is invalid, and it will allow return -1 mesning that the step can not be pass.  

`output`:  
It's a function only when the knight has no exit to go will be called.  

`main` :  
Firstly, we initialize the disk 8x8 and its value all of 0.  
Then according to the situation change the value of unused cells to -1.  

Secondly, we enter the `getNumExit` to find out the next step knight should go.  
**Noted** : If all next steps can't be passed (numFalse:number of cannot-pass), call `output` function, and end the program.  

If the process confirms that the knight has the road , then we find out the next step owning least exits.  
Recording every step , and print out the result finally.  
  
