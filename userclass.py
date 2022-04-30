



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


    def __init__(self, username, password, userID, employee, name, shippingAddr, billingAdr, cardNum):
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
    def register(self):
        register_username = input("Please enter a username.")
        print(" ")
        register_password = input("Please enter a password.")
        print(" ")
        register_name = input("Please enter your name.")
        print(" ")
        register_userID = input("Please enter a userID (any 4 numbers.)")
        print(" ")

        register_shippingAddr = input("Please enter a shipping address.")
        print(" ")
        register_billingAddr = input("Please enter a billing address.")
        print(" ")
        register_cardNum = input("Please enter your card number.")
        print(" ")
        # employee_choice = input("Are you an established employee? Enter 1 if so, 2 if not.")
        # if employee_choice == 1:
        # register_employee = True
        # elif employee_choice == 2:
        # register_employee = False

        self.username = register_username
        self.password = register_password
        self.name = register_name
        self.userID = register_userID
        self.shippingAddr = register_shippingAddr
        self.billingAddr = register_billingAddr
        self.cardNum = register_cardNum
        # self.employee = register_employee

    def login(self):
        login_username = input("Please enter username")
        login_password = input("Please enter password")
        if(login_password == self.password and login_username == self.username):
            print("Successfully logged in.")
            return True
        else:
            print("Incorrect username/password.")
            return False

    def changeUsername(self):
        self.username = input("Please enter a new username")

        print("Your new username is: " + self.username)

    def changePassword(self):
        self.password = input("Please enter a new password")

        print("Your new password is: " + self.password)

    def updateAddr(self):
        print("Enter 1 if you would like to update your shipping address.")
        print("Enter 2 if you would like to update your billing address.")
        print("Enter 3 if you would like to update both.")

        choice = input("Please enter your selection:")

        if choice == 1:
            self.shippingAddr = input("Please enter a new shipping address.")
        elif choice == 2:
            self.billingAddr = input("Please enter a new billing address.")
        elif choice == 3:
            self.shippingAddr = input("Please enter a new shipping address.")
            print("\n")
            self.billingAddr = input("Please enter a new billing address.")
        else:
            print("That is not a valid option, please try again.")
            updateAddr()

    def updateCard(self):
        self.cardNum =input("Please enter a new card number.")

    def deleteUser(self):
        print("Are you sure you want to delete this user?")
        del_choice = input("Please enter yes or no.")

        if del_choice == "yes":
            self.username = ""
            self.password = ""
            self.name = ""
            self.userID = ""
            self.shippingAddr = ""
            self.billingAddr = ""
            self.cardNum = ""
        elif del_choice == "no":
            print("")
        else:
            print("That is not a valid choice, please try again.")
            deleteUser()


username = input("Please enter a username")
password = input("Please enter a password")
name = input("Please enter a name")
userID = input("Please enter a userID")
employee = False
shippingAddr = input("Please enter a shipping address")
billingAddr = input("Please enter a billing address")
cardNum = input("Please enter your card number")

