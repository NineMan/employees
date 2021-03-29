FROM mongo

COPY employees.json /employees.json
CMD mongoimport --host mongodb --db employees    --collection employees_collection --type json --file employees.json --jsonArray