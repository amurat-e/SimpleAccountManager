import argparse
import psycopg2
import connect_db
import global_
import sys
from pathlib import Path


# Global vars from global_.py
glb = global_.vars()
dbconf = glb.dbconf
key = glb.key


def get_user(actid):
        global dbconf
        db = connect_db.db(dbconf)
        conn, cur = db.connect()
        try: 
            
            sql_text = "SELECT a.act_id, a.act_name, a.act_type, a.act_username, a.act_url, a.act_email, a.act_exp, pgp_sym_decrypt(b.psw_data, '" + key +"') as pswd FROM public.accounts a, public.passwords b WHERE b.act_id=a.act_id AND a.act_id = " + actid + ";"
	        # execute a statement
            cur.execute(sql_text)
            row = cur.fetchone()
            # close the communication with the PostgreSQL
            cur.close()
            return (row)
        except (Exception, psycopg2.DatabaseError) as error:
                print(error)
        finally:
                if conn is not None:
                    conn.close()

def update_user(actid,actname,acttype,actusrn,acturl,acteml,actexpl,actpswd):
    global dbconf
    db = connect_db.db(dbconf)
    conn, cur = db.connect()
    msg = ">" 
    try: 
        cur.execute('SELECT public.update_account_table (%s,%s,%s,%s,%s,%s,%s,%s,%s)',(actid,actname,acttype,actusrn,acturl,acteml,actexpl,actpswd,key))
        message = cur.statusmessage
        # close the communication with the PostgreSQL
        cur.close()
        conn.commit()
        return (msg + message)
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    finally:
            if conn is not None:
                conn.close()
                
def delete_user(actid):
    global dbconf
    db = connect_db.db(dbconf)
    conn, cur = db.connect()
    msg = ">" 
    try: 
        sql_text = "SELECT COUNT(act_id) as cnt FROM public.accounts WHERE act_id = " + actid + ";" 
        cur.execute(sql_text)
        row = cur.fetchone();
        if row[0] == 0:
            message = "Account ID:" + str(actid) + " Record Not Found."
        else:
            cur.execute('SELECT public.delete_account_table (%s)',(actid,))
            message = cur.statusmessage
            # close the communication with the PostgreSQL
        cur.close()
        conn.commit()
        return (message)
    except (Exception, psycopg2.DatabaseError) as error:
            print("Hata :",error)
    finally:
            if conn is not None:
                conn.close()

# Below function runs command line mode with argunent -f, --file file_name
# Calls public.insert_account_table function which inserts records tables of account
def main():
    # Initialize parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--delete", type=int, help = "Record ID.")
       
    # Read arguments from command line
    cargs = parser.parse_args()
    
    if cargs.delete:
       actid = str(cargs.delete)
       msg = "*"
       msg = delete_user(actid)
       print ("Delete : %s > %s" % (actid,msg))
    
        #sys.exit()

if __name__ == "__main__":
    main()
