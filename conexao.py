import psycopg2

# host=localhost port=5432 dbname=fliperama user=postgres password=xxxxxxx connect_timeout=10 sslmode=prefer
conn = psycopg2.connect(
database="fliperama",
user="postgres",
password="123456",
host="localhost",
port= '5432'
)