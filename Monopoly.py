import random
import os
import pygame

pygame.init()
WIDTH, HIGHT = 1300, 1100

win = pygame.display.set_mode((WIDTH, HIGHT))
pygame.display.set_caption("Monopoly")
pygame.display.flip()

ROWS, COLS = 11, 11

SPACE_WIDTH = 200
SPACE_HIGHT = 300

COLOR_WIDTH, COLOR_HIGHT = 100, 25

########COLOURS######### (R,G,B)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
WHITE = (225, 225, 225)
BROWN = (150, 75, 0)
RED = (255, 0, 0)
PINK = (255, 192, 203)
GREEN = (0, 225, 0)
SKY_BLUE = (135, 206, 235)
DARK_BLUE = (0, 0, 225)
YELLOW = (255, 225, 0)
ORANGE = (255, 165, 0)
########################
allProperties = ['b1', 'b2', 'lb1', 'lb2', 'lb3', 'p1', 'p2', 'p3', 'o1', 'o2', 'o3', 'r1', 'r2',
                                'r3', 'y1', 'y2', 'y3', 'g1', 'g2', 'g3', 'db1', 'db2']
allRailroads = ['rr1', 'rr2', 'rr3', 'rr4']
allUtility = ['ww', 'ec']
spaces = {0: 0, 1: 'b1', 2: 'cc', 3: 'b2', 4: 'tax1', 5: 'rr1', 6: 'lb1', 7: "chance", 8: 'lb2', 9: 'lb3', 10: 'visit', 11: 'p1', 12: 'ec', 13: 'p2', 14: 'p3', 15: 'rr2', 16: 'o1', 17: 'cc', 18: 'o2', 19: 'o3', 20: 'fp', 21: 'r1,', 22: 'chance', 23: 'r2', 24: 'r3', 25: 'rr3', 26: 'y1', 27: 'y2', 28: 'ww', 29: 'y3', 30: 'jail', 31: 'g1', 32: 'g2', 33: 'cc', 34: 'g3', 35: 'rr4', 36: 'chance', 37: 'db1', 38: 'tax2', 39: 'db2'}


allPropertyObj = []
allRailroadObj = []
allUtilityObj = []


propertyNames = {'b1': "Mediterranean Avenue/Old Kent Rd (Brown 1)", 'b2': "Baltic Avenue/Whitechapel Rd (Brown 2)", 'lb1': "Oriental Avenue/The Angel, Islington (Light Blue 1)", 'lb2': "Vermont Avenue/Euston Rd (Light Blue 2)", 'lb3': "Connecticut Avenue/Pentonville Rd (Light Blue 3)", 'p1': "St. Charles Place/Pall Mall (Pink 1)", 'p2': "States Avenue/Whitehall (Pink 2)", 'p3': "Virginia Avenue/Northumberland Ave (Pink 3)", 'o1': "St. James Place/Bow St (Orange 1)", 'o2': "Tennessee Avenue/Marlborough St (Orange 2)", 'o3': "New York Avenue/Vine St (Orange 3)", 'r1': "Kentucky Avenue/Strand (Red 1)", 'r2': "Indiana Avenue/Fleet St (Red 2)", 'r3': "Illinois Avenue/Trafalgar Sq (Red 3)", 'y1' : "Atlantic Avenue/Leicester Sq (Yellow 1)", 'y2': "Ventnor Avenue/Coventry St (Yellow 2)", 'y3': "Marvin Gardens/Piccadilly (Yellow 3)", 'g1': "Pacific Avenue/Regent St (Green 1)", 'g2': "North Carolina Avenue/Oxford St (Green 2)", 'g3': "Pennsylvania Avenue/Bond St (Green 3)", 'db1': "Park Place/Park Lane (Dark Blue 1)", 'db2': "Boardwalk/Mayfair (Dark Blue 2)", 'rr1': "Reading Railroad (Railroad 1)", 'rr2': "Pennsylvania Railroad (Railroad 2)", 'rr3': "B & O Railroad (Railroad 3)", 'rr4': "Short Line (Railroad 4)", 'ww': "Waterworks", 'ec': "Electric Company"}

