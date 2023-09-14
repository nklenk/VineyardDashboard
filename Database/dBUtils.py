import psycopg2


#TODO: move database information to a settings yaml

connectionInfo = "database='database-1', " \
                 "user='postgres', " \
                 "password='hopte6-xaktUs-dirjyd', " \
                 "host='database-1.cyjnrmeqg58a.us-east-2.rds.amazonaws.com', " \
                 "port='5432'"

# psql -U postgres -h database-1.cyjnrmeqg58a.us-east-2.rds.amazonaws.com -p 5432 -d database-1 --password

class DBUtils():

    def __init__(self, env):
        self.env = env
        # update to match current aws table
        self.connection = psycopg2.connect(connectionInfo)
        self.cursor = self.connection.cursor()

    def dbInsert(self, content):
        self.connection
        pass

    def execute(self, content):
        try:
            self.cursor.execute(content)
        except psycopg2.Error as e:
            pass
