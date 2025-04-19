# run with docker
docker-compose build 

docker-compose up

# populate the db with data
docker exec -it cars-e-shop-flask-1 python /app/populate_db.py

# access the endpoints
access the Flask API at http://localhost:5000

access the website at http://localhost:8080
