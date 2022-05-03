import orderItem as o

def printAll(currentcartid, cursor, conn):
    cursor.execute("SELECT * FROM inventory ORDER BY invid ASC;")
    row = cursor.fetchone()
    print("\nGames in our inventory: ")
    while row != None:
        print("Game id: " + str(row[0]) + ": " + str(row[3]) + " : $" + str(row[2]) + " : " + str(row[1]) + " in stock.")
        row = cursor.fetchone()

    while(True):
        print("\nSee something you like? \n0. Go Back \n1. Add a game to your cart")
        invChoice = input("Please make a selection: ")
        print()
        match invChoice:
            case "0":
                return 0
            case "1":
                while(True):
                    try:
                        gamechoice = int(input("Please input the game id here ('0' to go back): "))
                        #amtchoice = int(input("And how many copies: "))
                        amtchoice = 1
                        cursor.execute("SELECT stock FROM inventory WHERE invid = " + str(gamechoice))
                        selectedgameAMT = cursor.fetchone()
                        if (gamechoice == 0):
                            return 0
                        elif selectedgameAMT[0] > 0:
                            break
                        elif (amtchoice <= selectedgameAMT[0]):
                            break
                        else:
                            print("I'm sorry, we don't seem to have enough copies for you. \nPlease make another selection. \n")
                    except:
                        print("Response not valid.")
                        return 0
                cursor.execute("SELECT * FROM orderitem WHERE cartid = " + str(currentcartid) + " AND invid = " + str(gamechoice))
                row = cursor.fetchone()
                if (row == None):
                    newItem = o.orderItem(cursor, currentcartid, gamechoice, amtchoice)
                    cursor.execute("INSERT INTO orderitem (orderitemid, cartid, invid, amt) VALUES (" + str(newItem.ID) + ", " + str(newItem.cartID) + ", " + str(newItem.invID) + ", "  + str(newItem.amt) + ");")
                else:
                    print ("It looks like that selection is already in your cart.")
        conn.commit()

def getExistingInv(cursor):
    cursor.execute("SELECT * FROM inventory ORDER BY invid ASC;")
    allrows = cursor.fetchall()
    for row in allrows:
        print("GameID : " + str(row[0]) + " : Game Name : " + str(row[3]) + " : Price : " + str(row[2]) + " : # in Stock : " + str(row[1]))
    gameSel = input("\nWhat gameid do you want to edit/delete ('0' to go back): ")
    cursor.execute("SELECT * FROM inventory WHERE invid = " + str(gameSel) + ";")
    gamerow = cursor.fetchone()
    if(gamerow == None):
        print("Exit Selected or Gameid not recognized")
        return 0
    else:
        invobj = Inventory(gamerow[2], gamerow[3], gamerow[1], gamerow[0])
        return invobj

class Inventory:
    def print_info(self):
        print(self.price)
        print(self.name)
        print(self.amount)
        print(self.gameID)

    def __init__(self, price = 0, name = "", amount = "", gameID = ""):
        self.price = price
        self.name = name
        self.amount = amount
        self.gameID = gameID


    def newGame(self, cursor):

        cursor.execute("SELECT * FROM inventory")
        NameTaken = True

        while(NameTaken):
            newname = input("Enter the game's name: ")
            cursor.execute("SELECT * FROM inventory WHERE gamename = '" + newname + "';")
        
            if(cursor.fetchone() != None):
                print("Game Name already exists")

            else:
                self.name = newname
                NameTaken = False

        self.price = float(input("Enter the games price: "))
        self.amount = int(input("Enter how many of this game are there: "))
        
        
        cursor.execute("SELECT * FROM inventory ORDER BY invid DESC")
        try:
            highestid = cursor.fetchone()
            self.gameID = highestid[0] + 1
        except:
            self.gameID = 1

        values = "(" + str(self.gameID) + ", '" + self.name + "', " + str(self.amount) + ", " + str(self.price) + ");"
        cursor.execute("INSERT INTO inventory (invid, gamename, stock, price) VALUES " + values)

    def changeprice(self, cursor):
        self.price = float(input("Enter a new price for " + self.name + ": "))

        print("The new price is: " + str(self.price))
        cursor.execute("UPDATE inventory SET price = " + str(self.price) + " WHERE invid = " + str(self.gameID) + ";")
    
    def changename(self, cursor):
        NameTaken = True
        
        while(NameTaken):
            newname = input("Enter a new game name: ")
            cursor.execute("SELECT * FROM inventory WHERE gamename = '" + newname + "';")
        
            if(cursor.fetchone() != None):
                print("Game Name not available")

            else:
                self.name = newname
                NameTaken = False

        print("The new name is: " + self.name)
        cursor.execute("UPDATE inventory SET gamename = '" + str(self.name) + "' WHERE invid = " + str(self.gameID) + ";")


    def changeamount(self, cursor):
        self.amount = input("Enter a new amount for " + str(self.name) + ": ")

        print("The new stock is: " + self.amount)
        cursor.execute("UPDATE inventory SET stock = " + str(self.amount) + " WHERE invid = " + str(self.gameID) + ";")

    def DeleteGame(self, cursor):

        print("Are you sure you want to delete this game?")
        choice = input("Enter yes or no: ")

        if choice == ("yes" or "Yes" or "y" or "Y"):
            self.name = ""
            self.price = 0
            self.amount = 0
            cursor.execute("DELETE FROM inventory WHERE invid = " + str(self.gameID) + ";")
            self.gameID = ""
        elif choice == ("No" or "no" or "NO" or "n" or "N"):
            print("This game lives another day . . .")
        else:
            print("Thats not a valid choice, try again.")
            self.DeleteGame(cursor)
