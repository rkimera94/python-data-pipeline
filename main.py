from flask import Flask
#from flask_restful import Api
import sys
#from config import DB_DETAILS
from util import get_tables, load_db_details
from read import read_table

# test env request


def main():
    #env = sys.argv[1]
    db_details = load_db_details()
    # print(db_details)
    tables = get_tables('table_list')
    # for table in tables['table_name']:
    # print(table)
    column_names = ('id','migration',)
    table_name = 'migrations'
    data = read_table(db_details, table_name)
    for rec in data:
        print(data)

if __name__ == "__main__":
    main()
# debug = true for test environments
