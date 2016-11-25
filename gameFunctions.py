from User import User
#Game start text. Reads from start.txt, returns a string ("y" or "n")
#to tell whether to start the game or not
def start():

    #open start.txt and read out its contents
    startText = open('start.txt', 'r')
    
    for line in startText:
        print(line, end="")

    print()
    startGame = input()
    isValidInput = False
    while isValidInput == False:

        if startGame == 'y' or startGame == 'n':
            
            return startGame
        else:
            
            startGame = input("***That is not a valid input.***\n***Press \'y\'" +
                              " then <enter> for yes***\n***Press \'n\' then <enter> for no***\n")
            

def startMenu():
    print("")
    menuItems = ["1 Start New Game", "2 Continue a Previous Game", "3 High Scores", "4 Exit the Game"]
    menuNumbers = ["1", "2", "3", "4"]
    print("Select a menu option:")
    for item in menuItems:
        print("***" + item + "***")
    menuChoice = input("***Select a menu option by typing the corresponding number and then pressing <enter>***\n")
    while menuChoice not in menuNumbers:
        print("***That is not a valid choice***")
        menuChoice = input("***Select a menu option by typing the corresponding number and then pressing <enter>***\n")
        
    return menuChoice

    

#prints the highscores from highscores.txt
def displayHighscores():
    print("")
    highscores = open("highscores.txt", 'r')
    print("*"*14 + "HIGHSCORE LIST" + "*"*14)
    for line in highscores:
        line = line.split(",")
        line[1].strip("\n")
        print("\t"*2 + line[0], end="\t")
        print(line[1], end="")
    print("*"*42)
#prints out the list of users. returns False if their are no users
def displayUserlist():
    userList = open("userList.txt",'r')
    readLine = userList.readline()
    userList.close()
    if readLine == "":
        return False
    else:
        userList = open("userList.txt",'r')
        print("Here is a list of all saved games")
        for line in userList:
            line = line.replace("\n" ,"")
            print(line)
        return True

#prints out the list of saved users. returns False if their are no users
def displaySavedUserlist():
    userList = open("savedUserList.txt",'r')
    readLine = userList.readline()
    userList.close()
    if readLine == "":
        return False
    else:
        userList = open("savedUserList.txt",'r')
        print("Here is a list of all saved games")
        for line in userList:
            line = line.replace("\n" ,"")
            print(line)
        return True
#prompts the user to enter their username that has been
#previously saved, then checks it against userList.txt. Finally, returns the name
def getSavedUserName():
    
    userList = open("userList.txt",'r')

    nameList = []

    for line in userList:
        line = line.replace("\n","")
        nameList.append(line)
    
    name = input("Which was your username?")
    isValid = False

    while isValid == False:

        if name in nameList:
            isValid = True
        else:
            name = input("Please enter your username that is in the user list.")

    return name

#based on the valid username, will return the users corresponding file name
def getSavedFilePath(username):
    
    preString = "saves/"
    postString = "_save.txt"

    fileString = preString + username + postString

    return fileString
    

#prompt to be outputed if the user wins the game
def winPrompt():

    print("Good job Agent 123, we'll get this to the higher ups right away!")
        
def losePrompt():

    print("Better luck next time Agent....")

def previousUser():
    userOption = input("Are you a returning user? (hit 'y' or 'n' for yes or no, then hit <enter>")
    
    isValid = False
    while isValid == False:

        if userOption == 'y' or userOption == 'n':
            isValid = True
            if userOption == 'y':
               return True
            elif userOption == 'n':
                return False
        else:
            userOption = input("Wrong input, please only type 'y' or 'n' then <enter>")
            return False
        
        
    
