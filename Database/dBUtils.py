import psycopg2

#TODO: move database information to a settings yaml

connectionInfo = "database='database-1', " \
                 "user='postgres', " \
                 "password='hopte6-xaktUs-dirjyd', " \
                 "host='database-1.cyjnrmeqg58a.us-east-2.rds.amazonaws.com', " \
                 "port='5432'"


# psql -U postgres -h database-1.cyjnrmeqg58a.us-east-2.rds.amazonaws.com -p 5432 -d database-1 --password

class DBUtils():

    def __init__(self, connectionInfo):
        # connectionInfo = "database='database-1', " \
        #                  "user='postgres', " \
        #                  "password='hopte6-xaktUs-dirjyd', " \
        #                  "host='database-1.cyjnrmeqg58a.us-east-2.rds.amazonaws.com', " \
        #                  "port='5432'"
        # update to match current aws table
        print("##")
        print(connectionInfo)
        self.connection = psycopg2.connect(connectionInfo)
        print(self.connection)
        self.cursor = self.connection.cursor()

    def dbInsert(self, content):
        # self.connection
        print("Insert: {}".format(content))
        pass

    def execute(self, content):
        try:
            self.cursor.execute(content)
        except psycopg2.Error as e:
            print("Error: {}".format(e))
            pass

print("**")
print(connectionInfo)
dbutil = DBUtils(connectionInfo)
dbutil.dbInsert(connectionInfo)
