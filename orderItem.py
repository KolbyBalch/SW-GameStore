class orderItem:

    def __init__(self, cursor, cartid, invid, amt):
        cursor.execute("SELECT orderitemid FROM orderitem ORDER BY orderitemid DESC")
        try:
            highestid = cursor.fetchone()
            self.ID = highestid[0] + 1
        except:
            self.ID = 1
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
