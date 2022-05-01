
class orderItem:

    def __init__(self, cursor, cartid, invid):
        cursor.execute("SELECT orderitemid FROM orderitem ORDER BY orderitemid DESC")
        highestid = cursor.fetchone()

        self.ID = highestid[0] + 1
        self.cartID = cartid
        self.invID = invid
        self.amt = int(input("How many copies would you like? "))

    def updateamt(self, cursor):
        self.amt = int(input("How many copies would you like? "))
        cursor.execute("UPDATE orderitem SET amt = " + str(self.amt) + " WHERE orderitemid = " + str(self.ID) + ";")

    def delete(self, cursor):
        cursor.execute("DELETE FROM orderitem WHERE orderitemid = " + str(self.ID) + ";")
        self.ID = ""
        self.invID = ""
        self.invID = ""
        self.amt = ""
