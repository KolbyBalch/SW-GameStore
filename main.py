import psycopg2
import orderItem as oi

conn = psycopg2.connect(
    host="34.75.109.21",
    database="gamestore",
    user="postgres",
    password="admin"
)
print ("connected")

cur = conn.cursor()

oi.findItemsinCart(1, cur)

cur.close()
conn.close()
