from User import User
import gameFunctions as gF


class Game:


    #initiate Game
    def __init__(self):
        #represents game state
        self.isDone = False
        
    #prompts user for a name
    def getName(self):
        print("")
        print("We know your codename is Agent 123, but what is your username?")
        name = input("(please only enter letters, numbers, or underscores)\n")

        #check if name is valid and prompt for another name while invalid
        while self.validName(name) == False:
            name = input("")
                  
        return name

    
    #checks the validity of the game
    def validName(self, name):

        #get file that contains valid characters, then make a list of those characters
        charFile = open("validNameChars.txt", 'r')
        validChars = charFile.readline()
        validChars = validChars.split(",")

        #check if each character is valid
        #if not, returns false.
        isValid = True
        for char in name:
            if char not in validChars:
                print("Contains invalid characters. Please try again.")
                isValid = False
                return isValid

        savedUsernames = open("userList.txt", 'r')
        
        for line in savedUsernames:
            line = line.strip("\n")
            if line == name:
                print("Username is already in use. Please try again.")
                isValid = False
                return isValid
        return isValid


    #promtps the user to select a difficulty
    def getDifficulty(self):
        print("")
        print("Which difficulty would you like to be set at?")
        print("1 Easy")
        print("2 Intermediate")
        print("3 Hard")
        difficulty = input("please select the number option then hit <enter>\n")

        #validate until actual option is selected
        options = ['1', '2', '3']
        isValid = False
        while isValid == False:
            if difficulty not in options:
                difficulty = input("Not a valid number option. Enter valid number option, then press <enter>\n")
            else:
                isValid = True
        #converts the number option to the actual value (makes it easier if
        #the user needs to only type a number, rather than the whole difficulty name)
        if difficulty == '1':
            difficulty = "easy"
        elif difficulty == '2':
            difficulty = "intermediate"
        elif difficulty == '3':
            difficulty = "hard"

        return difficulty

   
    #How to play prompt. display to the user the rules of the game and how to play.     
    def howToPlay(self):
        #open howToPlay.txt and read out its contents
        htp = open('howToPlay.txt', 'r')
        #print each line in htp, print the line
        for line in htp:
            print(line, end="")

        print()
        
    #defines getKey function to access in the sorted() function in addToHighscores function
    def getKey(self, item):
        return item[1]

        
    #takes the score the user has and adds it to highscores.txt. This will also format the
    #list so that the scores in the txt document will be in decending order.
    def addToHighscores(self, User):

        #get the users name and score
        name = User.name
        score = User.score

        #append the highscores.txt with the new user and score
        highscores = open("highscores.txt",'a')
        highscores.write(name + "," + str(score) + "\n")
        highscores.close()

        #read the highscores.txt and put each line into a list
        highscores = open("highscores.txt",'r')
        highscoresList = []
        for line in highscores:
            #split each line into a separate list
            line = line.split(',')
            #take out the newline return out so the number can be read as a number
            line[1].rstrip("\n")
            #turn string number to an int number
            line[1] = int(line[1])
            #add the list to highscores list
            highscoresList.append(line)
        highscores.close()

        
        #sort the list using the magical sorted() (sorts by the second index of each list in the list)
        highscoresList = sorted(highscoresList, key=self.getKey, reverse = True)

        #nested for loop to check if the user name is already on the highscore list
        #if it is, it then removes it and keeps the higher score, so there are no
        #duplicate users on the user list.
        for i in range(0,(len(highscoresList))):
            for j in range(i+1, len(highscoresList)):
                #make sure j is not out of range
                if j < len(highscoresList):
                    #if the names are equal in value, remove last user from the list
                    if highscoresList[i][0] == highscoresList[j][0]:
                        highscoresList.pop(j)
                        
        #overwrite the file with the data from each list.
        outfile = open("highscores.txt",'w')
        #for each item in the list add them to highscores.txt
        for item in highscoresList:
            outfile.write(item[0] + "," + str(item[1]) + "\n")


    #Adds the name to the user list, unless it's already in the userList.txt
    def addToUserList(self, User):
        #create a list to hold values from text file
        userList = []
        #oepn text file
        userTxt = open("userList.txt", 'r')
        #add each line to the list, taking out the newline carriage return
        for line in userTxt:
            line = userTxt.readline()
            line = line.strip("\n")
            userList.append(line)
        userTxt.close()
        #open the file to possibly be appended
        userTxt = open("userList.txt", 'a')

        #if the user is not in the lsit, add it to the text file.
        if User.name not in userList:
            userTxt.write(User.name + "\n")
        userTxt.close()

            
    #removes duplicate users from the user list.    
    def removeFromSavedUserList(self, User):
        #create a list to hold all the usernames
        userList = []
        #open savedUserList.txt
        userTxt = open('savedUserList.txt','r')
        #add each line to the list
        for line in userTxt:
            if line != "":
                line = line.strip("\n")
                
                userList.append(line)
        userTxt.close
        #check if the name is in the list and remove it if it is.
        isPresent = True
        while isPresent == True:
            if User.name in userList:
                userList.remove(User.name)
            else:
                isPresent = False
        outfile = open('savedUserList.txt','w')
        #write the name to the file.
        for item in userList:
            outfile.write(item + "\n")
    
                        
    #display main menu options and get user input option
    def mainMenu(self):
        #prompt user to select an option
        print("")
        print("What would you like to do?")
        print("1 Solve for a key\n2 Solve entire letter\n3 Get a hint\n4 Exit the game")
        userOption = input("Press the corresponding number option, then hit <enter>\n")

        options = ['1','2','3','4']

        #check if the option is valid
        isValid = False
        while isValid == False:
            if userOption in options:
                isValid = True
            #prompt user for new value if invalid
            else:
                userOption = input("Not a valid option. Press the number option, then hit <enter>\n")
        return userOption


    #display a save menu, then get which option the user wants
    def saveMenu(self):
        #prompt user for save menu option. 
        userOption = input("Would you like to save your game? ('y' or 'n')\n")
        #validate the input
        while userOption != "y" and userOption != "n":
            userOption = input("Please type 'y' or 'n' then hit <enter>\n")

        return userOption


    #Prints newline carriage returns until a suitable distance is placed between
    #the previous round and the next round
    def newScreen(self):
        print("\n" * 20)


    #the game's loop
    def runLoop(self, User):
        self.howToPlay()
        while self.isDone == False:
            
            #display informative text to user
            User.correctPrompt()
            
            User.displayEncryptedLetter()
            User.displayKeysAndCharacters()
            User.displayHintsAndStrikes()

            #get which menu option the user wants
            mainOption = self.mainMenu()

            #menu option for solving a key:
            if mainOption == '1':

                User.getUserKeyAndCharacter()
                User.checkUserSolution()
                
            elif mainOption == '2':
                User.solveEntireLetter()

            #menu option for getting a hint:
            elif mainOption == '3':
                User.getHint()

            #menu option for exiting the game:
            elif mainOption == '4':

                #get whether user wants to save game or not
                saveOption = self.saveMenu()
                #save game option
                if saveOption == 'y':
                    User.saveGame()
                    self.isDone = True
                #just exit option
                elif saveOption == 'n':
                    self.isDone = True

            #check whether user has struck out. sets isDone to true if true
            if User.lose == True:
                self.addToUserList(User)
                self.isDone = True
                gF.losePrompt()
                self.removeFromSavedUserList(User)
                User.saveGame()

            #if the user wins the game, add their score to the highscore list
            if User.win == True:
                self.addToUserList(User)
                self.addToHighscores(User)
                gF.winPrompt()
                self.isDone = True
                self.removeFromSavedUserList(User)
                User.saveGame()
            
            self.newScreen()    
            

