import json
import os
import pymysql
from django.conf import settings

def get_connection(connection_config):
    try:
        connection_config_new = {
            'host': connection_config.get('HOST'),
            'database': connection_config.get('NAME'),
            'user': connection_config.get('USER'),
            'password': connection_config.get('PASSWORD'),
            'port': connection_config.get('POST')
        }
        connection = pymysql.connect(**connection_config_new)
        return connection
    except Exception as ex:
        print(f"Exception mysql connection initialization, {ex}")
        return None

def execute_select(connection_obj, query, where_clause):
    cursor = connection_obj.cursor()
    try:
        cursor.execute(query, where_clause)
        columns = cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
        cursor.close()
        return result
    except Exception as ex:
        print(f'Exception occured in execute_select, {ex}')
        return None

def execute_insert(connection_obj, table_name, parameters):
    curser=connection_obj.cursor()
    values = ', '.join(["%s"] * len(parameters["columns"]))
    columns = ', '.join(parameters["columns"])
    query = 'INSERT INTO %s ( %s ) VALUES ( %s )' % (table_name, columns, values)

    try:
        curser.executemany(query, parameters["values"])
        connection_obj.commit()
        connection_obj.close()
        curser.close()
        return curser.rowcount
    except Exception as ex:
        print(f'Exception occured in execute_insert, {ex}')
        return None

