from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Inicia el server: uvicorn users:app --reload

# Entidad user
class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int

users_list = [User(name="Carlos Javier", surname="Lozano", url="https://www.github.com/cjlozanoDev", age=36),
              User(name="Gloria", surname="Milagros", url="No tiene", age=34),
              User(name="Celia", surname="Lozano", url="No tiene", age=34)]


@app.get("/usersjson")
async def usersjson():
    return [
          {
            "name": "Carlos Javier", 
            "surname": "Lozano", 
            "url": "https://www.github.com/cjlozanoDev",
            "age": 36
          },
          {
            "name": "Gloria", 
            "surname": "Milagros", 
            "url": "No tiene",
            "age": 34
          },
          {
            "name": "Celia", 
            "surname": "Lozano", 
            "url": "No tiene",
            "age": 34
          }
    ]
@app.get("/users")
async def users():
    return users_list