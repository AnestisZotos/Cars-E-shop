from pymongo import MongoClient

MONGO_URI = "mongodb+srv://val-makkas:mTwJsN9grElylk3v@cars-e-shop.hwvqbpa.mongodb.net/car_shop?retryWrites=true&w=majority&appName=Cars-E-shop"

client = MongoClient(MONGO_URI)
db = client.car_shop

cars = [
    {
        "name": "Suzuki Jimmy",
        "image": "../Document/images/jimmy.png",
        "description": "Compact off-road SUV",
        "price": 22999,
        "likes": 0
    },
    {
        "name": "Suzuki Vitara",
        "image": "../Document/images/vitara.png",
        "description": "Efficient crossover",
        "price": 25999,
        "likes": 0
    },
    {
        "name": "Suzuki Swift",
        "image": "../Document/images/swift.png",
        "description": "Sporty city car",
        "price": 18999,
        "likes": 0
    },
    {
        "name": "Mini Cooper",
        "image": "../Document/images/minicooper.png",
        "description": "Iconic premium hatch",
        "price": 30999,
        "likes": 0
    },
    {
        "name": "Peugeot 208",
        "image": "../Document/images/208.png",
        "description": "Elegant city car",
        "price": 20999,
        "likes": 0
    },
    {
        "name": "Peugeot 308",
        "image": "../Document/images/308.png",
        "description": "Tech-savvy hatchback",
        "price": 26999,
        "likes": 0
    },
    {
        "name": "Peugeot 3008",
        "image": "../Document/images/3008.png",
        "description": "Spacious luxury SUV",
        "price": 32999,
        "likes": 0
    },
    {
        "name": "Peugeot 2008",
        "image": "../Document/images/2008.png",
        "description": "Compact SUV",
        "price": 24999,
        "likes": 0
    },
    {
        "name": "Toyota Yaris",
        "image": "../Document/images/yaris.png",
        "description": "Hybrid city car",
        "price": 21999,
        "likes": 0
    },
    {
        "name": "Nissan Qashqai",
        "image": "../Document/images/qashqai.png",
        "description": "Safe family SUV",
        "price": 27999,
        "likes": 0
    },
    {
        "name": "Toyota Prius",
        "image": "../Document/images/prius.png",
        "description": "Efficient hybrid",
        "price": 25999,
        "likes": 0
    },
    {
        "name": "Nissan Micra",
        "image": "../Document/images/micra.png",
        "description": "Modern city car",
        "price": 17999,
        "likes": 0
    },
    {
        "name": "Renault Megane",
        "image": "../Document/images/megane.png",
        "description": "Stylish hatchback",
        "price": 23999,
        "likes": 0
    },
    {
        "name": "Daewoo Matiz",
        "image": "../Document/images/matiz.png",
        "description": "Urban compact",
        "price": 14999,
        "likes": 0
    },
    {
        "name": "Hyundai i30",
        "image": "../Document/images/i30.png",
        "description": "Modern hatchback",
        "price": 22999,
        "likes": 0
    },
    {
        "name": "Hyundai i20",
        "image": "../Document/images/i20.png",
        "description": "Value hatchback",
        "price": 18999,
        "likes": 0
    },
    {
        "name": "Hyundai i10",
        "image": "../Document/images/i10.png",
        "description": "Compact city car",
        "price": 15999,
        "likes": 0
    },
    {
        "name": "Renault Clio",
        "image": "../Document/images/clio.png",
        "description": "Popular supermini",
        "price": 19999,
        "likes": 0
    },
    {
        "name": "Honda Civic",
        "image": "../Document/images/civic.png",
        "description": "Sporty sedan",
        "price": 24999,
        "likes": 0
    },
    {
        "name": "Toyota Auris",
        "image": "../Document/images/auris.png",
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