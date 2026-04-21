import mysql.connector
# Security for users and passwords
# import os

def create_conn():
    conn = mysql.connector.connect(
        host="localhost", # Localhost is also 127.0.0.1
        user="infs3070",
        # user = os.environ.get('3070User')
        password = "pydev",
        # password = os.environ.get('3070Pass')
        database = "infs3070"
    )
    return conn