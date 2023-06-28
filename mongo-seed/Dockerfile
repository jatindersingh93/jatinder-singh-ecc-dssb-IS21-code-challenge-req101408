FROM mongo

#COPY /dump /dump
#CMD mongorestore --host mongodb --db pro /dump --drop
COPY init_export.json /init_export.json
CMD mongorestore --host mongodb --db pro /init_export.json