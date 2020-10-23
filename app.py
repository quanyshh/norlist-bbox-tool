from flask import Flask, request, render_template, jsonify
import mysql.connector
from sshtunnel import SSHTunnelForwarder
import pymysql
import pandas as pd

app = Flask(__name__, static_folder='static/')


sql_hostname = 'localhost'
sql_username = 'root'
sql_password = 'P@ssw0rd2020'
sql_main_database = 'users'
sql_port = 3306
ssh_host = '172.16.3.62'
ssh_user = 'g.abdimanap'
mypkey = 'FOURWORDS'
ssh_port = 22
sql_ip = '1.1.1.1.1'
def conn(sql_query):
    with SSHTunnelForwarder(
            (ssh_host, ssh_port),
            ssh_username=ssh_user,
            ssh_password=mypkey,
            remote_bind_address=(sql_hostname, sql_port)) as tunnel:
        conn = pymysql.connect(host='127.0.0.1', user=sql_username,
                passwd=sql_password, db=sql_main_database,
                port=tunnel.local_bind_port)

        
        data = pd.read_sql_query(sql_query, conn)
        conn.close()
    return data
    #conn.close()


var_on_server = [1,2,3,4,5,6]
#Hello
sql = "select * from users_last_image;"
# val = (user['first_name'], user['last_name'], user['id'], user_last_word, user['username'], user['id'], user_last_word)
data = conn('select * from users_last_image;')
# users_list=[]
# for user in data['user_name']:
    # print(user)


filename = 'Dataset_qazaq_words_05102020/417/words/417_018_004.jpg'
annotator_id = '398822459'
annotation1 = 'заттай'

annotator_id2 = '537619641'
annotation2 = 'заттай'


@app.route('/')
def index():
    """Return the main page."""
    print('index print statement here')
    return render_template('index.html', var_from_server=var_on_server, filename=filename, annotation1=annotation1, annotation2=annotation2, users = data['user_name'])


@app.route('/increment_on_server', methods=['GET', 'POST'])
def increment_on_server():
    """Receieve number from browser, add one and return it."""

    print('increment_on_server print statement here')

    data = request.json
    try:
        new_number = 1 + int(data['package_to_server'])
        return str(new_number)
    except ValueError:
        return 'Please Input A Valid Number'
