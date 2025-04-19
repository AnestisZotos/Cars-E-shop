from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson import ObjectId

app = Flask(__name__)
CORS(app)

app.config["MONGO_URI"] = "mongodb://mongo:27017/cars_eshop"

try:
    mongo = PyMongo(app)
    print("MongoDB client initialized")
    
    mongo.db.command('ping')
    print("Successfully connected to MongoDB!")
    
    mongo.db.products.create_index([("name", "text")])
    print("Text index created successfully!")
except Exception as e:
    print(f"Error connecting to MongoDB: {str(e)}")
    raise

@app.route('/search', methods=['GET'])
def search_products():
    search_term = request.args.get('name', '')
    
    if not search_term:
        products = list(mongo.db.products.find().sort("price", -1))
    else:
        products = list(mongo.db.products.find(
            {"$text": {"$search": search_term}}
        ).sort("price", -1))
    
    for product in products:
        product['_id'] = str(product['_id'])
    
    return jsonify(products)

@app.route('/like', methods=['POST'])
def like_product():
    product_id = request.json.get('id')
    
    if not product_id:
        return jsonify({"error": "Product ID is required"}), 400
    
    try:
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
    products = list(mongo.db.products.find().sort("likes", -1).limit(5))
    
    for product in products:
        product['_id'] = str(product['_id'])
    
    return jsonify(products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)