import random

deck = [["" for a in range(2)] for b in range(52)]
deck[0][0], deck[0][1] = "Ace", "Spade"
deck[1][0], deck[1][1] = "Ace", "Club"
deck[2][0], deck[2][1] = "Ace", "Heart"
deck[3][0], deck[3][1] = "Ace", "Diamond"
deck[4][0], deck[4][1] = "2", "Spade"
deck[5][0], deck[5][1] = "2", "Club"
deck[6][0], deck[6][1] = "2", "Heart"
deck[7][0], deck[7][1] = "2", "Diamond"
deck[8][0], deck[8][1] = "3", "Spade"
deck[9][0], deck[9][1] = "3", "Club"
deck[10][0], deck[10][1] = "3", "Heart"
deck[11][0], deck[11][1] = "3", "Diamond"
deck[12][0], deck[12][1] = "4", "Spade"
deck[13][0], deck[13][1] = "4", "Club"
deck[14][0], deck[14][1] = "4", "Heart"
deck[15][0], deck[15][1] = "4", "Diamond"
deck[16][0], deck[16][1] = "5", "Spade"
deck[17][0], deck[17][1] = "5", "Club"
deck[18][0], deck[18][1] = "5", "Heart"
deck[19][0], deck[19][1] = "5", "Diamond"
deck[20][0], deck[20][1] = "6", "Spade"
deck[21][0], deck[21][1] = "6", "Club"
deck[22][0], deck[22][1] = "6", "Heart"
deck[23][0], deck[23][1] = "6", "Diamond"
deck[24][0], deck[24][1] = "7", "Spade"
deck[25][0], deck[25][1] = "7", "Club"
deck[26][0], deck[26][1] = "7", "Heart"
deck[27][0], deck[27][1] = "7", "Diamond"
deck[28][0], deck[28][1] = "8", "Spade"
deck[29][0], deck[29][1] = "8", "Club"
deck[30][0], deck[30][1] = "8", "Heart"
deck[31][0], deck[31][1] = "8", "Diamond"
deck[32][0], deck[32][1] = "9", "Spade"
deck[33][0], deck[33][1] = "9", "Club"
deck[34][0], deck[34][1] = "9", "Heart"
deck[35][0], deck[35][1] = "9", "Diamond"
deck[36][0], deck[36][1] = "10", "Spade"
deck[37][0], deck[37][1] = "10", "Club"
deck[38][0], deck[38][1] = "10", "Heart"
deck[39][0], deck[39][1] = "10", "Diamond"
deck[40][0], deck[40][1] = "Jack", "Spade"
deck[41][0], deck[41][1] = "Jack", "Club"
deck[42][0], deck[42][1] = "Jack", "Heart"
deck[43][0], deck[43][1] = "Jack", "Diamond"
deck[44][0], deck[44][1] = "Queen", "Spade"
deck[45][0], deck[45][1] = "Queen", "Club"
deck[46][0], deck[46][1] = "Queen", "Heart"
deck[47][0], deck[47][1] = "Queen", "Diamond"
deck[48][0], deck[48][1] = "King", "Spade"
deck[49][0], deck[49][1] = "King", "Club"
deck[50][0], deck[50][1] = "King", "Heart"
deck[51][0], deck[51][1] = "King", "Diamond"
random.shuffle(deck)
player1Hand = []
player2Hand = []
player1Hand.append(deck.pop())
player2Hand.append(deck.pop())
player1Hand.append(deck.pop())
player2Hand.append(deck.pop())
player1Hand.append(deck.pop())
player2Hand.append(deck.pop())
player1Hand.append(deck.pop())
player2Hand.append(deck.pop())
player1Hand.append(deck.pop())
player2Hand.append(deck.pop())
player1Hand.append(deck.pop())
player2Hand.append(deck.pop())
player1Hand.append(deck.pop())
player2Hand.append(deck.pop())
player1Fours = []
player2Fours = []

