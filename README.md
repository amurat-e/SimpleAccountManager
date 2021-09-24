# Simple Account Manager
## Simple account wallet program
Simple Account Manager application manges your account informations.
You can store your username / website info / e-mail info with notes and their passwords.
The password fields also stores in with encrypted data in database.

App Types: bash, Python 3.7
Last Update: 20/09/2021
Writen by A. Murat Ergin

## Features
| command        | Feature 
| -------        | ------- 
|acc_main_gui.py | Simple account wallet program main GUI. It lists accounts informations via partial (%partial%) or full of account name
|acc_ew_gui.py   | Enters New account entry
|acc_cdw_gui.py  | Changes accounts fields with using account id
|acc_help_gui.py | Shows help screen accounts Simple Account Manager
|global_.py      | Calls from all modules for global variables which are database init file, encrypt, decrypt key, etc.

| command      | parametrs       | Feature
| -------      | --------------- | -------
|getuser.py    |-a account_name  |Lists accounts entries with given partial (%partial%) or full of account name
|enteruser.py  |-f file_name     |Loads bulk accounts entry from given file. It also calls from acc_ew_gui.py for single entry
|chgdeluser.py |-d account_id    |Delete an accounts with given account id. It also calls from acc_cdw_gui.py for change a record

## Tech
/usr/bin/bash 
PostgreSQL 12.7 or above
python 3 or above
Execute (UNIX)

## Files
- **/accounts**
**/accounts/config**
 db.ini
**/accounts/data**
txtfile.txt
**/accounts/dba**
account_act_id_seq.sql
accounts.sql
delete_account_table.sql
generic_role.sql
genuser.sql
insert_account_table.sql
passwords.sql
passwords_psw_id_seq.sql
update_account_table.sql
**/accounts/sources**
acc_cdw_gui.py
acc_ew_gui.py
acc_main_gui.py
chgdeluser.py
connect_db.py
entuser.py
getdbv.py
getuser.py
global_.py

## Installation
Assumed you installed and running
- python 3.x 
- postgresql 12.x and create default database postgres
```sh
$ /usr/local/bin/python --version
Python 3.x
```
Install the dependencies.
postgresql driver for python
```sh
$ pip install psycopg2-binary
```
Downloads file 'accounts.tar.gz'
Extract files 
```sh
$ tar -xvf accounts.tar.gz
```
For database initialisation...

```sh
postgres$ createdb -h localhost -p 5432 -U postgres  -E UTF8 postgres
Creates postgres database ENCODING = 'UTF8' OWNER = postgres
```
```sh
postgres$ psql -d postgres -U postgres -f dba/extension_pgcrypto.sql
Creates 'pgcrypto' extension. It calls for encrypt decrypt proccess 
```
```sh
postgres$ psql -d postgres -U postgres -f dba/generic_role.sql
Creates 'generic_role' 
```
```sh
postgres$ psql -d postgres -U postgres -f dba/genuser.sql
Creates 'genuser' that is using for application connets database
```
```sh
postgres$ psql -d postgres -U postgres -f dba/accounts.sql
Creates 'public.accounts' table
```
```sh
postgres$ psql -d postgres -U postgres -f dba/account_act_id_seq.sql
Creates automatic sequence of 'public.accounts.act_id'
```
```sh
postgres$ psql -d postgres -U postgres -f dba/passwords.sql
Creates 'public.passwords' table
```
```sh
postgres$ psql -d postgres -U postgres -f dba/passwords_psw_id_seq.sql
Creates automatic sequence of 'public.passwords.psw_id'
```
```sh
postgres$ psql -d postgres -U postgres -f dba/delete_account_table.sql
Creates function for delete a recod from tables 'public.accounts' then 'public.passwords'
```
```sh
postgres$ psql -d postgres -U postgres -f dba/insert_account_table.sql
Creates function for insert a recod in to tables 'public.accounts' then 'public.passwords'
```
```sh
postgres$ psql -d postgres -U postgres -f dba/update_account_table.sql
Creates function for update a recod from tables 'public.accounts' and/or 'public.passwords'
```
Change host, username, password values in file config/db.ini for database connection 
> Note: Change **key** value that you prefer in file sources/global_.py. 
It uses password encrypt, decrypt
You can't change after insert any record in to database.

Load sample data from data/txtfile.txt for initialise
```sh
accounts/sources $ python entuser.py -f ../data/txtfile.txt
```
Run main GUI app.
```sh
accounts/sources $ python acc_main_gui.py
```


