
We will need to go to off prem database immediately as work across nodes will get too confusing if main laptop is db


went with postgres so that we have access to postgist

be sure to set db to Publicly Accessible = Yes so that it can be accessed remotely

#TODO Figure out security group for database so that all nodes can write to db.
--> public access to postgress db with password https://stackoverflow.com/questions/52324170/aws-rds-for-postgresql-cannot-be-connected-after-several-hours/52346331#52346331

add postgist to the postgres db
--> already present, but need to CREATE EXTENSION postgis;
--> SELECT PostGIS_Full_Version();