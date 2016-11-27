import random
import gameFunctions as gF
class User:

    
    #base User initialization
    def __init__(self, name, difficulty):

        #set defined arguments
        self.name = name
        self.difficulty = difficulty
        self.lettersFile = "letters.txt"

        #set undefined arguments for reference
        self.decryptedLetter = ""
        self.encrytpedLetter = []
        self.keyAndCharList = [[],[]]
        self.userKey = ""
        self.userChar = ""
        self.actualChar = ""
        self.hints = 0
        self.strikes = 0
        self.validChars = 0
        self.win = False
        self.lose = False
        self.score = 0
        #only set to string until correctness is found (after first round)
        self.correct = ""

        
    #grabs a random line from the letters txt file and sets it to decryptedLetter
    def findRandomLetter(self):

        #find out how many letters(lines) are in letterFile
        lines = 0
        infile = open(self.lettersFile, 'r')
        for line in infile:
            lines += 1
        infile.close()

        #find a random number that is less than or equal to the number of lines in the file
        randLine = random.randrange(1, lines + 1)

        #reopen letterFile, read, and then save the letter(line) at randLine
        infile = open(self.lettersFile, 'r')

        currentLine = 1
        letter = ""
        while currentLine <= randLine:
            letter = infile.readline()
            currentLine += 1
        letter = letter.strip("\n")
        #set the letter at that line to self.decryptedLetter
        self.decryptedLetter = letter


    #prints how many hints and how many strikes the user has left.
    def displayHintsAndStrikes(self):
        print("")
        print("Strikes left: " + str(self.strikes))
        print("Hints left: " + str(self.hints))
        print("Score: " + str(self.score))


    #creates a list of unique characters used in the decrypted letter.
    def createCharacterList(self):
        self.keyAndCharList[1] = []
        #for each character in the string
        for char in self.decryptedLetter:

            #if the character is not in the first list (character) in keyAndCharList
            #add it to the list. 
            if char not in self.keyAndCharList[1]:
                if char != "\n" and char != " ":
                    self.keyAndCharList[1].append(char)


    #creates the list of unique keys and stores in a list
    def createKeyList(self):

        #get how many unique characters there are in the letter
        charNum = len(self.keyAndCharList[1])

        #create a list of unique, random numbers between 1 and 100 whose length does not
        #exceed the number of unique characters
        keyList = []

        #keep track of how many random numbers created so far using index.
        #based on that, keep going until have all unique numbers
        index = 0
        while index < charNum:
            isValid = False
            while isValid == False:
                
                randNum = random.randrange(1, 101)
                
                if str(randNum) not in keyList:
                    
                    isValid = True
                    keyList.append(str(randNum))
            index += 1

        #set the fist list in self.keyAndCharList to keyList
        self.keyAndCharList[0] = keyList


    #sets the value of self.encryptedLetter
    def createEncryptedLetter(self):
        
        #create a string to hold the letter.
        encryptLetter = []

        #go through every character in the letter and compare it to every letter in keyAndCharList[1]
        #then convert the letters to corresponding numbers in the key list and put them into the encryptLetter list
        for char in self.decryptedLetter:
            if char == " ":
                encryptLetter.append("-")  
            else:
                index = 0
                for item in self.keyAndCharList[1]:
                    if char == item:
                        encryptLetter.append(str(self.keyAndCharList[0][index]))
                    index += 1
                    
        #set self.encryptedLetter to the final result   
        self.encryptedLetter = encryptLetter


    #solves for one key and character as long as the user has at least one hint.
    def getHint(self):
        if self.hints > 0:
            #find a random index to point to, then solve for that key and character
            randNum = random.randrange(0,len(self.keyAndCharList[0]))
            self.userKey = self.keyAndCharList[0][randNum]
            self.userChar = self.keyAndCharList[1][randNum]
            self.checkUserSolution()
            print("Hint applied...")
            self.hints -=1
            self.correct = "hint"
        else:
            print("You don't have any more hints")

        
    #takes the elements in the self.encryptedLetter and formats (prints) them. 
    def displayEncryptedLetter(self):
        print("")
        print("*"*50 + "   ENCRYPTED LETTER   " + "*"*50)
        for key in self.encryptedLetter:
            print(key, end=" ")
        print()
        print("*"*122)


    #prints a formated display of the remaining keys characters.
    def displayKeysAndCharacters(self):
        print("")
        print("List of valid keys remaining: ", end="")
        for key in self.keyAndCharList[0]:
            print(key, end=" ")
        print()    
        print("List of valid characters remaining: ", end="")
        for char in self.validChars:
            print(char, end=" ")
        print()

    
    #asks the user for a key and a character
    def getUserKeyAndCharacter(self):
        
        self.userKey = input("Which key would you like to solve for?\n")

        #check to see if the key given is valid or not. Keeps prompting unitl response is valid
        isValid = False
        while isValid == False:
            if self.userKey in self.keyAndCharList[0]:
                isValid = True
            else:
               self.userKey = input("That is not a valid key. Enter a valid key from the list of keys\n") 

        
        self.userChar = input("What do you think is the solution for the key?\n")

        #check to see if the key given is valid or not. Keeps prompting unitl response is valid
        isValid = False
        while isValid == False:
            if self.userChar in self.validChars:
                isValid = True
            else:
               self.userChar = input("That is not a valid character. Enter a valid character from the list of valid characters\n")


    #check if the users character choice is equal to the actual character with the user provided key
    #returns true if user is correct, and false if wrong.
    def checkUserSolution(self):

        #create index to hold where the key is stored in the list
        index = 0
        #check for the key in the list
        for key in self.keyAndCharList[0]:
            
            if key == self.userKey:
                #set actualChar to the value and the index in the 2D list
                self.actualChar = self.keyAndCharList[1][index]
                break
            #increment index should it not be found at that index.
            index += 1
        #find if actualChar and userChar are the same, which means the user
        #guessed correctly
        if self.actualChar == self.userChar:
            #edit all the arguments to reflect the correct values.
            self.correct = True
            self.editEncryptedLetter()
            self.editValidChars()
            self.editKeyAndCharList()
            self.addScore(self.difficulty, "plus")
        #if the user guessed wrong...    
        else:
            #adjust for wrong values.
            self.strikes -= 1
            self.correct = False
            self.addScore(self.difficulty, "minus")
            #if the user has no more strikes left, they lose.
            if self.strikes < 0:
                self.lose = True


    #prints text based on the value of self.correct, reflects user correctness, wrongness,
    #and if they used a hint            
    def correctPrompt(self):
        #if it's correct, display correct prompt
        if self.correct == True:
            print("That was correct Agent...")
        #if it's wrong, display wrong prompt
        elif self.correct == False:
            print("That was wrong Agent...")
        #if it's a hint, display hint prompt
        elif self.correct == "hint":
            print("Here is your hint:")
        else:
            print("")


    #called when user wants to solve for the entire letter.
    def solveEntireLetter(self):
        #get user input
        solution = input("Type what you think the letter says, then hit enter. Remember: only input lower case letters\n" +
                         "and spaces (<spacebar>). This is your only warning!\n-->")
        #if the user guesses correctly
        if solution == self.decryptedLetter:
            #edit win variables and game state
            self.win = True
            self.addScore(self.difficulty, "solved")
            self.saveGame()
        #if the user guessed wrong
        else:
            #edit wrong variables
            self.strikes -= 1
            self.correct = False
            self.addScore(self.difficulty, "minus")

        #if the user guessed wrong and the strikes are at zero, they lose.
        if self.strikes < 0:
            self.lose = True


    #if the user's solution is correct, this method is called to edit the self.encryptedLetter to change for it.
    def editEncryptedLetter(self):
        
        #check every key in encryptedKey against the user inputed key, and for every match it converts the number back to the
        #corresponding character.
        index = 0                               
        for key in self.encryptedLetter:
            if key == self.userKey:
                self.encryptedLetter[index] = self.userChar
            index += 1


    #if the user is correct, will be called to remove the correct character given from self.validChars
    def editValidChars(self):

        self.validChars.remove(self.userChar)


    #removes the correct key and character from self.keyAndCharList
    def editKeyAndCharList(self):

        #remove correct key from the keys list
        for key in self.keyAndCharList[0]:
            if key == self.userKey:
                self.keyAndCharList[0].remove(key)

        #remove correct characters from the character list 
        for char in self.keyAndCharList[1]:
            if char == self.actualChar:
                self.keyAndCharList[1].remove(char)

        #sets gameOver to True, conveying the fact that since all keys are solved for, the game is over and won.
        if len(self.keyAndCharList[0]) == 0:
            self.win = True
            

    #condenses a list into a string that can be written into a file
    def listToString(self, convertList):
        outputString = ""
        for item in convertList:
            outputString += item
            outputString += "," 

        return outputString


    #converts the string back into a list
    def stringToList(self, convertString):
        
        outputList = convertString.split(",")
        return outputList

        
    #add to the score based on difficulty. plusOrMinus represents if the score should be added or subtracted
    def addScore(self, difficulty, plusOrMinus):

        #if the difficulty is easy
        if difficulty == "easy":
            if plusOrMinus == "plus":
                self.score += 10
            elif plusOrMinus == "minus":
                self.score -= 10
            elif plusOrMinus == "solved":
                self.score += 50
        #if the difficulty is intermediate
        elif difficulty == "intermediate":
            if plusOrMinus == "plus":
                self.score += 50
            elif plusOrMinus == "minus":
                self.score -= 50
            elif plusOrMinus == "solved":
                self.score += 75
        #if the difficulty is hard    
        elif difficulty == "hard":
            if plusOrMinus == "plus":
                self.score += 100
            elif plusOrMinus == "minus":
                self.score -= 100
            elif plusOrMinus == "solved":
                self.score += 150
            
        
    #saves the current state of the game to a text file
    def saveGame(self):

        #open file, make it's path the persons username plus _save.txt, and add it to the saves directory
        outfile = open("saves/" + self.name + "_save.txt", 'w')
        
        #write data to each line

        #write name to file
        outfile.write(self.name + "\n")
        #write difficulty to file
        outfile.write(self.difficulty + "\n")
        #write decrypted letter to file
        outfile.write(self.decryptedLetter + "\n")
        #write strikes to file
        outfile.write(str(self.strikes) + "\n")
        #write hints to file
        outfile.write(str(self.hints) + "\n")
        #convert encryptedLetter to a string and then write it to file
        eLString = self.listToString(self.encryptedLetter)
        outfile.write(eLString + "\n")
        #convert keys list and char list to string and write to file
        kLString = self.listToString(self.keyAndCharList[0])
        outfile.write(kLString + "\n")
        
        cLString = self.listToString(self.keyAndCharList[1])
        outfile.write(cLString + "\n")
        #write score to file
        outfile.write(str(self.score) + "\n")
        #write validChars to file after it's converted to a string
        vCString = self.listToString(self.validChars)
        outfile.write(vCString + "\n")
        

        
        outfile.close()
        
        #open userList file and add the username to the end of the file
        userList = open("savedUserList.txt", 'r')
        isRepeat = False
        for line in userList:
            if line == (self.name + "\n"):
                isRepeat = True
        if isRepeat == False:
            userList.close()
            userList = open("savedUserList.txt", 'a')
            
            userList.write(self.name + "\n")
        userList.close()


    #provided a file, takes each line and reads to class arguments
    def getSavedData(self, file):

        infile = open(file, 'r')

        #read name line. Does not need to be saved
        infile.readline()
        #read difficulty line. Does not need to be saved
        infile.readline()
        #read decrypted letter line and save to User
        self.decryptedLetter = infile.readline()
        self.decryptedLetter = self.decryptedLetter.strip("\n")
        #read strikes line and save to User
        self.strikes = int(infile.readline())
        #read hints line and save to User
        self.hints = int(infile.readline())
        #read encrypted letter line and convert it to a list then save to User
        elList = self.stringToList(infile.readline())
        self.encryptedLetter = elList
        self.encryptedLetter.remove("\n")
        
        #read key and character line and convert it to a list then save to User
        klList = self.stringToList(infile.readline())
        self.keyAndCharList[0] = klList
        self.keyAndCharList[0].remove("\n")

        clList = self.stringToList(infile.readline())
        self.keyAndCharList[1] = clList
        self.keyAndCharList[1].remove("\n")
        
        #read in score line from file and save to User
        self.score = int(infile.readline())

        #read in validChars line, convert to list, and save to User
        vCList = self.stringToList(infile.readline())
        self.validChars = vCList
        self.validChars.remove("\n")
        infile.close()

        
    #sets the hints and strikes for the game depending on difficulty    
    def setHintsAndStrikes(self):
        #if the difficulty is easy set each to 3
        if self.difficulty == "easy":
            self.hints = 3
            self.strikes = 3
        #if the difficulty is intermediate set each to 2
        elif self.difficulty == "intermediate":
            self.hints = 2
            self.strikes = 2
        #if the difficulty is hard set each to 1    
        elif self.difficulty == "hard":
            self.hints = 1
            self.strikes = 1


    #for the beginning of the game, will reset validChars
    def setValidChars(self):
        self.validChars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


    #create new game conditions (start of a new game)
    def initializeNewGame(self):
        self.setValidChars()
        self.setHintsAndStrikes()
        self.findRandomLetter()
        self.createCharacterList()
        self.createKeyList()
        self.createEncryptedLetter()

    #initialize saved game conditions
    def initializeSavedGame(self, path):
        self.getSavedData(path)

