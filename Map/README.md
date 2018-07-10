# Location of McDonald's 麥當勞與捷運站相對關係  
According to the geographical theory, the stores are usually located in the spot near the traffic hub. 
As a result, I do this final report with `plotly` and `Mapbox` by using API offered by Google.  

> 在地理理論當中，大多數商家選擇據點設置在交通便捷之處，
而自己在測量系**空間資訊概論**的期末實作報告當中，
想藉由google的API服務搜尋麥當勞進行資料點的探討，
並利用python套件之一 `plotly` 加上搭配 `Mapbox` 進行視覺化。  

[1]: https://data.gov.tw/dataset/61792

# Tool  
* **Open Data** : The [metro data][1] is offered by government opendata website.  

* **Google API** : We will collect McDonald data by using this service.  

* **Plotly** : The package in python which helps us visualize the data.  

* **Mapbox** : The map service which can help us to tag data on the map directly.  

# Program  

* `Read Metro Data` : In this part, we read the csv file to gain all metro stations' name(108 station) and print it out.

#### function  
`access_number` : It's the function that we can call it to get a certain column we want(lat or lon).  

` search` : Search for the targets we want by using `gmaps` and check data with id to confirm there is no repeat store id. 
In the end, we only access columns of lontitude and latitude then return them.
  * `geocode` is the function that helps convert location name into coordinate system.  
  
  * `place_rader` is the function that gets data(keyword) from the assigned spot(location) near area(radius).
  
  #### visualization  
  `map_data` : ( red ) spots of McDonald's near to the metro stations  
  
  `m_all` : ( blue ) spots of all McDonald's in Taipei  
  
  `metro` : ( orange ) all metro stations in Taipei  
  
  
  
