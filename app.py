"""
Tool to validate handwritten dataset
Copyright (c) 2020 NORLIST.kz
Written by Kuanysh Slyamkhan, Nuradin Islam, Galymzhan Abdimanap.
Version 2.1
"""

# Import library.
import sys
import os
from flask import Flask, request, render_template, jsonify, send_from_directory
import pymysql
import pandas as pd
from mysql_connector import remote_query

app = Flask(__name__, static_folder='static/')

# Database config.
sql_hostname = 'localhost'
sql_username = 'root'
sql_password = 'P@ssw0rd2020'
sql_main_database = 'users'
sql_port = 3306
sql_ip = '1.1.1.1.1'
cursorType = pymysql.cursors.DictCursor


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

        return rows


@app.route('/media/<path:filename>')
def base_static(filename):
    """ Get base path for image."""

    return send_from_directory(app.root_path + '/../', filename)

def get_images(user_id):
    """ Get data."""

    data = query(f'select id, filename, annotation1, annotator_id, annotation2, annotator_id2 from image_annotations where annotation1 != annotation2 AND (annotator_id = {user_id} OR annotator_id2 = {user_id}) limit 10;')
    total = query(f'select count(*) as total from image_annotations where annotator_id = {user_id} OR annotator_id2 = {user_id};')
    misc = query(f'select count(*) as misc from image_annotations where annotation1 != annotation2 AND (annotator_id = {user_id} OR annotator_id2 = {user_id});')
    return data, total, misc

@app.route('/', methods=['GET', 'POST'])
def index():
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
            print("DELETE")
            query(f'UPDATE image_annotations SET isdelete1=true, isdelete2=true, annotation1=NULL, annotation2=NULL, verified=false WHERE id={id_};', typeOp='update')

        if type_button == 'SAVE':
            print("SAVE")
            # Get data from form.
            annotation1 = request.form['annotation1']
            annotation2 = request.form['annotation2']
        
            if annotation1 == annotation2:
                # Query for DB.
                query(f'UPDATE image_annotations SET annotation1="{annotation1}", annotation2="{annotation2}", verified=true WHERE id={id_};', typeOp='update')

        
        data, total, misc = get_images(user_id)
        return render_template('index.html',  users = info_user, data = data, total=total[0]['total'], misc=misc[0]['misc'], current_user_id=user_id)

    return render_template('index.html', users = info_user, total=total, misc=misc, current_user_id=user_id)


if __name__ == '__main__':
    try:
        type_of_run = sys.argv[1]
    except Exception as e:
        print("Добавьте аргумент")

    if type_of_run == "remote" or type_of_run == "r":
        app.run(host='0.0.0.0', port=8080)
    elif type_of_run == "server" or type_of_run == "s":
        app.run(host='0.0.0.0', port=8829)
    else:
        print("Аргументы: \"server\" or \"remote\"")