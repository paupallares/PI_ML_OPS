
</p>
<div style="display: flex; margin-left: 20px; align-items: center;">
  <h2 style="text-align: left;">[Machine Learning Operations (MLOps)]</h2>

					> Proyecto Individual  

###  <p align="center"> **Paula Pallares** :technologist:

#### 

<hr>  
</head>
<body>
  <h3>Contenidos</h3> 
  <ul>
    <li><a href="#objective">Objetivo</a></li>
    <li><a href="https://github.com/paupallares/PI_ML_OPS/blob/main/ETL-Transformaciones.ipynb">ETL</a></li>
    <li><a href="https://github.com/paupallares/PI_ML_OPS/blob/main/API-Funciones.ipynb">Funciones API  </a></li>
    <li><a href="https://github.com/paupallares/PI_ML_OPS/blob/main/EDA-An%C3%A1lisis.ipynb">EDA</a></li>
    <li><a href="https://github.com/paupallares/PI_ML_OPS/blob/main/ML-ModeloRecomendacion.ipynb">ML desarrollo algotirmo</a></li>
    <li><a href="https://pi-ml-ops-3gcr.onrender.com/">Proyecto deployado</a></li>
    <li><a href="https://youtu.be/OHSTXRbtsqA">Video presentación</a></li>
    <li><a href="#tools">Herramientas usadas</a></li>
  </ul>

## <p align=center>:green_circle:  Descripción del proyecto :arrow_down: 

## <p align=center>:clapper: :movie_camera: :film_strip: :film_projector:  :popcorn: 

####   <h2 id="objective" style="text-align: center;">OBJETIVO</h2>


- [x] Este proyecto consiste en analizar un dataset de peliculas con el objetivo de aplicar un sistema de recomendación que devuelva 5 películas similares a la elegida. 

**`Pasos desarrollados:`** 

- [x] ETL : carga, exploración y transformación de datos, nulos, duplicados, eliminación de campos innecesarios.
- [x] API: creación de 7 funciones básicas para recopilar datos.
- [x] EDA: análisis exploratorio del dataset, elección y jerarquización de campos y datos, imputación y discretización de algunas variables.
- [x] ML: para el sistema de recomendación usé una matriz TF-ITF para la interpretación del texto y una matriz de conteo para los metadatos, luego con la similaritud del coseno se procesaron las recomendaciones.
- [x] Deploy final: haciendo uso de FastAPI y render.com hice un deploy final con todas las funciones* disponibles en este link: <a href="https://pi-ml-ops-3gcr.onrender.com/">< Deploy en render.com ></a>

<p align="center">
<img src="https://github.com/HX-PRomero/PI_ML_OPS/raw/main/src/DiagramaConceptualDelFlujoDeProcesos.png"  height=400>
</p>


**`Decisiones tomadas:`** :brain: 

Para el modelo de recomendación decidí utilizar campos que me dieran información sobre la trama, temática y tono de la película, dándole importancia al género y teniendo en consideración si la película es nueva o antigua y los idiomas hablados en el film para tratar de llegar a gustos más particulares.
Descarté rapidamente las variables numéricas relacionadas con dinero, solo dejé popularidad y puntaje (vote_average) para usarlas como filtro y recomendar así películas que sean famosas o populares, les apliqué MinMaxScaler y StandardScaler para standarizar los valores pero dejé el filtro fuera del modelo entregado por costos computacionales. 
Para los datos de texto usé dos vectores, el TF-IDF para 'overview' y 'tagline' para extraer mejor la relación entre las palabras e identificar su importancia y usé Vector Count para 'genres' (x2 para darle más jerarquía), 'decade' y 'spoken_languages' para contabilizar la frecuencia de los términos ya que considero que estos datos se asemejan más a 'metadatos' que a un procesamiento de lenguaje natural. En ambas matrices obtengo similaritud por coseno para luego sacar la similaritud del coseno entre ambas matrices dandole un peso superior a la matriz TF-IDF (60/40) ya que considero que la temática y trama deberían ser más influyentes en la recomendación.


					𝑐𝑜𝑠𝑖𝑛𝑒(𝑥,𝑦)=  𝑥.𝑦⊺
						  ||𝑥||.||𝑦||



## **DESARROLLO** :chart_with_upwards_trend: 

- **`ETL`**: :mag_right: <br>
 					desanidar campos  :white_check_mark: <br>
  					valores nulos a 0 :white_check_mark: <br>
					valores nulos eliminados :white_check_mark: <br>
					fechas a datetime :white_check_mark: <br>
					campo 'release_year' con año de estreno :white_check_mark: <br>
					crear columna de retorno de inversión :white_check_mark: <br>
					elimnar columnas que no se usarán :white_check_mark: <br>

- **`API`**: :computer: <br> 

:small_orange_diamond: **FUNCION 1:** se ingresa el mes y se retorna la cantidad de peliculas que se estrenaron ese mes históricamente.
> Nombre del mes, en español y minúscula: ejemplo: **`.com/peliculas_mes/enero`**<br><br>

:small_blue_diamond: **FUNCION 2:** se ingresa el dia y se retorna la cantidad de peliculas que se estrenaron ese dia históricamente.
> Se ingresa el nombre del dia, en español y minúscula: ejemplo: **`.com/peliculas_dia/lunes`**<br><br>

