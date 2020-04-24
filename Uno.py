"""
0: 1 of every color
1-9, Draw 2, Skip, Reverse: 2 of every color
Wild, Wild Draw 4: 4
108 cards
7 cards in your hand
2 players
"""

import random

#Make and shuffle the deck
row, column = 108, 2
deck = [["" for i in range(column)] for j in range(row)]
deck[0][0], deck[0][1] = "0", "Red"
deck[1][0], deck[1][1] = "0", "Blue"
deck[2][0], deck[2][1] = "0", "Yellow"
deck[3][0], deck[3][1] = "0", "Green"
deck[4][0], deck[4][1] = "1", "Red"
deck[5][0], deck[5][1] = "1", "Red"
deck[6][0], deck[6][1] = "1", "Blue"
deck[7][0], deck[7][1] = "1", "Blue"
deck[8][0], deck[8][1] = "1", "Yellow"
deck[9][0], deck[9][1] = "1", "Yellow"
deck[10][0], deck[10][1] = "1", "Green"
deck[11][0], deck[11][1] = "1", "Green"
deck[12][0], deck[12][1] = "2", "Red"
deck[13][0], deck[13][1] = "2", "Red"
deck[14][0], deck[14][1] = "2", "Blue"
deck[15][0], deck[15][1] = "2", "Blue"
deck[16][0], deck[16][1] = "2", "Yellow"
deck[17][0], deck[17][1] = "2", "Yellow"
deck[18][0], deck[18][1] = "2", "Green"
deck[19][0], deck[19][1] = "2", "Green"
deck[20][0], deck[20][1] = "3", "Red"
deck[21][0], deck[21][1] = "3", "Red"
deck[22][0], deck[22][1] = "3", "Blue"
deck[23][0], deck[23][1] = "3", "Blue"
deck[24][0], deck[24][1] = "3", "Yellow"
deck[25][0], deck[25][1] = "3", "Yellow"
deck[26][0], deck[26][1] = "3", "Green"
deck[27][0], deck[27][1] = "3", "Green"
deck[28][0], deck[28][1] = "4", "Red"
deck[29][0], deck[29][1] = "4", "Red"
deck[30][0], deck[30][1] = "4", "Blue"
deck[31][0], deck[31][1] = "4", "Blue"
deck[32][0], deck[32][1] = "4", "Yellow"
deck[33][0], deck[33][1] = "4", "Yellow"
deck[34][0], deck[34][1] = "4", "Green"
deck[35][0], deck[35][1] = "4", "Green"
deck[36][0], deck[36][1] = "5", "Red"
deck[37][0], deck[37][1] = "5", "Red"
deck[38][0], deck[38][1] = "5", "Blue"
deck[39][0], deck[39][1] = "5", "Blue"
deck[40][0], deck[40][1] = "5", "Yellow"
deck[41][0], deck[41][1] = "5", "Yellow"
deck[42][0], deck[42][1] = "5", "Green"
deck[43][0], deck[43][1] = "5", "Green"
deck[44][0], deck[44][1] = "6", "Red"
deck[45][0], deck[45][1] = "6", "Red"
deck[46][0], deck[46][1] = "6", "Blue"
deck[47][0], deck[47][1] = "6", "Blue"
deck[48][0], deck[48][1] = "6", "Yellow"
deck[49][0], deck[49][1] = "6", "Yellow"
deck[50][0], deck[50][1] = "6", "Green"
deck[51][0], deck[51][1] = "6", "Green"
deck[52][0], deck[52][1] = "7", "Red"
deck[53][0], deck[53][1] = "7", "Red"
deck[54][0], deck[54][1] = "7", "Blue"
deck[55][0], deck[55][1] = "7", "Blue"
deck[56][0], deck[56][1] = "7", "Yellow"
deck[57][0], deck[57][1] = "7", "Yellow"
deck[58][0], deck[58][1] = "7", "Green"
deck[59][0], deck[59][1] = "7", "Green"
deck[60][0], deck[60][1] = "8", "Red"
deck[61][0], deck[61][1] = "8", "Red"
deck[62][0], deck[62][1] = "8", "Blue"
deck[63][0], deck[63][1] = "8", "Blue"
deck[64][0], deck[64][1] = "8", "Yellow"
deck[65][0], deck[65][1] = "8", "Yellow"
deck[66][0], deck[66][1] = "8", "Green"
deck[67][0], deck[67][1] = "8", "Green"
deck[68][0], deck[68][1] = "9", "Red"
deck[69][0], deck[69][1] = "9", "Red"
deck[70][0], deck[70][1] = "9", "Blue"
deck[71][0], deck[71][1] = "9", "Blue"
deck[72][0], deck[72][1] = "9", "Yellow"
deck[73][0], deck[73][1] = "9", "Yellow"
deck[74][0], deck[74][1] = "9", "Green"
deck[75][0], deck[75][1] = "9", "Green"
deck[76][0], deck[76][1] = "Draw 2", "Red"
deck[77][0], deck[77][1] = "Draw 2", "Red"
deck[78][0], deck[78][1] = "Draw 2", "Blue"
deck[79][0], deck[79][1] = "Draw 2", "Blue"
deck[80][0], deck[80][1] = "Draw 2", "Yellow"
deck[81][0], deck[81][1] = "Draw 2", "Yellow"
deck[82][0], deck[82][1] = "Draw 2", "Green"
deck[83][0], deck[83][1] = "Draw 2", "Green"
deck[84][0], deck[84][1] = "Skip", "Red"
deck[85][0], deck[85][1] = "Skip", "Red"
deck[86][0], deck[86][1] = "Skip", "Blue"
deck[87][0], deck[87][1] = "Skip", "Blue"
deck[88][0], deck[88][1] = "Skip", "Yellow"
deck[89][0], deck[89][1] = "Skip", "Yellow"
deck[90][0], deck[90][1] = "Skip", "Green"
deck[91][0], deck[91][1] = "Skip", "Green"
deck[92][0], deck[92][1] = "Reverse", "Red"
deck[93][0], deck[93][1] = "Reverse", "Red"
deck[94][0], deck[94][1] = "Reverse", "Blue"
deck[95][0], deck[95][1] = "Reverse", "Blue"
deck[96][0], deck[96][1] = "Reverse", "Yellow"
deck[97][0], deck[97][1] = "Reverse", "Yellow"
deck[98][0], deck[98][1] = "Reverse", "Green"
deck[99][0], deck[99][1] = "Reverse", "Green"
deck[100][0], deck[100][1] = "Wild", ""
deck[101][0], deck[101][1] = "Wild", ""
deck[102][0], deck[102][1] = "Wild", ""
deck[103][0], deck[103][1] = "Wild", ""
deck[104][0], deck[104][1] = "Wild Draw 4", ""
deck[105][0], deck[105][1] = "Wild Draw 4", ""
deck[106][0], deck[106][1] = "Wild Draw 4", ""
deck[107][0], deck[107][1] = "Wild Draw 4", ""
random.shuffle(deck)
player1Hand = [deck.pop(0), deck.pop(0), deck.pop(0), deck.pop(0), deck.pop(0), deck.pop(0), deck.pop(0)]
player2Hand = [deck.pop(0), deck.pop(0), deck.pop(0), deck.pop(0), deck.pop(0), deck.pop(0), deck.pop(0)]
discard = [deck.pop(0)]