def generalPlayer(playerHand, playerFours, playerNumber):
    turn = True
    while turn == True:
        print("\nPlayer " + str(playerNumber) + "'s hand")
        print("\n".join(str(i) for i in playerHand))
        request = input("\nWhat cards do you need? ")
        if sum(card.count(request) for card in playerHand) == 0:
            print("\nYou need at least one", request, "to ask for more.")
            continue

        if playerNumber == 1:
            print("\nPlayer 1: Player 2, do you have any " + request + "s?")
            if sum(card.count(request) for card in player2Hand) > 0:
                print("\nPlayer 2: Yes, I have", sum(card.count(request) for card in player2Hand), ".")
                for card in player2Hand:
                    if card[0] == request:
                        playerHand.append(player2Hand.pop(player2Hand.index(card)))
   
                now = input("\nType anything when you're ready to contiinue. ")
                if now == ""  or now != "":
                    continue

            else:
                print("\nPlayer 2: Go fish.")
                playerHand.append(deck.pop())
                if playerHand[-1][0] == request:
                    continue

                else:
                    turn = False

        else:
            print("\nPlayer 2: Player 1, do you have any " + request + "s?")
            if sum(card.count(request) for card in player1Hand) > 0:
                print("\nPlayer 1: Yes, I have ", sum(card.count(request) for card in player1Hand), ".")
                for card in player1Hand:
                    if card[0] == request:
                        playerHand.append(player1Hand.pop(player1Hand.index(card)))
   
                now = input("\nType anything when you're ready to contiinue. ")
                if now == ""  or now != "":
                    continue

            else:
                print("\nPlayer 1: Go fish.")
                playerHand.append(deck.pop(-1))
                if playerHand[-1][0] == request:
                    continue

                else:
                    turn = False 
        
        if sum(card.count("2") for card in playerHand) == 4: 
            for card in playerHand:
                if playerHand[card][0] == "2":
                    playerFours.append(playerHand.pop(playerHand.index(card)))

        if sum(card.count("3") for card in playerHand) == 4: 
            for card in playerHand:
                if playerHand[card][0] == "3":
                    playerFours.append(playerHand.pop(playerHand.index(card)))

        if sum(card.count("4") for card in playerHand) == 4: 
            for card in playerHand: 
                if playerHand[card][0] == "4":
                    playerFours.append(playerHand.pop(playerHand.index(card)))

        if sum(card.count("5") for card in playerHand) == 4: 
            for card in playerHand:
                if playerHand[card][0] == "5":
                    playerFours.append(playerHand.pop(playerHand.index(card))) 

        if sum(card.count("6") for card in playerHand) == 4: 
            for card in playerHand:
                if playerHand[card][0] == "6":
                    playerFours.append(playerHand.pop(playerHand.index(card)))

        if sum(card.count("7") for card in playerHand) == 4: 
            for card in playerHand:
                if playerHand[card][0] == "7":
                    playerFours.append(playerHand.pop(playerHand.index(card)))

        if sum(card.count("8") for card in playerHand) == 4: 
            for card in playerHand:
                if playerHand[card][0] == "8":
                    playerFours.append(playerHand.pop(playerHand.index(card)))

        if sum(card.count("9") for card in playerHand) == 4: 
            for card in playerHand:
                if playerHand[card][0] == "9":
                    playerFours.append(playerHand.pop(playerHand.index(card)))

        if sum(card.count("10") for card in playerHand) == 4: 
            for card in playerHand:
                if playerHand[card][0] == "10":
                    playerFours.append(playerHand.pop(playerHand.index(card)))

        if sum(card.count("Jack") for card in playerHand) == 4: 
            for card in playerHand:
                if playerHand[card][0] == "Jack":
                    playerFours.append(playerHand.pop(playerHand.index(card)))

        if sum(card.count("Queen") for card in playerHand) == 4: 
            for card in playerHand:
                if playerHand[card][0] == "Queen":
                    playerFours.append(playerHand.pop(playerHand.index(card)))

        if sum(card.count("King") for card in playerHand) == 4: 
            for card in playerHand:
                if playerHand[card][0] == "King":
                    playerFours.append(playerHand.pop(playerHand.index(card)))

        if sum(card.count("Ace") for card in playerHand) == 4: 
            for card in playerHand:
                if playerHand[card][0] == "Ace":
                    playerFours.append(playerHand.pop(playerHand.index(card)))   

def playGoFish():
    finished = False
    while finished == False:
        generalPlayer(player1Hand, player1Fours, 1)
        generalPlayer(player2Hand, player2Fours, 2)
        if len(deck) == 0 or len(player1Hand) == 0 or len(player2Hand) == 0:
            if len(player1Fours) > len(player2Fours):
                print("Player 1 wins!")
                finished = True

            elif len(player2Fours) > len(player1Fours):
                print("Player 2 wins!")
                finished = True

            else:
                print("It's a tie.")
                finished = True

        else:
            continue

playGoFish()