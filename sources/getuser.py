import psycopg2
import argparse
import connect_db
import global_

# Global vars from global_.py
glb = global_.vars()
dbconf = glb.dbconf
key = glb.key

def get_user(usrnm):
        global dbconf
        db = connect_db.db(dbconf)
        conn, cur = db.connect()
        rowss = list()
        try: 
            sql_text = "SELECT a.act_id, a.act_name, a.act_username, a.act_url, a.act_email, a.act_exp, pgp_sym_decrypt(b.psw_data, '" + key +"') as pswd FROM public.accounts a, public.passwords b WHERE b.act_id=a.act_id AND a.act_name LIKE '" + usrnm + "' ORDER BY a.act_id;"
	        # execute a statement
            #print (sql_text)
            cur.execute(sql_text)
            # display the PostgreSQL database server version
            rowss = cur.fetchall();
            # close the communication with the PostgreSQL
            cur.close()
            # print(db_version)
            return (rowss)
        except (Exception, psycopg2.DatabaseError) as error:
                print(error)
        finally:
                if conn is not None:
                    conn.close()

# Below function runs command line mode with argunent -a, --account account_namr
# Lists like %account_name%
def main():
    # Initialize parser
    parser = argparse.ArgumentParser()
    # Adding optional argument
    parser.add_argument("-a", "--account",  help = "full or partial  Account_name ")
    # Read arguments from command line
    args = parser.parse_args()
    accname = args.account
    if args.account:
        usera = "%"
        usera += accname + "%"
        rowss = get_user(usera)
        rrr = list()
        strr = "ID;HESAP ADI;KULLANICI;URL;E-POSTA;ACIKLAMA;SIFRE"
        rrr.append(strr)
        for row in rowss:
            strr = str(row[0])+";"+str(row[1])+";"+str(row[2])+";"+str(row[3])+";"+str(row[4])+";"+str(row[5])+";"+str(row[6])
            rrr.append(strr)
            
        for r in rrr:
            print(r)

if __name__ == '__main__':
    main()
    