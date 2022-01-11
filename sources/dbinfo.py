import psycopg2
import argparse
import connect_db
import global_

# Global vars from global_.py
glb = global_.vars()
dbconf = glb.dbconf
key = glb.key
def getinf():
        global dbconf
        db = connect_db.db(dbconf)
        conn, cur = db.connect()
        
        try: 
            sql_text = "SELECT substr(substr(version(), strpos(version(), \'P\')), 1, strpos(substr(version(), strpos(version(), \'P\')),\', compiled by\')-1) as OS, \
            CURRENT_USER usr,inet_server_addr() host,inet_server_port() port, current_database() dbname"
            #print('PostgreSQL database version:')
            cur.execute (sql_text)
            # display the PostgreSQL database server version
            db_version = cur.fetchone()
            # close the communication with the PostgreSQL
            cur.close()
            # print(db_version)
            text =  str(db_version)
            return (text[1:-1])
        except (Exception, psycopg2.DatabaseError) as error:
            return (error)
        finally:
            if conn is not None:
                conn.close()

def main():
    txt = getinf()
    print (txt)
if __name__ == "__main__":
    main()