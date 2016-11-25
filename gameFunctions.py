from User import User


#Game start text. Reads from start.txt, returns a string ("y" or "n")
#to tell whether to start the game or not
def start():

    #open start.txt and read out its contents
    startText = open('start.txt', 'r')
    #print each line in start.txt
    for line in startText:
        print(line, end="")

    print()
    #get input from user
    startGame = input()

    #validate their input
    isValidInput = False
    while isValidInput == False:

        if startGame == 'y' or startGame == 'n':
            #returns if they chose 'y' or 'n'
            return startGame
        else:
            #keep getting user input until valid
            startGame = input("***That is not a valid input.***\n***Press \'y\'" +
                              " then <enter> for yes***\n***Press \'n\' then <enter> for no***\n")
            
#Displays the start menu
def startMenu():
    print("")
    #display start menu
    menuItems = ["1 Start New Game", "2 Continue a Previous Game", "3 High Scores", "4 Exit the Game"]
    menuNumbers = ["1", "2", "3", "4"]
    print("Select a menu option:")
    for item in menuItems:
        print("***" + item + "***")
    #prompt for input 
    menuChoice = input("***Select a menu option by typing the corresponding number and then pressing <enter>***\n")
    #check for validity, keep getting input until valid
    while menuChoice not in menuNumbers:
        print("***That is not a valid choice***")
        menuChoice = input("***Select a menu option by typing the corresponding number and then pressing <enter>***\n")
    #return what menu item they chose.    
    return menuChoice

    

#prints the highscores from highscores.txt
def displayHighscores():
    print("")
    #open highscores list and print each line in a formatted way.
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
    #open user list file
    userList = open("userList.txt",'r')
    #read the first line 
    readLine = userList.readline()
    userList.close()
    #check if the line is empty, if it is then the document is empty. Return False
    if readLine == "":
        return False
    #if it's not empty, open file again and print each line out to the user.
    else:
        userList = open("userList.txt",'r')
        print("Here is a list of all saved games")
        for line in userList:
            line = line.replace("\n" ,"")
            print(line)
        return True


#prints out the list of saved users. returns False if their are no users
def displaySavedUserlist():
    #open the saved user list file
    userList = open("savedUserList.txt",'r')
    
    #check if the user list is empty
    readLine = userList.readline()
    userList.close()
    #if it is empty, return False
    if readLine == "":
        return False
    #if it's not empty, open the file again and read and print every line to the user, then return true for not empty.
    else:
        userList = open("savedUserList.txt",'r')
        print("Here is a list of all saved games")
        for line in userList:
            line = line.replace("\n" ,"")
            print(line)
        return True

    
#prompts the user to enter their username that has been
#previously saved, then checks it against userList.txt. Finally, returns the name
def getPreviousUserName():
    
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


#prompts the user to enter their username that has been
#previously saved, then checks it against userList.txt. Finally, returns the name
def getSavedUserName():
    
    userList = open("savedUserList.txt",'r')
    
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


#prompt to be outputed if the user loses the game        
def losePrompt():

    print("Better luck next time Agent....")


#asks the user if they are a returning user, returns true or false depending on input.
def previousUser():
    #get input from user
    userOption = input("Are you a returning user? (hit 'y' or 'n' for yes or no, then hit <enter>")

    #check if the user input 'y' or 'n'
    isValid = False
    while isValid == False:

        #if the user actually inputed 'y' or 'n' then return a bool value
        if userOption == 'y' or userOption == 'n':
            isValid = True
            if userOption == 'y':
               return True
            elif userOption == 'n':
                return False
        #if the user did not input 'y' or 'n' then keep prompting for input until they do. Damn user validation...
        else:
            userOption = input("Wrong input, please only type 'y' or 'n' then <enter>")
            
        
        
    
