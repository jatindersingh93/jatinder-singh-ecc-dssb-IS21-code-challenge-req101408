# Products at ECC - RESTFUL API


## Description
This Microservice provide RESTfull apis for products at ECC

## Stack Used
Python 3.6.5
Django==3.1.12
djongo==1.3.6
MongoDB - V4 and up - installed locally or in Docker

## Local installation
Make sure above Stack is avaiable on the machine for local installation

- update databse name, host, port in product/setting.py
- Create local python enviornment using virtualenv
- run following command to install requirments
```
```
    pip install -r requirements.txt
```
```
- Migrate Database - if not already set (this will create an empty database)
```
```
    python manage.py migrate
```
```
- Import initial data available under mongo-see/init.json to pro.productApi_product


## Docker Installation
App (Django and mongodb)can be installed using foolowing docker commands and is available at http://localhost:3000/api/products
```
```
docker-compose build --no-cache
docker-compose up
```
```

## End points
Swagger
http://localhost:3000/doc/

List all prodcuts
http://localhost:3000/api/products

Display full information about a product
http://localhost:3000/api/products/<key>


