# coding:utf-8

import mysql.connector as Mc
from mysql.connector import MySQLConnection
from sqlalchemy import create_engine
import pandas as pd
from pandas import DataFrame

class Connect_Tools():
    def __init__(self, password : str = ""):
        self.password = password

        self.engine = create_engine(f"mysql+mysqlconnector://root:{password}@localhost:3306/cassiopeia")
        self.conn = Mc.connect(host = 'localhost', database = 'CASSIOPEIA', user = 'root', password = password)

    def req_interne(self, order : str):
        """Simple interne request fonction. """
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(order)
            self.conn.commit()
        except Mc.Error as err:
            print(err)
            return None
        finally:
            if cursor:
                cursor.close()

    def req_fetchone(self, order : str, *args):
        """Fetchone fonction with a buffered cursor."""
        cursor = None
        try:
            cursor = self.conn.cursor(buffered=True)
            cursor.execute(order, args)
            self.conn.commit()
            return cursor.fetchone()
        except Mc.Error as err:
            print(err)
            return None
        finally:
            if cursor:
                cursor.close()
        
    def req_fetchall(self, order : str, *args):
        """Fetchall fonction with buffered cursor."""
        cursor = None
        try:
            cursor = self.conn.cursor(buffered=True)
            cursor.execute(order, args)
            self.conn.commit()
            return cursor.fetchall()
        except Mc.Error as err:
            print(err)
            return None
        finally:
            if cursor:
                cursor.close()

    def req_insert(self, table_name : str, args_list : list, nbins : int):
        """Insert a row into a specified table with a primary key's colonne auto increment. Nbins is the nomber of values to insert."""
        cursor = None
        try:
            cursor = self.conn.cursor()
            columns = ', '.join(['%s']*nbins)
            req = f'INSERT INTO {table_name} VALUES ({columns})'
            value_req = (cursor.lastrowid, *args_list )
            cursor.execute(req, value_req)
            self.conn.commit()
        except Mc.errors.IntegrityError:
            self.conn.rollback()
        except Mc.Error as err:
            print(err)
        finally:
            if cursor:
                cursor.close()

    def close_conn(self):
        try:
            self.conn.is_connected()
        except Mc.Error:
            print("Pas de connexion ouverte...")
        finally:
            self.conn.close()

    def read_db(self, table_name : str):
        try:
            req_table = f"SELECT * FROM {table_name}"
            req_df = pd.read_sql(sql=req_table, con= self.engine)
            return req_df
        except pd.errors.DatabaseError as err:
            print(err)
    
    def insert_db(self, dataframe : pd.DataFrame, table_name : str):
        """Insert database in mysql server."""
        try:
            dataframe.to_sql(table_name, con = self.engine, if_exists="append", index= False)
        except pd.errors.DatabaseError as err:
            print(err)