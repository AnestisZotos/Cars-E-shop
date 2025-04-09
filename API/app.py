from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
import os
from bson import ObjectId

app = Flask(__name__)
CORS(app)

# MongoDB configuration
app.config["MONGO_URI"] = "mongodb+srv://val-makkas:mTwJsN9grElylk3v@cars-e-shop.hwvqbpa.mongodb.net/car_shop?retryWrites=true&w=majority&appName=Cars-E-shop"

try:
    mongo = PyMongo(app)
    print("MongoDB client initialized")
    
    # Test the connection
    mongo.db.command('ping')
    print("Successfully connected to MongoDB!")
    
    # Create text index on name field
    mongo.db.products.create_index([("name", "text")])
    print("Text index created successfully!")
except Exception as e:
    print(f"Error connecting to MongoDB: {str(e)}")
    print(f"Connection URI: {app.config['MONGO_URI']}")
    raise

@app.route('/search', methods=['GET'])
def search_products():
    search_term = request.args.get('name', '')
    
    if not search_term:
        # Return all products sorted by price in descending order
        products = list(mongo.db.products.find().sort("price", -1))
    else:
        # Search for products containing the search term in their name
        products = list(mongo.db.products.find(
            {"$text": {"$search": search_term}}
        ).sort("price", -1))
    
    # Convert ObjectId to string for JSON serialization
    for product in products:
        product['_id'] = str(product['_id'])
    
    return jsonify(products)

@app.route('/like', methods=['POST'])
def like_product():
    product_id = request.json.get('id')
    
    if not product_id:
        return jsonify({"error": "Product ID is required"}), 400
    
    try:
        # Convert string ID to ObjectId
        product_id = ObjectId(product_id)
        
        result = mongo.db.products.update_one(
            {"_id": product_id},
            {"$inc": {"likes": 1}}
        )
        
        if result.modified_count == 0:
            return jsonify({"error": "Product not found"}), 404
        
        return jsonify({"message": "Like added successfully"})
    except Exception as e:
        return jsonify({"error": "Invalid product ID format"}), 400

@app.route('/popular-products', methods=['GET'])
def get_popular_products():
    # Get top 5 products sorted by likes in descending order
    products = list(mongo.db.products.find().sort("likes", -1).limit(5))
    
    # Convert ObjectId to string for JSON serialization
    for product in products:
        product['_id'] = str(product['_id'])
    
    return jsonify(products)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True) 