from fastapi import FastAPI
import pandas as pd
from fastapi.responses import HTMLResponse #Utilizado para generar el formato de texto de la pagina de inicio
import numpy as np 

meses_es = {
    'January': 'enero',
    'February': 'febrero',
    'March': 'marzo',
    'April': 'abril',
    'May': 'mayo',
    'June': 'junio',
    'July': 'julio',
    'August': 'agosto',
    'September': 'septiembre',
    'October': 'octubre',
    'November': 'noviembre',
    'December': 'diciembre'
}

semana_es = {
    'Monday': 'lunes',
    'Tuesday': 'martes',
    'Wednesday': 'miercoles',
    'Thursday': 'jueves',
    'Friday': 'viernes',
    'Saturday': 'sabado',
    'Sunday': 'domingo',
}

app = FastAPI()

df = pd.read_csv('/Users/ssanjua/Desktop/HENRY 2023/DataScience/DATAFT10/LABS/PI MLs/PI_ML_OPS_pau/Datasets/dataset_limpio_v2.csv')
df['release_date'] = pd.to_datetime(df['release_date'], format='%Y-%m-%d')
df['month_release'] = df['release_date'].apply(lambda x: meses_es[x.strftime('%B')])
df['day_of_week_release'] = df['release_date'].apply(lambda x: semana_es[x.strftime('%A')])


