from flask import request
import sqlite3
import hashlib

from flask_app_login import login_v2


db_name = 'login.db'

INSECURE_USER="ImraneIsInsecure"
INSECURE_PW="Insecure123"

SECURE_USER="ImraneIsSafe"
SECURE_PW="Secure123"

## https://pypi.org/project/requests/ ==> LINK OM MET RESTFULL API TE WERKEN 

#### RE-INTIALIZING DATABASE => deleting all records from test database

def delete_all():
    print("Deleting all test records")
    db_conn = sqlite3.connect(db_name)
    c = db_conn.cursor()
    sql_statement = "DELETE FROM USER_PLAIN ; "
    c.execute(sql_statement)
    sql_statement = "DELETE FROM USER_HASH ; "
    c.execute(sql_statement)
    db_conn.commit()
    db_conn.close()
    return "Test records deleted\n"


def loginV1(user, pw):
    db_conn = sqlite3.connect(db_name)
    c = db_conn.cursor()
    sql_statement = "CREATE TABLE IF NOT EXISTS USER_PLAIN (USERNAME TEXT PRIMARY KEY NOT NULL, PASSWORD TEXT NOT NULL); "
    c.execute(sql_statement)
    db_conn.commit()
    print("Creating new user v1 insecure")
    try:
        sql_statement = f"INSERT INTO USER_PLAIN (USERNAME, PASSWORD) VALUES ('{user}' , '{pw}')"
        c.execute(sql_statement)
        db_conn.commit()
    except sqlite3.IntegrityError:
        return "Username has been registered, but is insecure\n"
    return "Signup success, but insecure\n"


def LoginV2(user, pw):
    db_conn = sqlite3.connect(db_name)
    c = db_conn.cursor()
    sql_statement = "CREATE TABLE IF NOT EXISTS USER_HASH (USERNAME TEXT PRIMARY KEY NOT NULL, HASH TEXT NOT NULL); "
    c.execute(sql_statement)
    db_conn.commit()
    print("Creating new user v2 secure")
    try:
        hash_value = hashlib.sha256(pw.encode()).hexdigest()
        sql_statement = f"INSERT INTO USER_HASH (USERNAME, HASH) VALUES ('{user}' , '{hash_value}' );"
        c.execute(sql_statement)
        db_conn.commit()
    except sqlite3.IntegrityError:
        return "Username has been registered\n"
    print('username: ' , user, ' password: ', pw, ' hash: ', hash_value)
    return "Secure signup succeeded\n"

delete_all()
loginV1(INSECURE_USER, INSECURE_PW)
LoginV2(SECURE_USER, SECURE_PW)