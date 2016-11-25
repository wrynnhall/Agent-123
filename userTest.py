from User import User
import gameFunctions as gF
from Game import Game

zach = User("Zach", "easy")

print(zach.name)
print(zach.difficulty)
print(zach.hints)
print(zach.strikes)


newGame = Game()

newGame.howToPlay()

newGame.addToHighscores(zach)

name = gF.getSavedUserName()

print(name)

file = gF.getSavedFilePath(name)

print(file)

gF.displayHighscores()

zach.findRandomLetter()

print(zach.decryptedLetter)

zach.createCharacterList()

print(zach.keyAndCharList[1])

zach.createKeyList()

print(zach.keyAndCharList[0])

zach.createEncryptedLetter()

print(zach.encryptedLetter)

zach.displayEncryptedLetter()

zach.displayKeysAndCharacters()

zach.getUserKeyAndCharacter()

zach.checkUserSolution()



zach.displayEncryptedLetter()



zach.displayKeysAndCharacters()

zach.getHint()
zach.displayEncryptedLetter()



zach.displayKeysAndCharacters()

zach.saveGame()

zach.getSavedData("saves/Zach_save.txt")

zach.saveGame()

