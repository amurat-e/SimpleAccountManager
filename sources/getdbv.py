import psycopg2
import global_
import connect_db

glb = global_.vars()
dbconf = glb.dbconf

def get_dbv():
        global dbconf
        db = connect_db.db(dbconf)
        conn, cur = db.connect()
        try: 
            
	        # execute a statement
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


if __name__ == '__main__':
    txt = get_dbv()
    print(txt)