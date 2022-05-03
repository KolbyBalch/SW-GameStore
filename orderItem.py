def getOrderItem(cursor, invid, cartid):
    cursor.execute("SELECT * FROM orderitem WHERE invid = " + str(invid) + " AND cartid = " + str(cartid) + ";")
    try:
        row = cursor.fetchone()
        return orderItem(cursor, row[1], row[2], [3], row[0])
    except:
        print("Something went wrong! We couldn't find that cart item.")



class orderItem:

    def __init__(self, cursor, cartid, invid, amt, orderitemid = 0):
        if (orderitemid == 0):
            cursor.execute("SELECT orderitemid FROM orderitem ORDER BY orderitemid DESC")
            try:
                highestid = cursor.fetchone()
                self.ID = highestid[0] + 1
            except:
                self.ID = 1
        else:
            self.ID = orderitemid
        self.cartID = cartid
        self.invID = invid
        self.amt = amt


    def updateamt(self, cursor):
        self.amt = int(input("How many copies would you like? "))
        cursor.execute("UPDATE orderitem SET amt = " + str(self.amt) + " WHERE orderitemid = " + str(self.ID) + ";")

    def delete(self, cursor):
        cursor.execute("DELETE FROM orderitem WHERE orderitemid = " + str(self.ID) + ";")
        self.ID = ""
        self.invID = ""
        self.invID = ""
        self.amt = ""
