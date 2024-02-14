# coding:utf-8

import mysql.connector as Mc
from sqlalchemy import create_engine

def req_one(order : str,value_ord, password : str):
    try:
        conn = Mc.connect(host = 'localhost', database = 'CASSIOPEIA', user = 'root', password = password)
        cursor = conn.cursor(buffered=True)
        cursor.execute(order, value_ord)
        conn.commit()
        return cursor.fetchone()
    except Mc.Error as err:
        print(err)
    finally:
        if(conn.is_connected()):
            cursor.close()
            conn.close()

def req_all(order : str,value_ord, password : str):
    try:
        conn = Mc.connect(host = 'localhost', database = 'CASSIOPEIA', user = 'root', password = password)
        cursor = conn.cursor(buffered=True)
        cursor.execute(order, value_ord)
        conn.commit()
        return cursor.fetchall()
    except Mc.Error as err:
        print(err)
    finally:
        if(conn.is_connected()):
            cursor.close()
            conn.close()

def req_ins_one(order : str, value_ord, password : str):
    try:
        conn = Mc.connect(host = 'localhost', database = 'CASSIOPEIA', user = 'root', password = password)
        cursor = conn.cursor()
        req = f'INSERT INTO {order} VALUES (%s, %s)'
        value_req = (cursor.lastrowid, value_ord )
        cursor.execute(req, value_req)
        conn.commit()
    except Mc.errors.IntegrityError:
        conn.rollback()
    except Mc.Error as err:
        print(err)
    finally:
        if(conn.is_connected()):
            cursor.close()
            conn.close()

def req_ins_two(order : str, value_one, value_two, password : str):
    try:
        conn = Mc.connect(host = 'localhost', database = 'CASSIOPEIA', user = 'root', password = password)
        cursor = conn.cursor()
        req = f'INSERT INTO {order} VALUES (%s, %s, %s)'
        value_req = (cursor.lastrowid, value_one, value_two )
        cursor.execute(req, value_req)
        conn.commit()
    except Mc.errors.IntegrityError:
        conn.rollback()
    except Mc.Error as err:
        print(err)
    finally:
        if(conn.is_connected()):
            cursor.close()
            conn.close()
            
def req_df(dataframe, table : str, password):
    engine = create_engine(f"mysql+mysqlconnector://root:{password}@localhost:3306/cassiopeia")
    try:
        conn = Mc.connect(host = 'localhost', database = 'CASSIOPEIA', user = 'root', password = password)

        dataframe.to_sql(table, con= engine, if_exists='append', index= False)
        
        
    except Mc.errors.IntegrityError:
        print("Games are already exists")      
    except Mc.Error as err:
        print(err)
    finally:
        if(conn.is_connected()):
            conn.close()