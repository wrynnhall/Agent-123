
import gameFunctions as gF
from Game import Game
from User import User

def main():
    #if gameLoop is False, then this would exit the program. 
    gameLoop = True
    while gameLoop:
        menuOption = 0
        
        #Exit game if returns 'n' (no).
        start = gF.start()
        if start == 'n':
            return

        #once the user selects a valid menu option, it returns the string into menuChoice
        #'1', '2', or '3'
        menuLoop = True
        menuChoice = 0
        while menuLoop:
            menuChoice = gF.startMenu()
            
            #Start new game
            if menuChoice == '1':
                #start new game instance
                newGame = Game()
                #check if the user has played before and would like to 
                if gF.previousUser() == True:

                    #show list of usernames and check if their are any
                    userList = gF.displayUserlist()
                    if userList == False:
                        print("There are no saved users")
                        
                    else:
                        #get the user's username
                        name = gF.getPreviousUserName()
                        #abel the path that the users data is in
                        savedPath = gF.getSavedFilePath(name)
                        
                        difficulty = newGame.getDifficulty()
                        #create new user and initialze the saved game data
                        newUser = User(name,difficulty)
                        newUser.initializeSavedGame(savedPath)
                        #create new game conditions
                        newUser.initializeNewGame()

                        #create a loop to run the necessary functions of the game,
                        #which are in runLoop() of the Game class 
                        newGame.runLoop(newUser)
                    
                else:
                    
                    
                    #get the username and difficulty
                    username = newGame.getName()
                    difficulty = newGame.getDifficulty()

                    #create new User instance using username and difficulty
                    newUser = User(username, difficulty)

                    #create new game conditions
                    newUser.initializeNewGame()

                    #create a loop to run the necessary functions of the game,
                    #which are in runLoop() of the Game class 
                    newGame.runLoop(newUser)

            #start saved game    
            elif menuChoice == '2':
                
                #start saved game instance
                savedGame = Game()
                #show list of usernames and check if their are any
                userList = gF.displaySavedUserlist()
                if userList == False:
                    print("There are no saved users")
                else:
                    #get the user's username
                    name = gF.getSavedUserName()
                    #label the path that the users data is in
                    savedPath = gF.getSavedFilePath(name)

                    #create new user and initialze the saved game data
                    savedUser = User(name,"easy")
                    savedUser.initializeSavedGame(savedPath)

                    #run the game loop
                    savedGame.runLoop(savedUser)

            #display high scores screen
            elif menuChoice == '3':

                gF.displayHighscores()

            #exit the game
            elif menuChoice == '4':
                menuLoop = False
                gameLoop= False

main()
