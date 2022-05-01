import user as u

def findItemsinCart(user, cursor):

    subtotal = 0

    cursor.execute("SELECT invid, amt FROM orderitem WHERE cartid IN (SELECT cartid FROM cart WHERE userid = " + str(user.userID) +" AND currentcart = True);")
    cartentries = cursor.fetchall()

    cursor.execute("SELECT gamename, price FROM inventory WHERE invid IN (SELECT invid FROM cart WHERE userid = " + str(user.userID) + " AND currentcart = True);")
    inventries = cursor.fetchall()

    print("Game Title : Number of Copies")

    for row in range(cursor.rowcount):
        print(str(inventries[row][0]) + " : " + str(cartentries[row][1]))
        subtotal += (inventries[row][1] * cartentries[row][1])
    
    print("\nSubtotal: " + str(subtotal))

def getTotal(user, cursor):

    subtotal = 0

    cursor.execute("SELECT invid, amt FROM orderitem WHERE cartid IN (SELECT cartid FROM cart WHERE userid = " + str(user.userID) +" AND currentcart = True);")
    cartentries = cursor.fetchall()

    cursor.execute("SELECT gamename, price FROM inventory WHERE invid IN (SELECT invid FROM cart WHERE userid = " + str(user.userID) + " AND currentcart = True);")
    inventries = cursor.fetchall()

    for row in range(cursor.rowcount):
        subtotal += (inventries[row][1] * cartentries[row][1])
