# Chess 西洋棋
This program is the test of knight's tour. The knight will pass every lattice by its certain step to complete this mission.
If the knight can not complete all lattices, this program will output `no solution`.
Otherwise, if the knight succeeds, this program will output its path.  
> 此程式為利用西洋棋中的騎士走法，試圖讓騎士能遍歷所有格子，如果成功則輸出所有路徑，如果失敗則輸出 `no solution`.  

## Program  
#### function  
`getNumExit` :  
It can check the next step of eight cobinations is valid.  
If the next step is valid, and it will compute the exists the next step owns then return the value.  
If the next step is invalid, and it will allow return -1 mesning that the step can not be pass.  
> 計算下一步(8個方向)的合法出口數量為何，如果下個出口數量為0，則回傳 `-1` 

`output`:  
It's a function only when the knight has no exit to go will be called.  

`main` :  
1. we initialize the disk 8x8 and its value all of 0. Then according to the situation change the value of unused cells to -1.  
2. we enter the `getNumExit` to find out the next step knight should go.  
**Noted** : If all next steps can't be passed (numFalse:number of cannot-pass), call `output` function, and end the program.  

If the process confirms that the knight has the road , then we find out the next step owning least exits.  
Recording every step , and print out the result finally.  
 
