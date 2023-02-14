from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:admin@container.qdz4bit.mongodb.net/?retryWrites=true&w=majority")
db = client.beerapp