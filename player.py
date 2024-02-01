
class Player:
    red = None
    yellow = None
    green = None
    blue = None
    penalty = None

    def __init__(self):
        self.red = []
        self.yellow = []
        self.green = []
        self.blue = []
        self.penalty = 0

    def coloredNumber(self, color, number):
        match color:
            case "red":
                self.red.append(number)
            case "yellow":
                self.yellow.append(number)
            case "green":
                self.green.append(number)
            case "blue":
                self.blue.append(number)