def playUno():
    finished = False
    while finished == False:
        player1Turn()
        if len(player1Hand) == 0:
            print("Player 1 wins!")
            finished = True
        
        player2Turn()
        if len(player2Hand) == 0:
            print("Player 2 wins!")
            finished = True
    
def player1Turn():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    if len(player1Hand) == 1:
            print("Player 1 has Uno!")

    if len(player2Hand) == 1:
            print("Player 2 has Uno!")
    turn = True
    while turn == True:
        print("Player 1's Hand")
        print("\n".join(str(i) for i in player1Hand))
        print("\n")
        print("Discard Card: ", discard)
        card = input("What card do you want to play? (from 1 to the size of your hand or 'draw' if you can't play a card) ")
        if card != "draw" and int(card) in range(0, len(player1Hand) + 1):
            actualCard = player1Hand[int(card) - 1]
            print("You are going to play ", actualCard)

        elif card == "draw":
            player1Hand.append(deck.pop(0))
            continue

        else:
            print("You must type a number from 1 to the number of cards in your or hand or 'draw.'")
            continue
        
        if actualCard[0] == "Wild":
            newColor = input("To what color do you want to change it? ")
            if newColor == "Red" or newColor == "red" or newColor == "r":
                actualCard[1] = "Red"
                discard[0] = player1Hand.pop(int(card) - 1)
                turn = False

            elif newColor == "Blue" or newColor == "blue" or newColor == "b":
                actualCard[1] = "Blue"
                discard[0] = player1Hand.pop(int(card) - 1)
                turn = False

            elif newColor == "Yellow" or newColor == "yellow" or newColor == "y":
                actualCard[1] = "Yellow"
                discard[0] = player1Hand.pop(int(card) - 1)
                turn = False

            else:
                actualCard[1] = "Green"
                discard[0] = player1Hand.pop(int(card) - 1)
                turn = False

        elif actualCard[0] == "Wild Draw 4":
            newColor = input("To what color do you want to change it? ")
            if newColor == "Red" or newColor == "red" or newColor == "r":
                actualCard[1] = "Red"
                discard[0] = player1Hand.pop(int(card) - 1)
                player2Hand.append(deck.pop(0))
                player2Hand.append(deck.pop(0))
                player2Hand.append(deck.pop(0))
                player2Hand.append(deck.pop(0))
                continue

            elif newColor == "Blue" or newColor == "blue" or newColor == "b":
                actualCard[1] = "Blue"
                discard[0] = player1Hand.pop(int(card) - 1)
                player2Hand.append(deck.pop(0))
                player2Hand.append(deck.pop(0))
                player2Hand.append(deck.pop(0))
                player2Hand.append(deck.pop(0))
                continue

            elif newColor == "Yellow" or newColor == "yellow" or newColor == "y":
                actualCard[1] = "Yellow"
                discard[0] = player1Hand.pop(int(card) - 1)
                player2Hand.append(deck.pop(0))
                player2Hand.append(deck.pop(0))
                player2Hand.append(deck.pop(0))
                player2Hand.append(deck.pop(0))
                continue

            else:
                actualCard[1] = "Green"
                discard[0] = player1Hand.pop(int(card) - 1)
                player2Hand.append(deck.pop(0))
                player2Hand.append(deck.pop(0))
                player2Hand.append(deck.pop(0))
                player2Hand.append(deck.pop(0))
                continue

        elif actualCard[0] == "Skip" or actualCard[0] == "Reverse":
            if actualCard[0] == discard[0][0] or actualCard[1] == discard[0][1]:
                discard[0] = player1Hand.pop(int(card) - 1)
                continue

        elif actualCard[0] == "Draw 2":
            if actualCard[0] == discard[0][0] or actualCard[1] == discard[0][1]:
                discard[0] = player1Hand.pop(int(card) - 1)
                player2Hand.append(deck.pop(0))
                player2Hand.append(deck.pop(0))
                continue

        elif actualCard[0] == "0" or actualCard[0] == "1" or actualCard[0] == "2" or actualCard[0] == "3" or actualCard[0] == "4" or actualCard[0] == "5" or actualCard[0] == "6" or actualCard[0] == "7" or actualCard[0] == "8" or actualCard[0] == "9":
            if actualCard[0] == discard[0][0] or actualCard[1] == discard[0][1]:
                discard[0] = player1Hand.pop(int(card) - 1)
                turn = False

        else:
            print("You must type a number from 1 to the number of cards in your or hand or 'draw.'")
            continue

