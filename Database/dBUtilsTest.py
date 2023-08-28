
import yaml
import psycopg2

with open('../Settings/settings.yml', 'r') as ymlFile:
    dbYaml = yaml.safe_load(ymlFile)['database']
    dbname = dbYaml['dbname']
    user = dbYaml['username']
    host = dbYaml['host']
    password = dbYaml['password']

connectionString = "dbname={} user={} host={} password={}".format(dbname, user, host, password)
print(connectionString)

try:
    conn = psycopg2.connect(connectionString)
except:
    print("I am unable to connect to the database")
