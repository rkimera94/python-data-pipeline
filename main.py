from flask import Flask
#from flask_restful import Api
import sys
#from config import DB_DETAILS
from util import get_tables, load_db_details
from read import read_table
from write import build_insert_query,load_table


# test env request


def main():
    #env = sys.argv[1]
    db_details = load_db_details()
    # print(db_details)
    tables = get_tables('table_list')
    # for table in tables['table_name']:
    # print(table)
    column_names = ('id','migration','batch')
    table_name = 'migrations'
    for table_name in tables['table_name']:
        print(f'reading data for loading {table_name}')
        data = read_table(db_details, table_name)
        print(build_insert_query(table_name,column_names))
        print(f'loading data for table {table_name}')
        load_table(db_details, data, column_names,table_name)

if __name__ == "__main__":
    main()
# debug = true for test environments
