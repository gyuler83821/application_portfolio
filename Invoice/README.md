# Invoice 發票兌獎  
Because the thing checking every invoice one by one is annoying, this program will help us get the sum of money more quickly.
By reading a data file easily, this program will output the result prize finally.
> 藉由讀取發票檔案，即可在此程式中獲得最後中獎金額

## Program  
#### file
`final.h` : including the list of the prize number and some other parameter settings  
> 包括中獎號碼以及中獎金額參數的調整  


`final_data` : the invoice data  

#### function  
In this program, the notation `.` means the end of the data file. 
Besides, if the length of data number is not equal to eight or having repeat number, the program will not count it.  
> 在程式當中把`.`當作檔案的結束，同時也針對不符合規定的資料數字以及重複編號進行排除，以免發生重複計獎狀況。  

`check_bonus` : the function comparing the data and the prize number and output the money
