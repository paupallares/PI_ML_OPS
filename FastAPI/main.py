from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Libro(BaseModel):
    titulo: str
    autor: str
    paginas: int
    editorial: str
    
#http://127.0.0.1:8000

#decoradores:
@app.get('/')
def index():
    return {"saludo" : 'hola hola carabola'}

@app.get("/libros/{id}")
def mostrarlibro(id : int):
    return {"data": id}