def player2Turn():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    if len(player1Hand) == 1:
            print("Player 1 has Uno!")

    if len(player2Hand) == 1:
            print("Player 2 has Uno!")

    turn = True
    while turn == True:
        print("Player 2's Hand")
        print("\n".join(str(i) for i in player2Hand))
        print("\n")
        print("Discard Card: ", discard)
        card = input("What card do you want to play? (from 1 to the size of your hand or 'draw' if you can't play a card) ")
        if card != "draw" and int(card) in range(0, len(player2Hand) + 1):
            actualCard = player2Hand[int(card) - 1]
            print("You are going to play ", actualCard)

        elif card == "draw":
            player2Hand.append(deck.pop(0))
            continue

        else:
            print("You must type a number from 1 to the number of cards in your or hand or 'draw.'")
            continue
        
        if actualCard[0] == "Wild":
            newColor = input("To what color do you want to change it? ")
            if newColor == "Red" or newColor == "red" or newColor == "r":
                actualCard[1] = "Red"
                discard[0] = player2Hand.pop(int(card) - 1)
                turn = False

            elif newColor == "Blue" or newColor == "blue" or newColor == "b":
                actualCard[1] = "Blue"
                discard[0] = player2Hand.pop(int(card) - 1)
                turn = False

            elif newColor == "Yellow" or newColor == "yellow" or newColor == "y":
                actualCard[1] = "Yellow"
                discard[0] = player2Hand.pop(int(card) - 1)
                turn = False

            else:
                actualCard[1] = "Green"
                discard[0] = player2Hand.pop(int(card) - 1)
                turn = False

        elif actualCard[0] == "Wild Draw 4":
            newColor = input("To what color do you want to change it? ")
            if newColor == "Red" or newColor == "red" or newColor == "r":
                actualCard[1] = "Red"
                discard[0] = player2Hand.pop(int(card) - 1)
                player1Hand.append(deck.pop(0))
                player1Hand.append(deck.pop(0))
                player1Hand.append(deck.pop(0))
                player1Hand.append(deck.pop(0))
                continue

            elif newColor == "Blue" or newColor == "blue" or newColor == "b":
                actualCard[1] = "Blue"
                discard[0] = player2Hand.pop(int(card) - 1)
                player1Hand.append(deck.pop(0))
                player1Hand.append(deck.pop(0))
                player1Hand.append(deck.pop(0))
                player1Hand.append(deck.pop(0))
                continue

            elif newColor == "Yellow" or newColor == "yellow" or newColor == "y":
                actualCard[1] = "Yellow"
                discard[0] = player2Hand.pop(int(card) - 1)
                player1Hand.append(deck.pop(0))
                player1Hand.append(deck.pop(0))
                player1Hand.append(deck.pop(0))
                player1Hand.append(deck.pop(0))
                continue

            else:
                actualCard[1] = "Green"
                discard[0] = player2Hand.pop(int(card) - 1)
                player1Hand.append(deck.pop(0))
                player1Hand.append(deck.pop(0))
                player1Hand.append(deck.pop(0))
                player1Hand.append(deck.pop(0))
                continue

        elif actualCard[0] == "Skip" or actualCard[0] == "Reverse":
            if actualCard[0] == discard[0][0] or actualCard[1] == discard[0][1]:
                discard[0] = player2Hand.pop(int(card) - 1)
                continue

        elif actualCard[0] == "Draw 2":
            if actualCard[0] == discard[0][0] or actualCard[1] == discard[0][1]:
                discard[0] = player2Hand.pop(int(card) - 1)
                player1Hand.append(deck.pop(0))
                player1Hand.append(deck.pop(0))
                continue

        elif actualCard[0] == "0" or actualCard[0] == "1" or actualCard[0] == "2" or actualCard[0] == "3" or actualCard[0] == "4" or actualCard[0] == "5" or actualCard[0] == "6" or actualCard[0] == "7" or actualCard[0] == "8" or actualCard[0] == "9":
            if actualCard[0] == discard[0][0] or actualCard[1] == discard[0][1]:
                discard[0] = player2Hand.pop(int(card) - 1)
                turn = False

        else:
            print("You must type a number from 1 to the number of cards in your or hand or 'draw.'")
            continue

playUno()
