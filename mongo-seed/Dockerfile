FROM mongo

COPY init.json /init.json
CMD mongoimport --host mongodb --db pro --collection productAPI_product --type json --file /init.json --jsonArray