from pymongo import MongoClient

client = MongoClient('localhost', 27017)

car_list = [
        {
            "command": "Hi"
        }
    ]

db = client.my_db
cars = db.cars
cars.insert_many(car_list)

#cars.delete_many({})

for data in cars.find():
    print(data)


