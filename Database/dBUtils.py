import psycopg2

#TODO: move database information to a settings yaml

connectionInfo = "dbname='postgres', " \
                 "user='postgres', " \
                 "password='hopte6-xaktUs-dirjyd', " \
                 "host='database-1.cyjnrmeqg58a.us-east-2.rds.amazonaws.com', " \
                 "port='5432'"


# psql -U postgres -h database-1.cyjnrmeqg58a.us-east-2.rds.amazonaws.com -p 5432 -d database-1 --password

class DBUtils():

    def __init__(self):
        # update to match current aws table
        print("##")
        # print(connectionInfo)
        # self.connection = psycopg2.connect(connectionInfo)
        self.connection = psycopg2.connect(dbname="postgres", user="postgres", password="hopte6-xaktUs-dirjyd",
                                           host="database-1.cyjnrmeqg58a.us-east-2.rds.amazonaws.com", port="5432")
        print(self.connection)
        self.cursor = self.connection.cursor()

    def Insert(self, content):
        # self.connection
        print("Insert: {}".format(content))
        self.execute(content)
        self.connection.commit()
        pass

    def execute(self, content):
        try:
            print("query: {}".format(content))
            self.cursor.execute(content)
            self.connection.commit()
        except psycopg2.Error as e:
            print("Error: {}".format(e))
            pass

# dbutil = DBUtils(connectionInfo)
# dbutil.dbInsert(connectionInfo)
