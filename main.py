from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import mysql.connector
from sshtunnel import SSHTunnelForwarder
import pymysql
import pandas as pd



# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'




class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])


    
    def conn(sql_query):
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

    
    @app.route("/", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)
    
        print(form.errors)
        if request.method == 'POST':
            name=request.form['service']
            print(name)
    
        if form.validate():
            # Save the comment here.
            print(name)
            flash('Hello ' + name)
            
        else:
            flash('All the form fields are required. ')
        
        info_user = ReusableForm.conn('select * from users_last_image;')

    
        return render_template('hello.html', form=form, users=info_user)

if __name__ == "__main__":
    app.run()