class Game:
    def __init__(self):
        print("Game Init")
        self.playerList = []
        self.playerNameList = []
        self.availableProperties = ['b1', 'b2', 'lb1', 'lb2', 'lb3', 'p1', 'p2', 'p3', 'o1', 'o2', 'o3', 'r1', 'r2',
                                    'r3', 'y1', 'y2', 'y3', 'g1', 'g2', 'g3', 'db1', 'db2']
        self.availableRailroads = ['rr1', 'rr2', 'rr3', 'rr4']
        self.availableUtility = ['ww', 'ec']
        self.taxSpaces = ['tax1', 'tax2']

        self.propertyObj = []
        self.railroadObj = []
        self.taxObj = []
        self.utilityObj = []

    def AddPlayer(self, obj, name):
        self.playerList.append(obj)
        self.playerNameList.append(name)
        return True

    def GetPlayers(self):
        for player in self.playerList:
            print(str(player))

    def GetPlayerList(self):
        return self.playerList

    def GetPlayerNameList(self):
        return self.playerNameList



class Board:
    def __init__(self):
        pass

    def MakeBox(self, xPos, yPos, rectWidth, rectHight, color, thickness):
        self.rectangle = pygame.Rect(xPos, yPos, rectWidth, rectHight)
        pygame.draw.rect(win, color, self.rectangle, thickness)
        pygame.display.update()

    def CreateBoard(self):
        self.rectX = 100
        self.rectY = 0
        win.fill(WHITE)
        pygame.display.update()

        #########################
        # Set Top Row Colors
        self.colorX = 200
        self.colorY = 75
        for i in range(ROWS - 7):
            if i == 1:
                pass
            else:
                self.MakeBox(self.colorX, self.colorY, COLOR_WIDTH, COLOR_HIGHT, RED, 0)
            self.colorX += 100
        self.colorX = 700
        for i in range(ROWS - 7):
            if i == 2:
                pass
            else:
                self.MakeBox(self.colorX, self.colorY, COLOR_WIDTH, COLOR_HIGHT, YELLOW, 0)
            self.colorX += 100
        #############################
        ##Bottom Row Colors
        self.colorX = 200
        self.colorY = 1000
        for i in range(ROWS - 7):
            if i == 2:
                pass
            else:
                self.MakeBox(self.colorX, self.colorY, COLOR_WIDTH, COLOR_HIGHT, SKY_BLUE, 0)
            self.colorX += 100
        self.colorX = 800
        for i in range(ROWS - 8):
            if i == 1:
                pass
            else:
                self.MakeBox(self.colorX, self.colorY, COLOR_WIDTH, COLOR_HIGHT, BROWN, 0)
            self.colorX += 100
        ##############################
        ##Left Side Colors
        self.colorX = 175
        self.colorY = 100
        for i in range(COLS - 7):
            if i == 2:
                pass
            else:
                self.MakeBox(self.colorX, self.colorY, COLOR_HIGHT, COLOR_WIDTH, ORANGE, 0)
            self.colorY += 100
        self.colorY = 600
        for i in range(COLS - 7):
            if i == 2:
                pass
            else:
                self.MakeBox(self.colorX, self.colorY, COLOR_HIGHT, COLOR_WIDTH, PINK, 0)
            self.colorY += 100
        #######################
        ##Right Side Colors
        self.colorX = 1100
        self.colorY = 100
        for i in range(COLS - 7):
            if i == 2:
                pass
            else:
                self.MakeBox(self.colorX, self.colorY, COLOR_HIGHT, COLOR_WIDTH, GREEN, 0)
            self.colorY += 100
        self.colorY = 700
        for i in range(COLS - 8):
            if i == 1:
                pass
            else:
                self.MakeBox(self.colorX, self.colorY, COLOR_HIGHT, COLOR_WIDTH, DARK_BLUE, 0)
            self.colorY += 100
        #############################
        ##PRINT ACTUAL BOARD##
        self.rectX = 100
        self.rectY = 0
        for r in range(ROWS - 2):
            for c in range(COLS - 1):
                self.MakeBox(self.rectX, self.rectY, SPACE_WIDTH, SPACE_HIGHT, BLACK, 5)
                self.rectX += 100
            self.rectY += 100
            self.rectX = 100
        ##Clears middle of board
        self.clearRectX = 200
        self.clearRectY = 100
        for i in range(ROWS - 4):
            for j in range(COLS - 3):
                self.MakeBox(self.clearRectX, self.clearRectY, SPACE_WIDTH, SPACE_HIGHT, WHITE, 0)
                self.clearRectX += 100
            self.clearRectY += 100
            self.clearRectX = 200

