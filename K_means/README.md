# Data Science Algorithm : K-means  

It's the algorithm implement step by step for K-means. By reading a data file, 
this program will separate them into four groups(k=4) and show the clustering process.

## Algorithm
* `step 1` **select k points randomly :** Given an assigned number k, select k points from data. 
> 隨機指派k個點當作起始指定點

* `step 2` **compute distance & grouping :** Compute distance from each point to all k points and 
group it to the nearest point from the previously assigned points.  
> 計算每個點到指定點的距離並分配到最近指定點的群

* `step 3` **re-grouping:** According to the lately result, compute the newly group center and repeat step 2 
> 重新計算群體中心點直到群體中心穩定

***
## Program Introduction  
#### parameters  
* **xpoints** : storing the previous groups' center  

* **SSE_y** : sum of square error  

#### functions  
* `SSE_count` : Append the value of square error to SSE_y.  

* `find_points` : Randomly select k points from data in the begining.  

* `k_means` : Compute distance and group the data points until the groups' center is stable.
One grouping and one graphing. The four group data are separate by color of purple, green, blue, and yellow.
