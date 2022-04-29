import psycopg2

try:
    conn = psycopg2.connect(
        host="34.75.109.21",
        database="gamestore",
        user="postgres",
        password="admin"
    )
    print ("connected")
except:
    print ("not connected")