#Creamos un directorio index con mensaje de bienvenida
@app.get("/", response_class=HTMLResponse)
async def welcome():
    message = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>API de Consultas de Películas</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                color: #333;
            }

            h1 {
                font-size: 28px;
                color: #007bff;
            }

            p {
                font-size: 20px;
            }

            ol li {
                font-size: 18px;
            }
        </style>
    </head>
    <body>
        <h1>¡Bienvenido a la interfaz de consultas de películas!</h1>
        <p><b>Se pueden realizar 7 tipos de consultas:</b></p>
        <ol>
            <li style="margin-bottom: 10px;"><b>Consulta 1:</b> Se ingresa el <b><i>mes</b></i> y se retorna la <b><i>cantidad de peliculas</b></i> que se estrenaron ese mes históricamente.<br>> Se ingresa el nombre del mes, en español y minúscula: ejemplo <b>'/enero'</b> </li>
            <li style="margin-bottom: 10px;"><b>Consulta 2:</b>Se ingresa el <b><i>dia</b></i> y se retorna la <b><i>cantidad de peliculas</b></i> que se estrenaron ese dia históricamente.<br>> Se ingresa el nombre del dia, en español y minúscula: ejemplo <b>'/lunes'</b> </li>
            <li style="margin-bottom: 10px;"><b>Consulta 3:</b>Se ingresa la <b><i>franquicia</b></i> y se retorna la <b><i>cantidad de peliculas</b></i>, <b><i>ganancia total</b></i> y <b><i>ganancia promedio</b></i>. <br>> Se ingresa la franquicia con Mayúsculas: ejemplo <b>'/Toy Story Collection'</b>  </li>
            <li style="margin-bottom: 10px;"><b>Consulta 4:</b>Se ingresa el <b><i>paīs</b></i> y se retorna la <b><i>cantidad de peliculas</b></i> producidas por el mismo. <br>> Se ingresa el nombre del país en inglés con Mayúsculas: ejemplo <b>'/United States of America'</b>  </li>
            <li style="margin-bottom: 10px;"><b>Consulta 5:</b>Se ingresa la <b><i>productora</b></i> y se retorna la <b><i>ganancia total</b></i> y la <b><i>cantidad de peliculas</b></i> producidas por el mismo. <br>> Se ingresa el nombre de la productora con Mayúsculas: ejemplo <b>'/Pixar Animation Studios'</b>  </li>
            <li style="margin-bottom: 10px;"><b>Consulta 6:</b>Se ingresa la <b><i>película</b></i> y se retorna la <b><i>inversión</b></i>, <b><i>ganancia</b></i>,<b><i>retorno</b></i> y el <b><i>año de lanzamiento</b></i> de la película. <br>> Se ingresa el nombre original de la película: ejemplo <b>'/Toy Story'</b>  </li>
            <li style="margin-bottom: 10px;"><b>Consulta 6:</b>Se ingresa una <b><i>película</b></i> y se retornan <b><i>5 películas</b></i> similares a modo de <i>recomendación</i>. <br>> Se ingresa el nombre original de la película: ejemplo <b>'/Toy Story'</b>  </li>
        </ol>
        <p>Para saber cómo buscar y acceder a los datos, leer el archivo README.md donde se encontrará toda la info necesaria.</p>
    </body>
    </html>
    """
    return message
#http://127.0.0.1:8000

@app.get('/peliculas_mes/{mes}')
def peliculas_mes(mes:str):
    '''Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron ese mes historicamente'''
    df_mes = df[df['month_release'] == mes]
    if df_mes.empty:
        return {'error': 'El programa acepta los mes en español solo en minúscula, ejemplo: enero.'}
    cantidad = len(df_mes)
    
    return {'mes': mes, 'cantidad': cantidad}

@app.get('/peliculas_dia/{dia}')
def peliculas_dia(dia:str):
    '''Se ingresa el dia y la funcion retorna la cantidad de peliculas que se estrebaron ese dia historicamente'''
    df_dia = df[df['day_of_week_release'] == dia]
    if df_dia.empty:
        return {'error': 'El programa acepta los días en español solo en minúscula, ejemplo: lunes.'}
    cantidad = len(df_dia)
    
    return {'dia': dia, 'cantidad': cantidad}

@app.get('/franquicia/{franquicia}')
def franquicia(franquicia:str):
    '''Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio'''
    franquicia_df = df[df['belongs_to_collection'] == franquicia]
    if franquicia_df.empty:
        return {'error': 'La franquicia no se encuentra en el DataFrame o está mal escrita. Acordate de usar Mayusculas buscar los nombres'}
    cantidad = len(franquicia_df)
    ganancia_total = franquicia_df['revenue'].sum()
    ganancia_promedio = franquicia_df['revenue'].mean() if cantidad > 0 else 0
    
    return {'franquicia': franquicia, 'cantidad': cantidad, 'ganancia_total': ganancia_total, 'ganancia_promedio': ganancia_promedio}

@app.get('/productoras/{productora}')
def productoras(productora:str):
    '''Ingresas la productora, retornando la ganancia toal y la cantidad de peliculas que produjeron'''
    productora_df = df[df['production_companies'].notna() & df['production_companies'].str.contains(productora)]
    if productora_df.empty:
        return {'error': 'La productora no está en el DataFrame. Acordate de usar Mayusculas buscar los nombres'}
    ganancia_total = productora_df['revenue'].sum()
    cantidad = len(productora_df)
    
    return {'productora': productora, 'ganancia_total': ganancia_total, 'cantidad': cantidad}

@app.get('/retorno/{pelicula}')
def retorno(pelicula:str):
    '''Ingresas la pelicula, retornando la inversion, la ganancia, el retorno y 
    el año en el que se lanzo'''
    pelicula_df = df[df['title'] == pelicula]
    if pelicula_df.empty:
        return {'error': 'La película no se encuentra en el DataFrame. Acordate de usar Mayusculas buscar los nombres'}
    inversion = pelicula_df['budget'].iloc[0]
    ganancia = pelicula_df['revenue'].iloc[0]
    retorno = pelicula_df['return'].iloc[0]
    anio = pelicula_df['release_date'].dt.strftime('%Y').iloc[0]

    return {'pelicula':pelicula, 'inversion':inversion, 'ganancia':ganancia,'retorno':retorno, 'anio':anio}

@app.get('/recomendacion/{titulo}')
def recomendacion(titulo:str): 
    '''Ingresas un nombre de pelicula y te recomienda las similares en una lista de 5 valores
        como es una funcion basica, los agrupe por genero, 
        la funcion devuelve una lista con las 5 primeras peliculas del genero que encuentra
    ''' 
    pelicula_fila = df[df['title'] == titulo]
    if pelicula_fila.empty:
        return {'error': 'La película no se encuentra en el DataFrame. Acordate de usar Mayusculas buscar los nombres'}
    genero = pelicula_fila['genres'].iloc[0]
    peliculas_relacionadas = df[df['genres'] == genero]['title'].tolist()
    peliculas_relacionadas.remove(titulo)  
    peliculas_recomendadas = peliculas_relacionadas[:5]

    return {'lista recomendada': peliculas_recomendadas}