class Property:
    def __init__(self, cost, pph, rent, rent1, rent2, rent3, rent4, rentH, mortgage):
        self.cost = cost
        self.pph = pph
        self.rent = rent
        self.rent1 = rent1
        self.rent2 = rent2
        self.rent3 = rent3
        self.rent4 = rent4
        self.rentH = rentH
        self.mortgage = mortgage
        self.houseCount = 0
        self.hotelCount = 0

    def GetCost(self):
        return self.cost

    def GetRent(self):
        if self.houseCount == 0:
            return self.rent
        elif self.houseCount == 1:
            return self.rent1
        elif self.houseCount == 2:
            return self.rent2
        elif self.houseCount == 3:
            return self.rent3
        elif self.houseCount == 4:
            return self.rent4
        elif self.hotelCount == 1:
            return self.rentH

class Railroad:
    def __init__(self, cost):
        self.cost = cost
        self.rent = 12.5 #techniclly should be 25 but math reasons has it at half that
    def GetCost(self):
        return self.cost

    def GetRent(self):
        return self.rent

class Utility:
    def __init__(self, cost):
        self.cost = cost

    def GetCost(self):
        return self.cost

class Tax:
    def __init__(self, amount):
        self.amount = amount

    def GetTaxAmount(self):
        return self.amount

class Dice:
    def __init__(self):
        self.dice1 = 0
        self.dice2 = 0
        self.total = 0

    def RollDice(self):
        self.dice1 = random.randint(1, 6)
        self.dice2 = random.randint(1, 6)
        self.total = self.dice2 + self.dice1
        return self.total

    def GetTotalRoll(self):
        return self.total

    def GetDice1(self):
        return self.dice1

    def GetDice2(self):
        return self.dice2

class Player:

    def __init__(self, name):
        self.name = name
        self.money = 1500
        self.properties = []
        self.railroads = []
        self.utilities = []
        self.boardPos = 0
        self.inJail = False
        self.jailCards = 0
        self.jailCount = 0
        self.hotelCount = 0
        self.houseCount = 0

    def ChangeMoney(self, amount):
        self.money += amount

    def GetMoney(self):
        return self.money

    def AddOwnedProperty(self, prop):
        self.properties.append(prop)

    def GetOwnedProperties(self):
        return self.properties

    def AddOwnedRailroad(self, rr):
        self.railroads.append(rr)

    def GetOwnedRailroads(self):
        return self.railroads

    def AddOwnedUtility(self, util):
        self.utilities.append(util)

    def GetOwnedUtility(self):
        return self.utilities

    def SetBoardPos(self, pos):
        self.boardPos = pos

    def AddBoardPos(self, move):
        self.boardPos += move
        if self.boardPos >= 40:
            self.boardPos -= 40
            self.ChangeMoney(200)
            print(f"{self.name} got $200 for passing Go!")

    def GetBoardPos(self):
        return self.boardPos

    def PutInJail(self, jail):
        self.inJail = jail

    def GetInJail(self):
        return self.inJail

    def AddJailCard(self, amount):
        self.jailCards += amount

    def GetJailCards(self):
        return self.jailCards

    def AddHouse(self, amount):
        self.houseCount += amount

    def GetHouseCount(self):
        return self.houseCount

    def AddHotel(self, amount):
        self.hotelCount += amount

    def GetHotelCount(self):
        return self.hotelCount

    def SetJailCount(self, amount):
        self.jailCount = amount

    def GetJailCount(self):
        return self.jailCount

    def ChangeJailCount(self, amount):
        self.jailCount += amount

class CommunityChest:

    def __init__(self):
        self.cards = ['go', 200, -50, 50, 'jailcard', 'jail', 100, 20, 'player10', 100, -100, -50, 25, 'house40/115hotel', 10, 100]

    def GetCards(self):
        return self.cards

