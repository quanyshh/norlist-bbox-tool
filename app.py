
"""

Tool to validate handwritten dataset

Copyright (c) 2020 NORLIST.kz
Written by Kuanysh Slyamkhan, Nuradin Islam, Galymzhan Abdimanap.

Version 2.0
"""

# Import library.
import os
from flask import Flask, request, render_template, jsonify, send_from_directory
import pymysql
import pandas as pd
<<<<<<< HEAD
from sshtunnel import SSHTunnelForwarder
from mysql_connector import remote_query
||||||| 046ad41
=======
from mysql_connector import remote_query
>>>>>>> dev

app = Flask(__name__, static_folder='static/')

# Database config.
sql_hostname = 'localhost'
sql_username = 'root'
sql_password = 'P@ssw0rd2020'
sql_main_database = 'users'
sql_port = 3306
sql_ip = '1.1.1.1.1'
<<<<<<< HEAD
cursorType = pymysql.cursors.DictCursor
||||||| 046ad41
def conn(sql_query):
    with SSHTunnelForwarder(
            (ssh_host, ssh_port),
            ssh_username=ssh_user,
            ssh_password=mypkey,
            remote_bind_address=(sql_hostname, sql_port)) as tunnel:
        conn = pymysql.connect(host='127.0.0.1', user=sql_username,
                passwd=sql_password, db=sql_main_database,
                port=tunnel.local_bind_port)
=======
cursorType = pymysql.cursors.DictCursor

>>>>>>> dev

<<<<<<< HEAD
||||||| 046ad41
        
        data = pd.read_sql_query(sql_query, conn)
        conn.close()
    return data
    #conn.close()
=======
def query(sql_query, typeOp="select"):
    """ Execute query."""
    # Try connection.
    if type_of_run == "remote" or type_of_run == "r":
        return remote_query(sql_query, typeOp)
        
    elif type_of_run == "server" or type_of_run == "s":
        connection_object = pymysql.connect(host='127.0.0.1', user=sql_username,
                    passwd=sql_password, db=sql_main_database, cursorclass=cursorType)

        rows = ""
        try:
            cursor_object = connection_object.cursor()
            cursor_object.execute(sql_query)

            # If type of operation is UPDATE, execute commit.
            if typeOp == "update":
                connection_object.commit()
            else:
                rows = cursor_object.fetchall()
        except Exception as e:
            print(f"Exception occured: {e}")
        finally:
            cursor_object.close()
            connection_object.close()
>>>>>>> dev

<<<<<<< HEAD
def query(sql_query, typeOp="select"):
    """ Execute query."""

    if type_of_run == "remote" or type_of_run == "r":
        return remote_query(sql_query, typeOp)
    else:
        connection_object = pymysql.connect(host='172.16.3.62', user=sql_username,
                    passwd=sql_password, db=sql_main_database, cursorclass=cursorType)

    rows = ""
    try:
        cursor_object = connection_object.cursor()
        cursor_object.execute(sql_query)
||||||| 046ad41
=======
        return rows
>>>>>>> dev

<<<<<<< HEAD
        # If type of operation is UPDATE, execute commit.
        if typeOp == "update":
            connection_object.commit()
        else:
            rows = cursor_object.fetchall()
    except Exception as e:
        print(f"Exception occured: {e}")
    finally:
        cursor_object.close()
        connection_object.close()
||||||| 046ad41
var_on_server = [1,2,3,4,5,6]
#Hello
sql = "select * from users_last_image;"
# val = (user['first_name'], user['last_name'], user['id'], user_last_word, user['username'], user['id'], user_last_word)
data = conn('select * from users_last_image;')
# users_list=[]
# for user in data['user_name']:
    # print(user)
=======
>>>>>>> dev

<<<<<<< HEAD
    return rows
||||||| 046ad41
=======
@app.route('/media/<path:filename>')
def base_static(filename):
    """ Get base path for image."""
>>>>>>> dev

<<<<<<< HEAD
||||||| 046ad41
filename = 'Dataset_qazaq_words_05102020/417/words/417_018_004.jpg'
annotator_id = '398822459'
annotation1 = 'заттай'
=======
    return send_from_directory(app.root_path + '/../', filename)
>>>>>>> dev

<<<<<<< HEAD
@app.route('/media/<path:filename>')
def base_static(filename):
    """ Get base path for image."""
||||||| 046ad41
annotator_id2 = '537619641'
annotation2 = 'заттай'
=======
def get_images(user_id):
    """ Get data."""
>>>>>>> dev

<<<<<<< HEAD
    return send_from_directory(app.root_path + '/../', filename)
||||||| 046ad41
=======
    data = query(f'select id, filename, annotation1, annotator_id, annotation2, annotator_id2 from image_annotations where annotation1 != annotation2 AND (annotator_id = {user_id} OR annotator_id2 = {user_id}) limit 10;')
    total = query(f'select count(*) as total from image_annotations where annotator_id = {user_id} OR annotator_id2 = {user_id};')
    misc = query(f'select count(*) as misc from image_annotations where annotation1 != annotation2 AND (annotator_id = {user_id} OR annotator_id2 = {user_id});')
    return data, total, misc
