import psycopg2
import orderItem as oi
import user as u

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

def main(cur):
    loginFlag = False
    while(True):
        while(loginFlag == False):
            logreg = input("Please select a choice 'Exit', 'Login', or 'Register' \n")

            if (logreg == "Login" or logreg == "login"):
                currentUser = u.userLogin(cur)
                if(currentUser == False):
                    doNothing()
                else:
                    loginFlag = True

            elif (logreg == "Register" or logreg == "register"):
                currentUser = u.User()
                currentUser.register(cur)
                loginFlag = True

            elif (logreg == "exit" or logreg == "Exit"):
                print("Goodbye!")
                return 0

        print("Available Selections: \n\n0. Logout\n1. See Products \n2. Filter Products \n3. See Current Cart \n4. See Past Orders \n5. Manage Account \n")
        menuchoice = input("Please make a selection: ")
        match menuchoice:
            case "0":
                currentUser = ""
                loginFlag = False
            case "1": #See Products
                doNothing()
            case "2": #Filter Products
                doNothing()
            case "3": #See Current Cart
                doNothing()
            case "4": #See Past Orders
                doNothing()
            case "5": #Manage Account
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


main(cur)

conn.commit()
cur.close()
conn.close()