class Chance:
    def __init__(self):
        self.cards = ['boardwalk', 'go', 'r3', 'p1', 'closeRR', 'closeRR', 'closeUtil', 50,'jailcard', 'back3', 'jail', '25house/100hotel', -15, 'readingRR', '-50each', 150]

    def GetCards(self):
        return self.cards


def PlayerInit():
    playerCount = 0
    while playerCount < 2:
        playerCount = int(input("How many players are playing?(Min 2): "))
    for i in range(playerCount):
        playerName = input(f"What is the name of Player {i + 1}")
        n = Player(playerName)
        game.AddPlayer(n, playerName)

def PropertyInit():
    b1 = Property(60, 50, 2, 10, 30, 90, 160, 250, 30)
    b2  = Property(60, 50, 4, 20, 60, 180, 320, 450, 30)
    lb1 = Property(100, 50, 6, 30, 90, 270, 400, 550, 50)
    lb2 = Property(100, 50, 6, 30, 90, 270, 400, 550, 50)
    lb3 = Property(120, 50, 8, 40, 100, 300, 450, 600, 60)
    p1  = Property(140, 100, 10, 50, 150, 450, 625, 750, 70)
    p2  = Property(140, 100, 10, 50, 150, 450, 625, 750, 70)
    p3  = Property(160, 100, 12, 60, 180, 500, 700, 900, 80)
    o1  = Property(180, 100, 14, 70, 200, 550, 750, 950, 90)
    o2  = Property(180, 100, 14, 70, 200, 550, 750, 950, 90)
    o3  = Property(200, 100, 16, 80, 220, 600, 800, 1000, 100)
    r1  = Property(220, 150, 18, 90, 250, 700, 875, 1050, 110)
    r2  = Property(220, 150, 18, 90, 250, 700, 875, 1050, 110)
    r3  = Property(240, 150, 20, 100, 300, 750, 925, 1100, 120)
    y1  = Property(260, 150, 22, 110, 330, 800, 975, 1150, 130)
    y2  = Property(260, 150, 22, 110, 330, 800, 975, 1150, 130)
    y3  = Property(280, 150, 24, 120, 360, 850, 1025, 1200, 140)
    g1  = Property(300, 200, 26, 130, 390, 900, 1100, 1275, 150)
    g2  = Property(300, 200, 26, 130, 390, 900, 1100, 1275, 150)
    g3  = Property(320, 200, 28, 150, 450, 1000, 1200, 1400, 160)
    db1 = Property(350, 200, 35, 175, 500, 1100, 1300, 1500, 175)
    db2 = Property(400, 200, 50, 200, 600, 1400, 1700, 2000, 200)
    game.propertyObj.extend((b1, b2, lb1, lb2, lb3, p1, p2, p3, o1, o2, o3, r1, r2, r3, y1, y2, y3, g1, g2, g3, db1, db2))
    allPropertyObj.extend((b1, b2, lb1, lb2, lb3, p1, p2, p3, o1, o2, o3, r1, r2, r3, y1, y2, y3, g1, g2, g3, db1, db2))
    # Railroads
    rr1 = Railroad(200)
    rr2 = Railroad(200)
    rr3 = Railroad(200)
    rr4 = Railroad(200)
    game.railroadObj.extend((rr1, rr2, rr3, rr4))
    allRailroadObj.extend((rr1, rr2, rr3, rr4))

    tax1 = Tax(200)
    tax2 = Tax(100)
    game.taxObj.extend((tax1, tax2))

    ww = Utility(150)
    ec = Utility(150)
    game.utilityObj.extend((ww, ec))
    allUtilityObj.extend((ww, ec))


