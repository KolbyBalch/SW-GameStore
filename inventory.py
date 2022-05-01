

class Inventory:
    def print_info(game):
        print(game.price)
        print(game.name)
        print(game.amount)
        print(game.gameID)



    def __init__(game, price = 0, name = "", amount = "", gameID = ""):
        game.price = price
        game.name = name
        game.amount = amount
        game.gameID = gameID


    def newGame(game, cursor):

        cursor.execute("SELECT * FROM gamestoreinventory")
        NameTaken = True

        while(NameTaken):
            newname = input("Enter the game's name: ")
            cursor.execute("SELECT * FROM gamestoreinventory WHERE name = '" + newname + "';")
        
            if(cursor.fetchone() != None):
                print("Game Name not available")

            else:
    
                NameTaken = False

        print(" ")
        game.price = input("Enter the games price: ")
        print(" ")
        game.amount = input("Enter how many of this game are there: ")
        print(" ")
        
        cursor.execute("SELECT * FROM gamestoreinventory ORDER BY gameID DESC")
        highestid = cursor.fetchone()
        game.gameID = highestid[0] + 1

        values = "(" + str(game.gameID) + ", '" + game.name + ", '" + str(game.amount) + ", '" + str(game.price) + ");"
        print(values)
        cursor.execute("INSERT INTO gamestoreinventory (gameID, name, amount, price) VALUES " + values)



    def changeprice(game, cursor):
        game.price = input("Enter a new price for " + game.name)

        print("The new price is: " + game.price)
        cursor.execute("UPDATE gamestoreinventory SET price = '" + game.price + "';")
    

    def changename(game, cursor):
        NameTaken = True
        
        while(NameTaken):
            newname = input("Enter a new game name: ")
            cursor.execute("SELECT * FROM gamestoreinventory WHERE name = '" + newname + "';")
        
            if(cursor.fetchone() != None):
                print("Game Name not available")

            else:
                game.name = newname
                NameTaken = False

        print("The new name is: " + game.name)
        cursor.execute("UPDATE gamestoreinventory SET gameID")


    def changeamount(game, cursor):
        game.amount = input("Enter a new amount for " + game.name)

        print("The new price is: " + game.amount)
        cursor.execute("UPDATE gamestoreinventory SET amount = '" + game.amount + "';")

    def DeleteGame(game, cursor):

        print("Are you sure you want to delete this game?")
        choice = input("Enter yes or no")

        if choice == "yes" or "Yes" or "y" or "Y":
            game.name = ""
            game.price = 0
            game.amount = 0
            cursor.execute("DELETE FROM gamestoreinventory WHERE gameID =" + game.gameID)
            game.gameID = ""
        elif choice == "No" or "no" or "NO" or "n" or "N":
            print("This game lives another day . . .")
        else:
            print("Thats not a valid choice, try again.")
            game.DeleteGame()
