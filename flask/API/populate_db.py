from pymongo import MongoClient

client = MongoClient("mongodb://mongo:27017/")
db = client.cars_eshop

cars = [
    {
        "name": "Suzuki Jimmy",
        "image": "http://localhost:8080/images/jimmy.png",
        "description": "Compact off-road SUV",
        "price": 22999,
        "likes": 0
    },
    {
        "name": "Suzuki Vitara",
        "image": "http://localhost:8080/images/vitara.png",
        "description": "Efficient crossover",
        "price": 25999,
        "likes": 0
    },
    {
        "name": "Suzuki Swift",
        "image": "http://localhost:8080/images/swift.png",
        "description": "Sporty city car",
        "price": 18999,
        "likes": 0
    },
    {
        "name": "Mini Cooper",
        "image": "http://localhost:8080/images/minicooper.png",
        "description": "Iconic premium hatch",
        "price": 30999,
        "likes": 0
    },
    {
        "name": "Peugeot 208",
        "image": "http://localhost:8080/images/208.png",
        "description": "Elegant city car",
        "price": 20999,
        "likes": 0
    },
    {
        "name": "Peugeot 308",
        "image": "http://localhost:8080/images/308.png",
        "description": "Tech-savvy hatchback",
        "price": 26999,
        "likes": 0
    },
    {
        "name": "Peugeot 3008",
        "image": "http://localhost:8080/images/3008.png",
        "description": "Spacious luxury SUV",
        "price": 32999,
        "likes": 0
    },
    {
        "name": "Peugeot 2008",
        "image": "http://localhost:8080/images/2008.png",
        "description": "Compact SUV",
        "price": 24999,
        "likes": 0
    },
    {
        "name": "Toyota Yaris",
        "image": "http://localhost:8080/images/yaris.png",
        "description": "Hybrid city car",
        "price": 21999,
        "likes": 0
    },
    {
        "name": "Nissan Qashqai",
        "image": "http://localhost:8080/images/qashqai.png",
        "description": "Safe family SUV",
        "price": 27999,
        "likes": 0
    },
    {
        "name": "Toyota Prius",
        "image": "http://localhost:8080/images/prius.png",
        "description": "Efficient hybrid",
        "price": 25999,
        "likes": 0
    },
    {
        "name": "Nissan Micra",
        "image": "http://localhost:8080/images/micra.png",
        "description": "Modern city car",
        "price": 17999,
        "likes": 0
    },
    {
        "name": "Renault Megane",
        "image": "http://localhost:8080/images/megane.png",
        "description": "Stylish hatchback",
        "price": 23999,
        "likes": 0
    },
    {
        "name": "Daewoo Matiz",
        "image": "http://localhost:8080/images/matiz.png",
        "description": "Urban compact",
        "price": 14999,
        "likes": 0
    },
    {
        "name": "Hyundai i30",
        "image": "http://localhost:8080/images/i30.png",
        "description": "Modern hatchback",
        "price": 22999,
        "likes": 0
    },
    {
        "name": "Hyundai i20",
        "image": "http://localhost:8080/images/i20.png",
        "description": "Value hatchback",
        "price": 18999,
        "likes": 0
    },
    {
        "name": "Hyundai i10",
        "image": "http://localhost:8080/images/i10.png",
        "description": "Compact city car",
        "price": 15999,
        "likes": 0
    },
    {
        "name": "Renault Clio",
        "image": "http://localhost:8080/images/clio.png",
        "description": "Popular supermini",
        "price": 19999,
        "likes": 0
    },
    {
        "name": "Honda Civic",
        "image": "http://localhost:8080/images/civic.png",
        "description": "Sporty sedan",
        "price": 24999,
        "likes": 0
    },
    {
        "name": "Toyota Auris",
        "image": "http://localhost:8080/images/auris.png",
        "description": "Hybrid hatchback",
        "price": 22999,
        "likes": 0
    }
]

db.products.delete_many({})

result = db.products.insert_many(cars)
print(f"Inserted {len(result.inserted_ids)} cars into the database")

db.products.create_index([("name", "text")])
print("Text index created successfully")

client.close()