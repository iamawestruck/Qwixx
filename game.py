from player import Player

class Game:
    playerCount = None
    
    def getPlayerCount(self):
        self.playerCount = int(input("How many players will be joining?"))
    
    
    def Game(self):
        self.getPlayerCount()
        print(self.playerCount)
    