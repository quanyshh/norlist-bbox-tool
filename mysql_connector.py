""" Module for remote access to mysql.


"""
import pandas as pd
import pymysql
from sshtunnel import SSHTunnelForwarder

def _read_config():
    with open("mysql.config", "r") as f:
        config = f.readlines()

    clean_config = [c.replace(' ', '').replace('\n', '').split('=') for c in config]
    keys = [k[0] for k in clean_config]
    values = [v[1].replace('\"', '') for v in clean_config]
    config_dict = dict(zip(keys, values))

    return config_dict

def remote_query(sql_query, typeOp="select"):

    rows = ""
    config_dict = _read_config()

    if typeOp == "select":
        with SSHTunnelForwarder((config_dict['ssh_host'], int(config_dict['ssh_port'])), 
        ssh_username=config_dict['ssh_user'], ssh_password=config_dict['mypkey'],
        remote_bind_address=(config_dict['sql_hostname'], int(config_dict['sql_port']))) as tunnel:

            connection_object = pymysql.connect(host='127.0.0.1', 
            user=config_dict['sql_username'], passwd=config_dict['sql_password'], 
            db=config_dict['sql_main_database'], port=tunnel.local_bind_port, cursorclass=pymysql.cursors.DictCursor)

            try:
                cursor_object = connection_object.cursor()
                cursor_object.execute(sql_query)

                # connection_object.commit()
                rows = cursor_object.fetchall()
            except Exception as e:
                print(f"Exception occured: {e}")
            finally:
                cursor_object.close()
                connection_object.close()
                
        return rows

    else:
        return rows
