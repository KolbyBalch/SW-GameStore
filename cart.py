import orderItem as o

def getCart(cursor, userid, cartid = 0):
    if cartid == 0:
        cursor.execute("SELECT * FROM cart WHERE userid = " + str(userid) + " AND currentcart = true;")
    else:
        cursor.execute("SELECT * FROM cart WHERE userid = " + str(userid) + " AND currentcart = " + str(cartid) + ";")
    
    try:
        row = cursor.fetchone()
        if(row == None):
            newcart = cart(cursor, 0, userid, 0, True)
            cursor.execute("INSERT INTO cart (cartid, userid, subtotal, currentcart) VALUES (" + str(newcart.cartid) + ", " + str(newcart.userid) + ", " + str(newcart.subtotal) + ", True);")
            return newcart
        else:
            return cart(cursor, row[0], row[1], row[2], row[3])
    except:
        print("Cart not found.")

def seePastOrders(cursor, userid):
    cursor.execute("SELECT * FROM cart WHERE userid = " + str(userid) + " AND currentcart = false;")
    pastorder = cursor.fetchone()
    if pastorder == None:
        print("No previous orders to display. ")
        return 0
    else:
        while(pastorder != None):
            print("CartID: " + str(pastorder[0]) + " | Total: $" + str(pastorder[2]) + ";")
            pastorder = cursor.fetchone()
    while(True):
        print("Would you like to see more details about an order? ")
        choice = input("0. Go Back \n1. See Details of Order \nPlease make a Selection: ")
        match choice:
            case "0":
                return 0
            case "1":
                idChoice = input("Which order would you like to look at? (Input CartID): ")
                print("\n")
                cursor.execute("SELECT * FROM cart WHERE cartid = " + str(idChoice) + ";")
                chosenrow = cursor.fetchone()
                chosenOrder = cart(cursor, chosenrow[0], chosenrow[1], chosenrow[2], chosenrow[3])
                chosenOrder.findItemsinCart(cursor)



class cart:

    def __init__(self, cursor, cartid, userid, subtotal, currentcart):
        if (cartid == 0):
            cursor.execute("SELECT cartid FROM cart ORDER BY cartid DESC;")
            try:
                highestid = cursor.fetchone()
                self.cartid = highestid[0] + 1
            except:
                self.cartid = 1
        else:
            self.cartid = cartid
        self.userid = userid
        self.subtotal = subtotal
        self.currentcart = currentcart


    def findItemsinCart(self, cursor):
        newsubtotal = 0

        cursor.execute("SELECT invid, gamename, price FROM inventory WHERE invid IN (SELECT invid FROM orderitem WHERE cartid = " + str(self.cartid) + ");")
        entry = cursor.fetchone()
        print("ID : Game Title : Price")

        while (entry != None):
            print(str(entry[0]) + " : " + str(entry[1]) + " : " + str(entry[2]))
            newsubtotal += entry[2]
            entry = cursor.fetchone()
        
        self.subtotal = newsubtotal
        print("\nTotal: " + str(self.subtotal))
        cursor.execute("UPDATE cart SET subtotal = " + str(self.subtotal) + ";")

    def getTotal(self, cursor):
        newsubtotal = 0

        cursor.execute("SELECT invid, gamename, price FROM inventory WHERE invid IN (SELECT invid FROM orderitem WHERE cartid = " + str(self.cartid) + ");")
        entry = cursor.fetchone()

        while (entry != None):
            newsubtotal += entry[2]
            entry = cursor.fetchone()
        
        self.subtotal = newsubtotal
        cursor.execute("UPDATE cart SET subtotal = " + str(self.subtotal) + ";")

    def removeItem(self, cursor):
        self.findItemsinCart(cursor)
        print("Which Game did you wish to remove? ")
        choice = input("Please input the gameid as it appears above: ")
        cursor.execute("SELECT * FROM orderitem WHERE cartid = " + str(self.cartid) + " AND invid = " + str(choice) + ";")
        row = cursor.fetchone()
        selectedItem = o.getOrderItem(cursor, row[2], row[1])
        selectedItem.delete(cursor)
        self.getTotal(cursor)

    def checkout(self, cursor, conn):
        self.getTotal(cursor)
        print("\nChecking Out! Total: $"+ str(self.subtotal) + "\n")

        cursor.execute("UPDATE inventory SET stock = (stock - 1) WHERE invid IN (SELECT invid FROM orderitem WHERE cartid = " + str(self.cartid) + ");")

        self.currentcart = False
        cursor.execute("UPDATE cart SET currentcart = false WHERE cartid = " + str(self.cartid) + ";")
        conn.commit()

    def clearCart(self, cursor):
        cursor.execute("DELETE FROM orderitem WHERE cartid = " + str(self.cartid) + ";")