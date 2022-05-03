
def userLogin(cursor):
    try:
        login_username = input("Username: ")
        cursor.execute("SELECT * FROM gamestoreuser WHERE username LIKE '" + login_username + "'")
        row = cursor.fetchone()
        login_password = input("Password: ")
        if (login_password == row[2]):
            currentUser = User(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            print("login successful")
            return currentUser
        else:
            print("Username or Password not recognized.")
            return False
    except:
        print("Username or Password not recognized. Are you registered with us? ")
        return False

class User:
    def print_info(self):
        print(self.username)
        print(self.password)
        print(self.name)
        print(self.userID)
        print(self.employee)
        print(self.shippingAddr)
        print(self.billingAddr)
        print(self.cardNum)


    def __init__(self, userID = 0, username = "", password = "", employee = False, name = "", shippingAddr = "", billingAdr = "", cardNum = ""):
        self.username = username
        self.password = password
        self.name = name
        self.userID = userID
        self.employee = employee
        self.shippingAddr = shippingAddr
        self.billingAddr = billingAdr
        self.cardNum = cardNum
        # self.cart = cart
        # self.orders = orders

        # print(self.cart)
        # print(self.orders)
    def register(self, cursor):

        cursor.execute("SELECT * FROM gamestoreuser")
        usernameNotAvailable = True

        while(usernameNotAvailable):
            register_username = input("Please enter a username: ")
            cursor.execute("SELECT * FROM gamestoreuser WHERE username = '" + register_username + "';")
            if(cursor.fetchone() != None):
                print("Username not available.")
            else:

                usernameNotAvailable = False

        print(" ")
        register_password = input("Please enter a password: ")
        print(" ")
        register_name = input("Please enter your name: ")
        print(" ")
        register_shippingAddr = input("Please enter a shipping address: ")
        print(" ")
        register_billingAddr = input("Please enter a billing address: ")
        print(" ")
        register_cardNum = input("Please enter your card number: ")
        print(" ")
        # employee_choice = input("Are you an established employee? Enter 1 if so, 2 if not.")
        # if employee_choice == 1:
        # register_employee = True
        # elif employee_choice == 2:
        # register_employee = False

        cursor.execute("SELECT * FROM gamestoreuser ORDER BY userid DESC")
        highestid = cursor.fetchone()
        self.userID = highestid[0] + 1

        self.username = register_username
        self.password = register_password
        self.name = register_name
        self.shippingAddr = register_shippingAddr
        self.billingAddr = register_billingAddr
        self.cardNum = register_cardNum

        values = "(" + str(self.userID) + ", '" + self.username + "', '" + self.password + "', False, '" + self.name + "', '" + self.shippingAddr + "', '" + self.billingAddr + "', " + self.cardNum + ");"
        cursor.execute("INSERT INTO gamestoreuser (userid, username, pass, employeetag, realname, shippingaddr, billingadr, cardnum) VALUES " + values)
        # self.employee = register_employee

    #def login(self):
    #    login_username = input("Please enter username")
    #    login_password = input("Please enter password")
    #    if(login_password == self.password and login_username == self.username):
    #        print("Successfully logged in.")
    #        return True
    #    else:
    #        print("Incorrect username/password.")
    #        return False

    def changeUsername(self, cursor):
        usernameNotAvailable = True

        while(usernameNotAvailable):
            new_username = input("Please enter a username: ")
            cursor.execute("SELECT * FROM gamestoreuser WHERE username = '" + new_username + "';")
            if(cursor.fetchone() != None):
                print("Username not available.")
            else:
                self.username = new_username
                usernameNotAvailable = False

        print("Your new username is: " + self.username)
        cursor.execute("UPDATE gamestoreuser SET username = '" + self.username + "' WHERE userid = " + str(self.userID) + ";")



    def changePassword(self, cursor):
        self.password = input("Please enter a new password: ")

        print("Your new password is: " + self.password)
        cursor.execute("UPDATE gamestoreuser SET pass = '" + self.password + "' WHERE userid = " + str(self.userID) + ";")



    def updateAddr(self, cursor):
        print("Enter 1 if you would like to update your shipping address.")
        print("Enter 2 if you would like to update your billing address.")
        print("Enter 3 if you would like to update both.")

        choice = int(input("Please enter your selection: "))

        if choice == 1:
            self.shippingAddr = input("Please enter a new shipping address: ")
            cursor.execute("UPDATE gamestoreuser SET shippingaddr = '" + self.shippingAddr + "' WHERE userid = " + str(self.userID) + ";")
        elif choice == 2:
            self.billingAddr = input("Please enter a new billing address: ")
            cursor.execute("UPDATE gamestoreuser SET billingadr = '" + self.billingAddr + "' WHERE userid = " + str(self.userID) + ";")
        elif choice == 3:
            self.shippingAddr = input("Please enter a new shipping address: ")
            cursor.execute("UPDATE gamestoreuser SET shippingaddr = '" + self.shippingAddr + "' WHERE userid = " + str(self.userID) + ";")
            print("\n")
            self.billingAddr = input("Please enter a new billing address: ")
            cursor.execute("UPDATE gamestoreuser SET billingadr = '" + self.billingAddr + "' WHERE userid = " + str(self.userID) + ";")
        else:
            print("That is not a valid option, please try again.")
            self.updateAddr()

    def updateCard(self, cursor):
        try:
            self.cardNum = int(input("Please enter a new card number: "))
        except:
            print("Something went wrong. Make sure that you are inputting only numbers.")
            
        cursor.execute("UPDATE gamestoreuser SET cardnum = " + str(self.cardNum) + " WHERE userid = " + str(self.userID) + ";")

    def deleteUser(self, cursor):
        print("Are you sure you want to delete your account?")
        del_choice = input("Please enter yes or no.")

        if del_choice == "yes":
            self.username = ""
            self.password = ""
            self.name = ""
            self.shippingAddr = ""
            self.billingAddr = ""
            self.cardNum = ""
            cursor.execute("DELETE FROM orderitem WHERE cartid IN (SELECT cartid FROM cart WHERE userid = " + str(self.userID) + ");")
            cursor.execute("DELETE FROM cart WHERE userid =" +self.userID)
            cursor.execute("DELETE FROM gamestoreuser WHERE userid =" +self.userID)
            self.userID = ""
        elif del_choice == "no":
            print("")
        else:
            print("That is not a valid choice, please try again.")
            self.deleteUser()


#username = input("Please enter a username")
#password = input("Please enter a password")
#name = input("Please enter a name")
#userID = input("Please enter a userID")
#employee = False
#shippingAddr = input("Please enter a shipping address")
#billingAddr = input("Please enter a billing address")
#cardNum = input("Please enter your card number")

