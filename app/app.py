import pandas as pd
from sqlalchemy import create_engine
import psycopg2
import pyarrow

db_name = 'database'
db_user = 'username'
db_pass = 'secret'
db_host = 'db'
db_port = '5432'

#INPUT YOUR OWN CONNECTION STRING HERE
conn_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)

#conn=psycopg2.connect(dbname='database', user='username', host='db', password='secret', port=5432

df1 = pd.read_parquet('ds_clicks.parquet.gzip')
df2 = pd.read_parquet('ds_leads.parquet.gzip')
df3 = pd.read_parquet('ds_offers.parquet.gzip')
#Import .csv file
#df = pd.read_csv('upload_test_data_big.csv')



#perform to_sql test and print result
db = create_engine(conn_string)
conn = db.connect()


df1.to_sql('clicks', con=conn, if_exists='append', index=False)
df2.to_sql('leads', con=conn, if_exists='append', index=False)
df3.to_sql('offers', con=conn, if_exists='append', index=False)