def PlayGame():
    winner = False
    cc = CommunityChest()
    random.shuffle(cc.GetCards())
    chance = Chance()
    random.shuffle(chance.GetCards())
    while winner == False:
        pygame.event.get()
        for index, player in enumerate(game.GetPlayerList()):
            if game.GetPlayerList()[index].GetInJail() == False:
                game.GetPlayerList()[index].GetOwnedProperties().sort()
                game.GetPlayerList()[index].GetOwnedRailroads().sort()
                game.GetPlayerList()[index].GetOwnedUtility().sort()
                poop = input(f"{game.GetPlayerNameList()[index]}'s Turn (Press Enter to Continue)")
                print(f"Current Balance: {game.GetPlayerList()[index].GetMoney()}")
                print(f"Current Properties: {game.GetPlayerList()[index].GetOwnedProperties()}")
                print(f"Current Railroads: {game.GetPlayerList()[index].GetOwnedRailroads()}")
                print(f"Current Utility: {game.GetPlayerList()[index].GetOwnedUtility()}")
                game.GetPlayerList()[index].AddBoardPos(dice.RollDice())
                print(f"You Rolled a {dice.GetTotalRoll()}")
                print(f"Current Space: {game.GetPlayerList()[index].GetBoardPos()}")
                #### COMMUNITY CHEST SPACE
                if spaces[game.GetPlayerList()[index].GetBoardPos()] == 'cc':
                    if isinstance(cc.GetCards()[0], int):
                        if cc.GetCards()[0] > 0:
                            game.GetPlayerList()[index].ChangeMoney(cc.GetCards()[0])
                            print(f"Landed on a Community Chest Space and gained ${cc.GetCards()[0]}!")
                        elif cc.GetCards()[0] < 0:
                            game.GetPlayerList()[index].ChangeMoney(cc.GetCards()[0])
                            print(f"Landed on a Community Chest Space and lost ${-(cc.GetCards()[0])}!")

                    elif cc.GetCards()[0] == 'go':
                        game.GetPlayerList()[index].SetBoardPos(0)
                        game.GetPlayerList()[index].ChangeMoney(200)
                        print("Advance to Go!")
                    elif cc.GetCards()[0] == 'jailcard':
                        print("Landed on a Community Chest Space and got a Get Out of Jail Free Card!")
                        game.GetPlayerList()[index].AddJailCard(1)
                    elif cc.GetCards()[0] == 'jail':
                        print("Landed on a Community Chest Space and got put in jail!")
                        game.GetPlayerList()[index].PutInJail(True)
                    elif cc.GetCards()[0] == 'player10':
                        receivingPlayer = game.GetPlayerList()[index]
                        print("Landed on a Community Chest Space and now every player owes you $10")
                        for owedPlayer in game.GetPlayerList():
                            receivingPlayer.ChangeMoney(10)
                            owedPlayer.ChangeMoney(-10)
                    elif cc.GetCards()[0] == 'house40/115hotel':
                        print(f"Landed on a Community Chest Space and you must pay $40 per house and $115 per hotel (${((game.GetPlayerList()[index].GetHouseCount()) * 40) + (game.GetPlayerList()[index].GetHotelCount() * 115)} total)")
                        game.GetPlayerList()[index].ChangeMoney(-(((game.GetPlayerList()[index].GetHouseCount()) * 40) + (game.GetPlayerList()[index].GetHotelCount() * 115)))
                    cc.GetCards().append(cc.GetCards()[0])
                    cc.GetCards().remove(cc.GetCards()[0])
                #### CHANCE SPACE
                elif spaces[game.GetPlayerList()[index].GetBoardPos()] == 'chance':
                    if isinstance(chance.GetCards()[0], int):
                        if chance.GetCards()[0] > 0:
                            game.GetPlayerList()[index].ChangeMoney(chance.GetCards()[0])
                            print(f"Landed on a Chance Space and gained ${chance.GetCards()[0]}!")

                        elif chance.GetCards()[0] < 0:
                            game.GetPlayerList()[index].ChangeMoney(chance.GetCards()[0])
                            print(f"Landed on a Chance Space and lost ${-(chance.GetCards()[0])}!")

                    elif chance.GetCards()[0] == 'go':
                        game.GetPlayerList()[index].SetBoardPos(0)
                        game.GetPlayerList()[index].ChangeMoney(200)
                        print("Landed on a Chance Space and advanced to Go!")

                    elif chance.GetCards()[0] == 'boardwalk':
                        game.GetPlayerList()[index].SetBoardPos(39)
                        print("Landed on a Chance Space and advanced to Boardwalk!")

                    elif chance.GetCards()[0] == 'r3':
                        game.GetPlayerList()[index].SetBoardPos(24)
                        print(f"Landed on a Chance Space and advanced to {propertyNames['r3']}!")

                    elif chance.GetCards()[0] == 'p1':
                        game.GetPlayerList()[index].SetBoardPos(11)
                        print(f"Landed on a Chance Space and advanced to {propertyNames['p1']}!")

                    elif chance.GetCards()[0] == 'closeRR':
                        if game.GetPlayerList()[index].GetBoardPos() == 22:
                            game.GetPlayerList()[index].SetBoardPos(25)
                            print(f"Landed on a Chance Space and moved to {propertyNames['rr3']}!")

                        elif game.GetPlayerList()[index].GetBoardPos() == 36:
                            game.GetPlayerList()[index].SetBoardPos(35)
                            print(f"Landed on a Chance Space and moved to {propertyNames['rr4']}!")

                        elif game.GetPlayerList()[index].GetBoardPos() == 7:
                            game.GetPlayerList()[index].SetBoardPos(5)
                            print(f"Landed on a Chance Space and moved to {propertyNames['rr1']}!")

                    elif chance.GetCards()[0] == 'closeUtil':
                        if game.GetPlayerList()[index].GetBoardPos() == 22:
                            game.GetPlayerList()[index].SetBoardPos(28)
                            print(f"Landed on a Chance Space and moved to {propertyNames['rr3']}!")

                        elif game.GetPlayerList()[index].GetBoardPos() == 36:
                            game.GetPlayerList()[index].SetBoardPos(28)
                            print(f"Landed on a Chance Space and moved to {propertyNames['rr4']}!")

                        elif game.GetPlayerList()[index].GetBoardPos() == 7:
                            game.GetPlayerList()[index].SetBoardPos(12)
                            print(f"Landed on a Chance Space and moved to {propertyNames['rr1']}!")

                    elif chance.GetCards()[0] == 'jailcard':
                        print("Landed on a Chance Space and got a Get Out of Jail Free Card!")
                        game.GetPlayerList()[index].AddJailCard(1)

                    elif chance.GetCards()[0] == 'jail':
                        print("Landed on a Chance Space and got put in jail!")
                        game.GetPlayerList()[index].PutInJail(True)

                    elif chance.GetCards()[0] == 'back3':
                        print("Landed on a Chance Space and moved back 3 spaces")
                        game.GetPlayerList()[index].AddBoardPos(-3)

                    elif chance.GetCards()[0] == '25house/100hotel':
                        print(f"Landed on a Chance Space and you must pay $25 per house and $100 per hotel (${((game.GetPlayerList()[index].GetHouseCount()) * 25) + (game.GetPlayerList()[index].GetHotelCount() * 100)} total)")
                        game.GetPlayerList()[index].ChangeMoney(-(((game.GetPlayerList()[index].GetHouseCount()) * 25) + (game.GetPlayerList()[index].GetHotelCount() * 100)))

                    elif chance.GetCards()[0] == 'readingRR':
                        print(f"Landed on a Chance Space and moved to {propertyNames['rr1']}!")
                        if game.GetPlayerList()[index].GetBoardPos() > 5:
                            print("You pass Go along the way and collect $200!")
                            game.GetPlayerList()[index].ChangeMoney(200)

                        game.GetPlayerList()[index].SetBoardPos(5)

                    elif chance.GetCards()[0] == '-50each':
                        print(f"Landed on a Chance Space and have to pay $50 to each player! (${(len(game.GetPlayerList()) - 1) * 50 } total) ")
                        payingPlayer = game.GetPlayerList()[index]
                        for owedPlayer in game.GetPlayerList():
                            payingPlayer.ChangeMoney(-50)
                            owedPlayer.ChangeMoney(50)




                if spaces[game.GetPlayerList()[index].GetBoardPos()] in game.availableProperties:
                    propIndex = game.availableProperties.index(spaces[game.GetPlayerList()[index].GetBoardPos()])
                    propObj = game.propertyObj[propIndex]
                    purchaseChoice = input(f"Would you like to buy {propertyNames[spaces[game.GetPlayerList()[index].GetBoardPos()]]} for ${propObj.cost} (y/n)")
                    if purchaseChoice.lower() == 'y':
                        if game.GetPlayerList()[index].GetMoney() >= propObj.GetCost():
                            game.GetPlayerList()[index].AddOwnedProperty(spaces[game.GetPlayerList()[index].GetBoardPos()])
                            game.availableProperties.remove(spaces[game.GetPlayerList()[index].GetBoardPos()])
                            game.propertyObj.remove(propObj)
                            game.GetPlayerList()[index].ChangeMoney(propObj.GetCost())
                            print("Property Acquired")
                        else:
                            print("Insufficient Funds!")
                elif spaces[game.GetPlayerList()[index].GetBoardPos()] in game.availableRailroads:
                    railroadIndex = game.availableRailroads.index(spaces[game.GetPlayerList()[index].GetBoardPos()])
                    railroadObj = game.railroadObj[railroadIndex]
                    purchaseChoice = input(f"Would you like to buy {propertyNames[spaces[game.GetPlayerList()[index].GetBoardPos()]]} for ${railroadObj.cost} (y/n)")
                    if purchaseChoice.lower() == 'y':
                        if game.GetPlayerList()[index].GetMoney() >= railroadObj.GetCost():
                            game.GetPlayerList()[index].AddOwnedRailroad(spaces[game.GetPlayerList()[index].GetBoardPos()])
                            game.availableRailroads.remove(spaces[game.GetPlayerList()[index].GetBoardPos()])
                            game.railroadObj.remove(railroadObj)
                            game.GetPlayerList()[index].ChangeMoney(railroadObj.GetCost())
                            print("Railroad Acquired")
                        else:
                            print("Insufficient Funds!")
                elif spaces[game.GetPlayerList()[index].GetBoardPos()] in game.taxSpaces:
                    taxIndex = game.taxSpaces.index(spaces[game.GetPlayerList()[index].GetBoardPos()])
                    taxObj = game.taxObj[taxIndex]
                    print(f"You Landed on a tax space and have to pay ${game.taxObj[taxIndex].GetTaxAmount()}!")
                    game.GetPlayerList()[index].ChangeMoney(-(game.taxObj[taxIndex].GetTaxAmount()))

                elif spaces[game.GetPlayerList()[index].GetBoardPos()] in game.availableUtility:
                    utilityIndex = game.availableUtility.index((spaces[game.GetPlayerList()[index].GetBoardPos()]))
                    utilityObj = game.utilityObj[utilityIndex]
                    purchaseChoice = input(f"Would you like to buy {propertyNames[spaces[game.GetPlayerList()[index].GetBoardPos()]]} for ${utilityObj.GetCost()}? (y/n)" )
                    if purchaseChoice.lower() == 'y':
                        if game.GetPlayerList()[index].GetMoney() >= utilityObj.GetCost():
                            game.GetPlayerList()[index].AddOwnedUtility(spaces[game.GetPlayerList()[index].GetBoardPos()])
                            game.availableUtility.remove(spaces[game.GetPlayerList()[index].GetBoardPos()])
                            game.utilityObj.remove(utilityObj)
                            game.GetPlayerList()[index].ChangeMoney(utilityObj.GetCost())

                elif spaces[game.GetPlayerList()[index].GetBoardPos()] == "jail":
                    game.GetPlayerList()[index].PutInJail(True)
                    game.GetPlayerList()[index].AddBoardPos(-20)

                ##PLAYER RENT COLLECTION
                elif not spaces[game.GetPlayerList()[index].GetBoardPos()] in game.GetPlayerList()[index].GetOwnedProperties():
                    if spaces[game.GetPlayerList()[index].GetBoardPos()] in allProperties:
                        finedPlayer = game.GetPlayerList()[index]
                        propIndex = allProperties.index(spaces[game.GetPlayerList()[index].GetBoardPos()])
                        propObj = allPropertyObj[propIndex]
                        for index, player in enumerate(game.GetPlayerList()):
                            if spaces[game.GetPlayerList()[index].GetBoardPos()] in player.GetOwnedProperties():
                                if player.GetInJail() == False:
                                    finedPlayer.ChangeMoney(-(propObj.GetRent()))
                                    player.ChangeMoney(propObj.GetRent())
                                    print(f"${propObj.GetRent()} payed to {game.GetPlayerNameList()[index]}")

                elif not spaces[game.GetPlayerList()[index].GetBoardPos()] in game.GetPlayerList()[index].GetOwnedRailroads():
                    if spaces[game.GetPlayerList()[index].GetBoardPos()] in allRailroads:
                        finedPlayer = game.GetPlayerList()[index]
                        railroadIndex = allRailroads.index(spaces[game.GetPlayerList()[index].GetBoardPos()])
                        railroadObj = allRailroadObj[railroadIndex]
                        for index, player in enumerate(game.GetPlayerList()):
                            if spaces[game.GetPlayerList()[index].GetBoardPos()] in player.GetOwnedRailroads():
                                if player.GetInJail() == False:
                                    finedPlayer.ChangeMoney(-(railroadObj.GetRent()))
                                    total = 0
                                    for i in range(len(player.GetOwnedRailroads())):
                                        total += railroadObj.GetRent() * 2
                                    player.ChangeMoney(railroadObj.GetRent())
                                    print(f"${railroadObj.GetRent()} payed to {game.GetPlayerNameList()[index]} for landing on their Railroad Property")

                elif not spaces[game.GetPlayerList()[index].GetBoardPos()] in game.GetPlayerList()[index].GetOwnedUtility():
                    if spaces[game.GetPlayerList()[index].GetBoardPos()] in allUtility:
                        finedPlayer = game.GetPlayerList()[index]
                        utilityIndex = allUtility.index(spaces[game.GetPlayerList()[index].GetBoardPos()])
                        utilityObj = allUtilityObj[utilityIndex]
                        for index, player in enumerate(game.GetPlayerList()):
                            if spaces[game.GetPlayerList()[index].GetBoardPos()] in player.GetOwnedUtility():
                                if player.GetInJail() == False:
                                    if len(player.GetOwnedUtility()) == 1:
                                        totalCharge = dice.RollDice() * 4
                                        finedPlayer.ChangeMoney(-totalCharge)
                                        player.ChangeMoney(totalCharge)
                                    elif len(player.GetOwnedUtility()) == 2:
                                        totalCharge = dice.RollDice() * 10
                                        finedPlayer.ChangeMoney(-totalCharge)
                                        player.ChangeMoney(totalCharge)
                                    print(f"Payed ${totalCharge} to {game.GetPlayerNameList()[index]} for landing on their Utility Property")



            else:
                poop = input(f"{game.GetPlayerNameList()[index]}'s Turn (Press Enter to Continue)")
                print("You Are In Jail!")
                if game.GetPlayerList()[index].GetJailCards() > 0:
                    print("You Used Your Get Out of Jail Free Card to escape!")
                    game.GetPlayerList()[index].AddJailCard(-1)
                    game.GetPlayerList()[index].PutInJail(False)

                elif game.GetPlayerList()[index].GetJailCount() < 3:
                    jailChoice = input("Would you like to try to roll doubles to escape jail or pay $50? (pay/roll): ")
                    if jailChoice.lower() == 'pay':
                        game.GetPlayerList()[index].PutInJail(False)
                        game.GetPlayerList()[index].ChangeMoney(-50)
                        print("You payed $50 to escape jail")
                        game.GetPlayerList()[index].SetJailCount(0)
                    elif jailChoice.lower() == 'roll':
                        dice.RollDice()
                        if dice.GetDice1() == dice.GetDice2():
                            game.GetPlayerList()[index].PutInJail(False)
                            print(f"You rolled double {dice.GetDice1}'s to escape jail!")
                            game.GetPlayerList()[index].SetJailCount(0)
                        else:
                            print(f"You did not roll doubles, {3 - game.GetPlayerList()[index].GetJailCount()} attempts left")

                if game.GetPlayerList()[index].GetJailCount() == 3:
                    game.GetPlayerList()[index].PutInJail(False)
                    game.GetPlayerList()[index].ChangeMoney(-50)
                    print("You payed $50 to escape jail")
                    game.GetPlayerList()[index].SetJailCount(0)

def main():
    board = Board()
    run = True
    board.CreateBoard()
    PlayerInit()
    PropertyInit()
    PlayGame()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()


if __name__ == '__main__':
    game = Game()
    dice = Dice()
    main()
