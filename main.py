import psycopg2
import orderItem as oi
import user as u

conn = psycopg2.connect(
    host="34.75.109.21",
    database="gamestore",
    user="postgres",
    password="admin"
)
print ("connected to store")
cur = conn.cursor()
loginFlag = False
loopFlag = True

while(loopFlag):
    while(loginFlag == False):
        logreg = input("Please select a choice 'Login' or 'Register' \n")

        if (logreg == "Login" or logreg == "login"):
            currentUser = u.userLogin(cur)
            if(currentUser == False):
                break
            else:
                print(currentUser.username)
                print(currentUser.name)
                loginFlag = True

        elif (logreg == "Register" or logreg == "register"):
            currentUser = u.User()
            currentUser.register(cur)
            loginFlag = True

    print("Account settings: \n\n0. Go Back \n1. Update Username \n2. Update Password \n3. Update Address \n4. Update Card Information \n5. Delete Account \n")

    accChoice = input("Please make a selection")

    match accChoice:
        case 0:
            loopFlag = False
        case 1:
            currentUser.changeUsername(cur)
        case 2:
            currentUser.changePassword(cur)
        case 3:
            currentUser.updateAddr(cur)
        case 4:
            currentUser.updateCard(cur)
        case 5:
            currentUser.deleteUser(cur)
            loginFlag = False

cur.close()
conn.close()
