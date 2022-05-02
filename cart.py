from main import doNothing


import orderItem as o

class cart:
    doNothing
    #cartid (refer to invid and userid)
    #userid
    #subtotal
    #currentcart

def findItemsinCart(self, userID, cursor):
    newsubtotal = 0

    cursor.execute("SELECT invid, amt FROM orderitem WHERE cartid IN (SELECT cartid FROM cart WHERE userid = " + str(userID) +" AND currentcart = True);")
    cartentries = cursor.fetchall()

    cursor.execute("SELECT gamename, price FROM inventory WHERE invid IN (SELECT invid FROM cart WHERE userid = " + str(userID) + " AND currentcart = True);")
    inventries = cursor.fetchall()

    print("Game Title : Number of Copies")

    for row in range(cursor.rowcount):
        print(str(inventries[row][0]) + " : " + str(cartentries[row][1]))
        newsubtotal += (inventries[row][1] * cartentries[row][1])
    
    self.subtotal = newsubtotal
    print("\nSubtotal: " + str(self.subtotal))

def getTotal(self, userID, cursor):

    newsubtotal = 0

    cursor.execute("SELECT invid, amt FROM orderitem WHERE cartid IN (SELECT cartid FROM cart WHERE userid = " + str(userID) +" AND currentcart = True);")
    cartentries = cursor.fetchall()

    cursor.execute("SELECT gamename, price FROM inventory WHERE invid IN (SELECT invid FROM cart WHERE userid = " + str(userID) + " AND currentcart = True);")
    inventries = cursor.fetchall()

    for row in range(cursor.rowcount):
        newsubtotal += (inventries[row][1] * cartentries[row][1])

    self.subtotal = newsubtotal
