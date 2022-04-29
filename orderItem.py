import psycopg2


def findItemsinCart(cartID, cursor):

    cursor.execute("SELECT * FROM orderitem WHERE cartid = " + str(cartID))

    print("Number of Unique games: ", cursor.rowcount )

    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()
