from pymongo import MongoClient

# Base de datos local
# db_client = MongoClient().local

# Base de datos remota

# Base de datos remota
db_client = MongoClient("mongodb+srv://test:test@cluster0.litpg2y.mongodb.net/?retryWrites=true&w=majority").test