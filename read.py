from util import get_connection

def read_table(db_details, table_name, limit=0):
    SOURCE_DB = db_details['source']
    connection = get_connection(db_type=SOURCE_DB['DB_TYPE'], db_host=SOURCE_DB['DB_HOST'],
                                db_name=SOURCE_DB['DB_NAME'],
                                db_user=SOURCE_DB['DB_USER'],
                                db_pass=SOURCE_DB['DB_PASS'])

    cursor = connection.cursor()
    if limit == 0:
        query = f'SELECT * FROM {table_name}'
    else:
        query = f'SELECT * FROM {table_name} LIMIT{limit}'
    cursor.execute(query)
    data = cursor.fetchall()
    #column_names =[dec[0] for dec in description]
    #column_names = cursor.Column
    connection.close()

    return data



