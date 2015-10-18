import sys
import MySQLdb


class DBhelper(object):

    def __init__(self):
        self.db = MySQLdb.connect(
            host="localhost",
            user="daniuk", 
            passwd="supersecret",  #change pass 
            db="ft")
    
    def create_cursor(self):
        #creates a cusror object that enables to execute queries
        self.cursor = self.db.cursor()
        return self.cursor

    def select_query(self, query): #to which class get this shit to?
        cursor = self.create_cursor()
        print "Query result:", str(cursor.execute(query)),"rows."
        # print all the cells of all the rows
        for row in cursor.fetchall() :
            print row

    def insert_one(self, rank, title,year):
        cursor = self.create_cursor()
        try:
            cursor.execute(
                """INSERT INTO imdb (rank, title, year) 
                VALUES (%s,%s,%s)""", (rank, title, year)
                )
            self.db.commit()
            print '1 row inserted'
        except Exception as e:
            print "exception: ", type(e), e
            self.db.rollback()

    def insert_many(self, data_list):
        for item in data_list:
            self.insert_one(item['Rank'],item['Title'],item['Year'])


        

