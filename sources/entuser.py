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


def ent_user(actname,acttype,actusrn,acturl,acteml,actexpl,actpswd):
        global dbconf
        global key
        db = connect_db.db(dbconf)
        conn, cur = db.connect()
        
        msg = ">" 
        try: 
            cur.execute('SELECT public.insert_account_table (%s,%s,%s,%s,%s,%s,%s,%s)',(actname,acttype,actusrn,acturl,acteml,actexpl,actpswd,key))
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
                    #print('Database connection closed.')
def cmmnt_cnt(strline):
    for i in range(len(strline)):
         if strline.find("#",i,i+1) > -1:
             return True
    return False

# Below function runs command line mode with argunent -f, --file file_name
# Calls public.insert_account_table function which inserts records tables of account
def main():
    # Initialize parser
    parser = argparse.ArgumentParser()
    # Adding optional argument
    parser.add_argument("-f", "--file",  help = " file name")
    # Read arguments from command line
    args = parser.parse_args()
    filename = args.file
    if args.file:
        p=Path(filename)
        if p.is_file():
            print("Displaying input as: %s" %args.file)
            try: 
             # Path(filename) full path required
             # Reads as text file and splits text from EOL
             lines = Path(filename).read_text().splitlines()
             fields=[]
             for line in lines:
                strline = str(line)
                if cmmnt_cnt(strline):
                    pass
                else:
                     fields  = strline.split("|")
                     actname = fields[0] 
                     acttype = int(fields[1])
                     actusrn = None if fields[2] == "NULL" else fields[2]
                     acturl  = None if fields[3] == "NULL" else fields[3]
                     acteml  = None if fields[4] == "NULL" else fields[4]
                     actexpl = None if fields[5] == "NULL" else fields[5]
                     actpass = fields[6] 
                     print(actname, str(acttype), actusrn, acturl, acteml, actexpl, actpass)
                     msg = ent_user(actname, acttype, actusrn, acturl, acteml, actexpl, actpass)
                
            except FileNotFoundError:
                print ("File not found: %s" %filename)
                sys.exit()
        else:
            print("File not found: %s" %args.file)
            sys.exit()

if __name__ == "__main__":
    main()