>>>>>>> dev

<<<<<<< HEAD
def get_images(user_id):
    """ Get data."""

    data = query(f'select id, filename, annotation1, annotator_id, annotation2, annotator_id2 from image_annotations where annotation1 != annotation2 AND (annotator_id = {user_id} OR annotator_id2 = {user_id}) limit 10;')
    total = query(f'select count(*) as total from image_annotations where annotator_id = {user_id} OR annotator_id2 = {user_id};')
    misc = query(f'select count(*) as misc from image_annotations where annotation1 != annotation2 AND (annotator_id = {user_id} OR annotator_id2 = {user_id});')
    return data, total, misc

@app.route('/', methods=['GET', 'POST'])
||||||| 046ad41
@app.route('/')
=======
@app.route('/', methods=['GET', 'POST'])
>>>>>>> dev
def index():
<<<<<<< HEAD
    """ Return the main page."""
||||||| 046ad41
    """Return the main page."""
    print('index print statement here')
    return render_template('index.html', var_from_server=var_on_server, filename=filename, annotation1=annotation1, annotation2=annotation2, users = data['user_name'])
=======
    """ Return the main page."""

    info_user = query('select * from users_last_image;')

    data={}
    user_id=request.args.get('service')
    total = 0
    misc = 0

    # If request GET and return images and annotations for correction.
    if user_id is not None:
        data, total, misc = get_images(user_id)
        return render_template('index.html',  users = info_user, data = data, total=total[0]['total'], misc=misc[0]['misc'], current_user_id=user_id)
    
    # If request POST and updates annotations.
    if request.method == 'POST':

        type_button = request.form['button']
        id_ = int(request.form['id'])
        user_id = request.form['user_id']
        if type_button == 'DELETE':
            query(f'UPDATE image_annotations SET isdelete1=true, isdelete2=true, annotation1=NULL, annotation2=NULL, verified=false WHERE id={id_};', typeOp='update')
            print("hello")

        if type_button == 'SAVE':
            # Get data from form.
            annotation1 = request.form['annotation1']
            annotation2 = request.form['annotation2']
        
            if annotation1 == annotation2:
                # Query for DB.
                query(f'UPDATE image_annotations SET annotation1="{annotation1}", annotation2="{annotation2}", verified=true WHERE id={id_};', typeOp='update')

        #
        data, total, misc = get_images(user_id)
        return render_template('index.html',  users = info_user, data = data, total=total[0]['total'], misc=misc[0]['misc'], current_user_id=user_id)

>>>>>>> dev

    info_user = query('select * from users_last_image;')
    print(info_user)

<<<<<<< HEAD
    data={}
    user_id=request.args.get('service')
    total = 0
    misc = 0
||||||| 046ad41
@app.route('/increment_on_server', methods=['GET', 'POST'])
def increment_on_server():
    """Receieve number from browser, add one and return it."""
=======
    return render_template('index.html', users = info_user, total=total, misc=misc, current_user_id=user_id)
>>>>>>> dev

<<<<<<< HEAD
    # If request GET and return images and annotations for correction.
    if user_id is not None:
        data, total, misc = get_images(user_id)
        return render_template('index.html',  users = info_user, data = data, total=total[0]['total'], misc=misc[0]['misc'], current_user_id=user_id)
    
    # If request POST and updates annotations.
    if request.method == 'POST':
        # Get data from form.
        annotation1 = request.form['annotation1']
        annotation2 = request.form['annotation2']
        id_ = int(request.form['id'])
        user_id = request.form['user_id']
||||||| 046ad41
    print('increment_on_server print statement here')
=======
>>>>>>> dev

<<<<<<< HEAD
        if annotation1 == annotation2:
            # Query for DB.
            query(f'UPDATE image_annotations SET annotation1="{annotation1}", annotation2="{annotation2}", verified=true WHERE id={id_};', typeOp='update')

        

        #
        data, total, misc = get_images(user_id)
        return render_template('index.html',  users = info_user, data = data, total=total[0]['total'], misc=misc[0]['misc'], current_user_id=user_id)



    return render_template('index.html', users = info_user, total=total, misc=misc, current_user_id=user_id)


if __name__ == '__main__':
    type_of_run = "remote"
    app.run(host='0.0.0.0', port=8829)
||||||| 046ad41
    data = request.json
    try:
        new_number = 1 + int(data['package_to_server'])
        return str(new_number)
    except ValueError:
        return 'Please Input A Valid Number'
=======
if __name__ == '__main__':
    type_of_run = os.environ['NORLIST_TOOL_RUN_TYPE']
    app.run(host='0.0.0.0', port=8829)
>>>>>>> dev
