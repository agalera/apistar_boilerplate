from settings import MONGODB

from mongoengine import connect

print("connect db", MONGODB)
DB = connect(**MONGODB)
