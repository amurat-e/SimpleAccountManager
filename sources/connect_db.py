import psycopg2
import argparse
import configparser
import sys
from pathlib import Path
import global_

# Global vars from global_.py
glb = global_.vars()
dbconf = glb.dbconf

class db:
    
    global dbconf
    # fname = "db.ini"
    
    def __init__(self, dbconf):
        self.filename = dbconf
        self.connect() 
        
    def connect(self):
        # Initialize configparser
        config = configparser.ConfigParser()
        # Read sections and keys from ini file
        config.read(self.filename)
        host=config['postgresql']['host']
        user=config['postgresql']['user']
        passwd=config['postgresql']['passwd']
        db=config['postgresql']['db']
        # print ("Database parameters: %s %s %s %s" % (host,user,passwd,db))
        """ Connect to the PostgreSQL database server """
        conn = None
        try:
            conn = psycopg2.connect(host=host,database=db,user=user,password=passwd)
        # create a cursor
            cur = conn.cursor()
            return  conn, cur
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

def main():
   global dbconf
   dbc = db(dbconf)
   conn, cur = dbc.connect()
   try: 
        #print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        # close the communication with the PostgreSQL
        cur.close()
        # print(db_version)
        text = "> " + str(db_version)
        return (text)
   except (Exception, psycopg2.DatabaseError) as error:
            print(error)
   finally:
        if conn is not None:
            conn.close()
            print(text)


if __name__ == "__main__":
    main()
