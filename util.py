
import pandas as pd
#from mysql import connector as mc
#from mysql.connector import errorcode as ec
from config import DB_DETAILS
import psycopg2



# get database details
def load_db_details():
    db_details = DB_DETAILS
    return db_details


# postgres database connection

# mysql database connection


def mysql_db_connection(db_host, db_name, db_user, db_pass):
    try:
        connection = mc.connect(user=db_user,
                                password=db_pass,
                                host=db_host,
                                database=db_name
                                )
    except mc.Error as error:
        if error.errno == ec.ER_ACCESS_DENIED_ERROR:
            print("INVAILED CREDENTIALS")
        else:
            print(error)
    return connection

# postgres database connection


def pg_db_connection(db_host, db_name, db_user, db_pass):
    connection = psycopg2.connect(user=db_user,
                                  password=db_pass,
                                  host=db_host,
                                  dbname=db_name
                                  )
    return connection

#conn = psycopg2.connect("host='localhost' dbname='terp' user='postgres' password='123@Ht'")
#cur = conn.cursor()


def pg_connection():
    connection = psycopg2.connect(
        "host='localhost' dbname='terp' user='postgres' password='123@Ht'")
    return connection

# get connection API


def get_connection(db_type, db_host, db_name, db_user, db_pass):
    connection = None
    if db_type == 'postgres':
        connection = pg_db_connection(db_user=db_user,
                                      db_pass=db_pass,
                                      db_host=db_host,
                                      db_name=db_name
                                      )
    return connection
# list of tables to be loaded


def get_tables(path):
    tables = pd.read_csv(path, sep=':')
    return tables.query('to_be_loaded =="YES"')