:small_orange_diamond: **FUNCION 3:** se ingresa la franquicia y se retorna la cantidad de peliculas, ganancia total y ganancia promedio.
> Se ingresa la franquicia con Mayúsculas: ejemplo: **`.com/franquicia/Toy Story Collection`**<br><br>

:small_blue_diamond: **FUNCION 4:** se ingresa el paīs y se retorna la cantidad de peliculas producidas por el mismo.
> Se ingresa el nombre del país en inglés con Mayúsculas: ejemplo: **`.com/peliculas_pais/United States of America`**<br><br>

:small_orange_diamond: **FUNCION 5:** se ingresa la productora y se retorna la ganancia total y la cantidad de peliculas producidas por el mismo.
> Se ingresa el nombre de la productora con Mayúsculas: ejemplo: **`.com/productoras/Pixar Animation Studio`**<br><br>

:small_blue_diamond: **FUNCION 6:** se ingresa la película y se retorna la inversión, ganancia,retorno y el año de lanzamiento de la película.
> Se ingresa el nombre original de la película: ejemplo: **`.com/retorno/Toy Story`** <br><br>

:green_square: **FUNCION 7 - ML:** se ingresa una película y se retornan 5 películas similares a modo de recomendación.
> Se ingresa el nombre original de la película: ejemplo: **`.com/recomendacion/The Dukes`** <br><br>

:interrobang:  **FUNCION TEST:** se ingresa una película y se retornan 5 películas similares a modo de recomendación, solo por gênero.
> Se ingresa el nombre original de la película: ejemplo: **`.com/recomendacionTEST/Avatar`** <br><br>


**`EDA`**: (Exploratory Data Analysis-EDA) :bar_chart: 

Usé *_pandas profiling*, para tener un resumen rápido y efectivo de los datos. Eliminé duplicados, nulos y corregí algunas categorías que tenían valores erroneos como 'popularity' o 'genres'. Decidí mantener para mi modelo las columnas: <br>
 + **'genres'** : es muy determinante ya que la escencia de como se cuenta una historia esta muy anclada en el género, dos peliculas pueden ser sobre una historia de amor, pero como la cuente una comedia a como la cuente un drama o una de terror seran muy diferentes.
 + **'overview'** : voy a usar la descripción para alimentar al algorítmo de la idea del film, de información sobre la trama y el tono.
+ **'tagline'**: junto con overview me pude ayudar a dar una descripcion mas detallada.
+ **'spoken_languages'**: puede ayudar a recomendar peliculas en el mismo idioma, considerando que la mayoria son de habla inglesa, si un usuario prefiere peliculas en italiano, el algoritmo podria predecir en su lista al menos una o dos peliculas en dicho idioma, tendre que imputar algunos datos desde el campo 'original_language'.
+ **'decades'**: discreticé esta variable desde 'relese_year' para que el algoritmo pueda darle mas peso a peliculas en relacion a su epoca, por ejemplo si busca peliculas clasicas.
+ **'popularity'**: puede ser un factor muy importante par evitar recomendar peliculas que no sean conocidas.
+ **'vote_average'**: la idea es que ayude a seleccionar peliculas populares y con buenas criticas.

<p align="center">
<img src="https://github.com/paupallares/PI_ML_OPS/blob/main/src/boceto.png"  height=400>
</p>

**`Sistema de recomendación`**: :vertical_traffic_light: 

El sistema consiste en recomendar películas a los usuarios basándose en películas similares, por lo que se debe encontrar la similitud de puntuación entre esa película y el resto de películas, se ordenarán según el score de similaridad y devolverá una lista de Python con 5 valores, cada uno siendo el string del nombre de las películas con mayor puntaje, en orden descendente. Las decisiones que tomé a la hora de construirlo están explicadas arriba en ***Decisiones tomadas***

El modelo responde muy bien, con recomendaciones que aparentemente son muy idóneas. Ejemplos:

<p align="center">
<img src="https://github.com/paupallares/PI_ML_OPS/blob/main/src/ejemplos.png"  height=400>
</p>

<br/>

**`Deployment`**: Realizado con [Render](https://render.com/docs/free#free-web-services), se puede acceder por este link: <a href="https://pi-ml-ops-3gcr.onrender.com/">Proyecto deployado</a>

Lamentablemente render.com limita el uso de memoria RAM para suscripciones gratuitas :sleepy:  por lo que la recomendación en la API se hace con un dataset reducido. Puede pasar que la pelicula que quieran consultar no se encuentre en ese dataset. Pueden buscarla en la consulta recomendacionTEST pero esa consulta no evalua similaritud con un algorítmo de ML sino solo arroja los primeros 5 registros que coinciden con el género de la película ingresada. 

<sub> Alguna películas presentes en el dataset reducido son: 'The Dukes', 'Dollman', 'Tom and Huck'. </sub>

<br/>

**`Video`**: :rocket:  

https://youtu.be/OHSTXRbtsqA

<br/>

####   <h2 id="tools" style="text-align: center;">HERRAMIENTAS USADAS :books:</h2>  

<p align="center">
<img src="https://github.com/paupallares/PI_ML_OPS/blob/main/src/librerias.png"  height=300>
</p>

   
## <p align=center> :star_struck: MUCHAS GRACIAS :hugs: 

<li><a href="https://www.linkedin.com/in/paupallares/">Linkedin</a></li>
