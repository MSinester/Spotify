import mysql.connector
from decouple import config


MYSQL_HOST = config('MYSQL_HOST')
MYSQL_PORT = config('MYSQL_PORT')
MYSQL_USER = config('MYSQL_USER')
MYSQL_PASSWORD = config('MYSQL_PASSWORD')
MYSQL_DB = config('MYSQL_DB')

mydb = mysql.connector.connect(
  host=MYSQL_HOST,
  port=MYSQL_PORT,
  user=MYSQL_USER,
  password=MYSQL_PASSWORD,
  database=MYSQL_DB
)

cursor = mydb.cursor()
