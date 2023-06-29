# Products at ECC - RESTFUL API


## Description
This App provides RESTfull APIs for products at ECC

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
    pip install -r requirements.txt
```
- Migrate Database - if not already set (this will create an empty database)
```
    python manage.py migrate
```
- Import initial data available under mongo-see/init.json to pro.productApi_product


## Docker Installation
App (Django and mongodb) can be installed using following docker commands and is available at http://localhost:3000/api/products
This should provide two container, one for APP and another for mongo db.
Data will be pre-populated from mongo-seed/dump using mongorestore
```
docker-compose build --no-cache
```
```
docker-compose up
```

## End points
Swagger
http://localhost:3000/doc/

List all prodcuts
http://localhost:3000/api/products

Display full information about a product
http://localhost:3000/api/products/<key>


## IMPORTANT INSTRUCTIONS

Keep Developer names in array when making an edit else it will break the format, this is a temp solution and needs to be modified.
![Screen Shot 2023-06-28 at 6 43 34 PM](https://github.com/jatindersingh93/jatinder-singh-ecc-dssb-IS21-code-challenge-req101408/assets/8764259/ba0025ce-51ac-482e-9a50-c49f03fbf5ef)

When you add new project, make sure to add multiple developer names sepeated by comma:


![Screen Shot 2023-06-28 at 6 44 51 PM](https://github.com/jatindersingh93/jatinder-singh-ecc-dssb-IS21-code-challenge-req101408/assets/8764259/ff1b24a2-f2e1-4810-9e0c-824bfc024e5a)

