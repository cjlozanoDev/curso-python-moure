from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Inicia el server: uvicorn users:app --reload

# Entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id=1, name="Carlos Javier", surname="Lozano", url="https://www.github.com/cjlozanoDev", age=36),
              User(id=2, name="Gloria", surname="Milagros", url="No tiene", age=34),
              User(id=3, name="Celia", surname="Lozano", url="No tiene", age=34)]


@router.get("/usersjson")
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

@router.get("/users")
async def users():
    return users_list

# Path
@router.get("/user/{id}")
async def user(id: int):
    return search_user(id)


# Query

@router.get("/userquery/")
async def user(id: int):
    return search_user(id)


@router.post("/user/", response_model=User, status_code=201)
async def user(user: User):
  if type(search_user(user.id)) == User:
    raise HTTPException(status_code=404, detail="El usuario ya existe")
  else:
    users_list.append(user)
    return user


@router.put("/user")
async def user(user: User):
  found = False

  for index, user_saved in enumerate(users_list):
    if (user_saved.id == user.id):
      users_list[index] = user
      found = True

  if not found: 
    return {"error": "No se ha encontrado el usuario"}    

  return user 


@router.delete("/user/{id}")
async def user(id: int):

  found = False

  for index, user_saved in enumerate(users_list):
    if (user_saved.id == id):
      del users_list[index]
      found = True

  if not found:
    return {"error": "No se ha eliminado el usuario"}



def search_user(id: int):
  users = filter(lambda user: user.id ==id, users_list)
  try: 
    return list(users)[0]
  except:
    return {"error": "No se ha encontrado el usuario"}





