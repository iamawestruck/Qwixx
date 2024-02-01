
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

    def setColoredNumber(self, color, number):
        if self.verifyColoredNumber(color, number):
            match color:
                case "red":
                    self.red.append(number)
                case "yellow":
                    self.yellow.append(number)
                case "green":
                    self.green.append(number)
                case "blue":
                    self.blue.append(number)

    def verifyColoredNumber(self, color, number):
        match color:
            case "red":
                if len(self.red) == 0:
                    return True
                return self.red[-1] < number
            case "yellow":
                if len(self.yellow) == 0:
                    return True
                return self.yellow[-1] < number
            case "green":
                if len(self.green) == 0:
                    return True
                return self.green[-1] > number
            case "blue":
                if len(self.blue) == 0:
                    return True
                return self.blue[-1] > number
