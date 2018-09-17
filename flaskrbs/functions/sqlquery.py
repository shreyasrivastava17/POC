import os
import sqlite3
import pandas as pd


data_url = '/home/allahbaksh/RBS/flaskrbs/rbsdata.csv'
headers = ['person_id','first_name','last_name','mobile','Relationship_manager','firebase_id','IsSignificant']
Customers_master = pd.read_csv(data_url, header=None, names=headers)

# Clear example.db if it exists
if os.path.exists('example.db'):
    os.remove('example.db')

# Create a database
conn = sqlite3.connect('example.db',check_same_thread=False)

# Add the data to our database
Customers_master.to_sql('Customers_master', conn, dtype={
    'person_id':'VARCHAR(10)',
    'first_name':'VARCHAR(200)',
    'last_name':'VARCHAR(200)',
    'mobile':'VARCHAR(10)',
    'Relationship_manager':'VARCHAR(100)',
	'firebase_id':'VARCHAR(100)',
	'IsSignificant':'VARCHAR(5)',
    
})


conn.row_factory = sqlite3.Row

# Make a convenience function for running SQL queries
def sql_query(query):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def sql_edit_insert(query,var):
    cur = conn.cursor()
    cur.execute(query,var)
    conn.commit()

def sql_delete(query,var):
    cur = conn.cursor()
    cur.execute(query,var)

def sql_query2(query,var):
    cur = conn.cursor()
    cur.execute(query,var)
    rows = cur.fetchall()
    return rows

def sql_create(query):
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()

sql_create_cust_table = ''' CREATE TABLE Customers(
                                        id varchar(10),
                                        Name Varchar(200) NOT NULL,
                                        IsSignificant VARCHAR(5),
                                        firebase_id varchar(50),
                                        mobile VARCHAR(10)
                                    ) '''
sql_create(sql_create_cust_table)

