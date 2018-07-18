# Location of McDonald's 麥當勞與捷運站相對關係  
According to the geographical theory, the stores are usually located in the spot near the traffic hub. 
As a result, I do this final report with `plotly` and `Mapbox` by using API offered by Google.  

> 在地理理論當中，大多數商家選擇據點設置在交通便捷之處，
而自己在測量系**空間資訊概論**的期末實作報告當中，
想藉由google的API服務搜尋麥當勞進行資料點的探討，
並利用python套件之一 `plotly` 加上搭配 `Mapbox` 進行視覺化。  

## Description  
#### `Part1`  Mcdonlod's V.S. Metro  
In this part, the program compare the Mcdonlod's data with metro data and compute the number of the Mcdonlod's nearing metro stations.
By using google API, we can obtain the Mcdonlod's data nearing each station and sum it up.  
>在第一部份的程式，主要為找出各個捷運站附近500公尺的麥當勞資料並計算其總營運佔比(在臺北地區的部份)  


#### `Part2`  Mcdonlod's V.S. KFC  
The second part is the comparison of Mcdonlod's and KFC. It's believed that spots of Mcdonlod's and KFC's share highly relation.
Therefore, this program grab data from google map and compute the percentage of KFC stores nearing Mcdonlod's of its all stores.
Moverover, we also compute the percentage of Mcdonlod's stores nearing KFC of its all stores and compare it to the previous one.  
>第二部份的程式針對肯德基在麥當勞所有設點的半徑200公尺進行討論，也同時相比較麥當勞與肯德基之間的設點關係  

[1]: https://data.gov.tw/dataset/61792

## Tool  
* **Open Data** : The [metro data][1] is offered by government opendata website.  

* **Google API** : We will collect McDonald data by using this service.  

* **Plotly** : The package in python which helps us visualize the data.  

* **Mapbox** : The map service which can help us to tag data on the map directly.  

## Program  

* `Read Metro Data` : In this part, we read the csv file to gain all metro stations' name(108 stations) and print it out.

#### function  
`access_number` : It's the function that we can call it to get a certain column we want(lat or lon).  

` search` : Search for the targets we want by using `gmaps` and check data with id to confirm there is no repeat store id. 
In the end, we only access columns of lontitude and latitude then return them.
  * `geocode` is the function that helps convert location name into coordinate system.  
  
  * `place_radr` is the function that gets data(keyword) from the assigned spot(location) near area(radius).
  
  #### visualization  
  ###### part 1
  `map_data` : ( red ) spots of **McDonald's** near to the metro stations  
  `m_all` : ( blue ) spots of all **McDonald's** in Taipei    
  `metro` : ( orange ) all **metro** stations in Taipei  
  
  ###### part2
  `all_2_data` : ( orange ) all **Mcdonlod's** in Taipei    
  `kfc` : ( red ) spots of **KFC** near to the McDonald's  
  `all_kfc` : ( green ) all **KFC** in Taipei
  
  
***  
[2]: https://plot.ly/~gyuler83821/268/
[3]: https://plot.ly/~gyuler83821/270/map-of-mcdonalds-vs-kfc/
視覺化結果：
1. [麥當勞在捷運站附近][2]的佔比 `66%`  
> 麥當勞的設點在捷運站佔了它所有營運的66%，因此可以推論麥當勞設點策略跟捷運站息息相關。  

2. [肯德基在麥當勞附近][3]的佔比 `52%` ；麥當勞在肯德基附近的佔比 `20%`
> 肯德基高達五成在麥當勞附近設點，然而針對一家麥當勞而言，肯德基在附近出現的機率只有兩成左右(可能是因為肯德基據點較少)，
所以直觀而言似乎肯德基較依賴麥當勞而設立據點。
