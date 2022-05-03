import psycopg2
import cart as c
import user as u
import inventory as i

def doNothing():
    print("")

conn = psycopg2.connect(
    host="34.75.109.21",
    database="gamestore",
    user="postgres",
    password="admin"
)

print ("connected to store")
cur = conn.cursor()

def employeeMenu(cursor):
    while(True):
        print("\nEmployee Only Options: \n0. Go Back \n1. Add New Game \n2. Update Game Price \n3. Update Game Name \n4. Update Game Stock \n5. Remove Game")
        empChoice = input("Please make a selection: ")
        match empChoice:
            case "0":
                return 0
            case "1": # New Game
                currentgame = i.Inventory()
                currentgame.newGame(cur)
            case "2": # Update Price
                currentgame = i.getExistingInv(cur)
                if (currentgame != 0):
                    currentgame.changeprice(cur)
            case "3": # Update Name
                currentgame = i.getExistingInv(cur)
                if (currentgame != 0):
                    currentgame.changename(cur)
            case "4": # Update Stock
                currentgame = i.getExistingInv(cur)
                if (currentgame != 0):
                    currentgame.changeamount(cur)
            case "5": # Remove Game
                currentgame = i.getExistingInv(cur)
                if (currentgame != 0):
                    currentgame.DeleteGame(cur)
            case _ : # Default
                print ("Selection not recognized. \n")
        conn.commit()

def main(cur, conn):
    loginFlag = False
    while(True):
        while(loginFlag == False):
            logreg = input("Please select a choice 'Exit', 'Login', or 'Register' \n")

            if (logreg == "Login" or logreg == "login"):
                currentUser = u.userLogin(cur)
                if(currentUser == False):
                    doNothing()
                else:
                    currentCart = c.getCart(cur, currentUser.userID)
                    loginFlag = True

            elif (logreg == "Register" or logreg == "register"):
                currentUser = u.User()
                currentUser.register(cur)
                currentCart = c.getCart(cur, currentUser.userID)
                loginFlag = True

            elif (logreg == "exit" or logreg == "Exit"):
                print("Goodbye!")
                return 0
            conn.commit()

        print("Available Selections: \n\n0. Logout\n1. See Products \n2. See Current Cart \n3. See Past Orders \n4. Manage Account \n")
        if (currentUser.employee == True):
            print ("9: Manage Inventory (Not visible to non-employees).\n")
        menuchoice = input("Please make a selection: ")

        match menuchoice:
            case "0":
                currentUser = ""
                loginFlag = False
            case "1": #See All Products
                i.printAll(currentCart.cartid, cur, conn)
            case "2": #See Current Cart
                currentCart.findItemsinCart(cur)
                
                cartFlag = True
                while(cartFlag == True):
                    print("Available Selections: \n\n0. Go Back \n1. Checkout \n2. Remove Item from Cart \n3. Empty Cart \n")
                    cartSel = input("Please make a selection: ")
                    match cartSel:
                        case "0": #Go Back
                            cartFlag = False
                        case "1": #Checkout
                            currentCart.checkout(cur, conn)
                            currentCart = c.getCart(cur, currentUser.userID)
                        case "2": #Remove Item
                            currentCart.removeItem(cur)
                        case "3": #Empty Cart
                            currentCart.clearCart(cur)
                        case _ :  #Not Recognized
                            print("Selection not Recognized.")
                    conn.commit()

            case "3": #See Past Orders
                c.seePastOrders(cur, currentUser.userID)
            case "4": #Manage Account
                accFlag = True
                while(accFlag):
                    print("Account settings: \n\n0. Go Back \n1. Update Username \n2. Update Password \n3. Update Address \n4. Update Card Information \n5. Delete Account \n")
                    accChoice = input("Please make a selection: ")
                    match accChoice:
                        case "0":
                            accFlag = False
                        case "1":
                            currentUser.changeUsername(cur)
                        case "2":
                            currentUser.changePassword(cur)
                        case "3":
                            currentUser.updateAddr(cur)
                        case "4":
                            currentUser.updateCard(cur)
                        case "5":
                            currentUser.deleteUser(cur)
                            loginFlag = False
                    conn.commit()
            case "9":
                if(currentUser.employee == False):
                    print("Selection not Recognized.")
                elif(currentUser.employee == True):
                    employeeMenu(cur)
            case _ : #Not Recognized
                print("Selection not Recognized.")

        conn.commit()

main(cur, conn)

conn.commit()
cur.close()
conn.close()