import random

"""
Ride the Tide ia a card game in Casino Island to Go where you guess whether the next card is higher or lower to get 6 correct gueeses in a row. Aces are high.
In Casino Island to Go, you lose if the next card has the same value, but you don't in my version.
You can stand at anytime, and if you get more correct guesses in a row than the delaer, you win.
"""

#Make and shuffle the deck
row, column = (52, 2)
deck = [["" for i in range(column)] for j in range(row)]
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
player3Hand = []
dealerHand = []
def playRideTheTide():
    numberOfPlayers = input("How many players are there from 1 to 3 except the dealer? ")
    if numberOfPlayers == "1":
        player1Turn()
        dealerTurn()
        print("\n")
        if player1Hand == [] and dealerHand == []:
            print("\nPlayer 1 and the dealer guessed wrong.")
        
        else:
            if len(player1Hand) == 6:
                print("Player 1 rides the tide!")
            
            elif player1Hand == []:
                print("\nPlayer 1 guessed wrong.")
                print("The dealer wins.")

            elif dealerHand == []:
                print("The dealer guessed wrong.")
                print("Player 1 wins!")

            else:
                print("\nPlayer 1's correct guesses: ", len(player1Hand))
                print("The dealer's correct guesses: ", len(dealerHand))
                if len(player1Hand) > len(dealerHand):
                    print("Player 1 wins!")

                elif len(player1Hand) == len(dealerHand):
                    print("Player 1 ties.")

                else:
                    print("Player 1 loses.")

    elif numberOfPlayers == "2":
        player1Turn()
        player2Turn()
        dealerTurn()
        print("\n")
        if player1Hand == [] and player2Hand == [] and dealerHand == []:
            print("\nPlayer 1, player 2, and the dealer guessed wrong.")
        
        else:
            if len(player1Hand) == 6:
                if len(player2Hand) == 6:
                    print("Player 1 and player 2 ride the tide!")
                    return

                else:
                    print("Player 1 rides the tide!")

            elif player2Hand == 6:
                print("Player 2 rides the tide!")

            else:
                print("Neither player 1 nor player 2 rides the tide.")

            if player1Hand == [] and player2Hand != [] and dealerHand != []:
                print("\nPlayer 1 guessed wrong.")
                print("Player 2's correct guesses: ", len(player2Hand))
                print("The dealer's correct guesses: ", len(dealerHand))
                if len(player2Hand) > len(dealerHand):
                    if len(player2Hand) != 6:
                        print("Player 2 wins!")

                elif len(player2Hand == len(dealerHand)):
                    if len(player2Hand) != 6:
                        print("Player 2 ties.")

                else:
                    print("Player 2 loses.")

            elif player1Hand != [] and player2Hand == [] and dealerHand != []:
                print("\nPlayer 2 guessed wrong.")
                print("\nPlayer 1's correct guesses: ", len(player1Hand))
                print("The dealer's correct guesses: ", len(dealerHand))
                if len(player1Hand) > len(dealerHand):
                    if len(player1Hand) != 6:
                        print("Player 1 wins!")

                elif len(player1Hand == len(dealerHand)):
                    if len(player1Hand) != 6:
                        print("Player 1 ties.")

                else:
                    print("Player 1 loses.")
            
            elif player1Hand != [] and player2Hand != [] and  dealerHand == []:
                print("The dealer guessed wrong.")
                if len(player1Hand) != 6:
                    if len(player2Hand) != 6:
                        print("Player 1 and player 2 win!")

                    else:
                        print("Player 1 wins!")

            elif player1Hand == [] and player2Hand == [] and dealerHand != []:
                print("Player 1 and player 2 guessed wrong.")
                print("The dealer wins.")

            elif player1Hand == [] and player2Hand != [] and dealerHand == []:
                print("Player 1 and the dealer guessed wrong.")
                if len(player2Hand) != 6:
                    print("Player 2 wins!")

            elif player1Hand != [] and player2Hand == [] and dealerHand == []:
                print("Player 2 and the dealer guessed wrong.")
                if len(player1Hand) != 6:
                    print("Player 1 wins!")

            else:
                print("Player 1's correct guesses: ", len(player1Hand))
                print("Player 2's correct guesses: ", len(player2Hand))
                print("The dealer's correct guesses: ", len(dealerHand))
                if len(player1Hand) > len(dealerHand):
                    if len(player1Hand) != 6:
                        print("Player 1 wins!")

                elif len(player1Hand) == len(dealerHand):
                    if len(player1Hand) != 6:
                        print("Player 1 ties.")

                else:
                        print("Player 1 loses.")

                if len(player2Hand) > len(dealerHand):
                    if len(player2Hand) != 6:
                        print("Player 2 wins!")

                elif len(player2Hand) == len(dealerHand):
                    if len(player2Hand) != 6:
                        print("Player 2 ties.")

                else:
                    print("Player 2 loses.")

    elif numberOfPlayers == "3":
        player1Turn()
        player2Turn()
        player3Turn()
        dealerTurn()
        print("\n")
        if player1Hand == [] and player2Hand == [] and player3Hand == [] and dealerHand == []:
            print("\nPlayer 1, player 2, player 3, and the dealer guessed wrong.")
        
        else:
            if len(player1Hand) == 6:
                if len(player2Hand) == 6:
                    if len(player3Hand) == 6:
                        print("Player 1, player 2, and player 3 ride the tide!")
                        return

                    else:
                        print("Player 1 and player 2 ride the tide!")

                elif len(player3Hand) == 6:
                    print("Player 1 and player 3 ride the tide!")

                else:
                    print("Player 1 rides the tide!")

            elif len(player2Hand) == 6:
                if len(player3Hand) == 6:
                    print("Player 2 and player 3 ride the tide!")

                else:
                    print("Player 2 rides the tide!")

            elif len(player3Hand) == 6:
                print("Player 3 rides the tide!")

            else:
                print("Neither player 1, player 2, nor player 3 rides the tide.")
            
            if player1Hand == [] and player2Hand != [] and player3Hand != [] and dealerHand != []:
                print("\nPlayer 1 guessed wrong.")
                print("Player 2's correct guesses: ", len(player2Hand))
                print("Player 3's correct guesses: ", len(player3Hand))
                print("The dealer's correct guesses: ", len(dealerHand))
                if len(player2Hand) > len(dealerHand):
                    if len(player2Hand) != 6:
                        print("Player 2 wins!")

                elif len(player2Hand) == len(dealerHand):
                    if len(player2Hand) != 6:
                        print("Player 2 ties.")

                else:
                    print("Player 2 loses.")

                if len(player3Hand) > len(dealerHand):
                    if len(player3Hand) != 6:
                        print("Player 3 wins!")

                elif len(player3Hand) == len(dealerHand):
                    if len(player3Hand) != 6:
                        print("Player 3 ties.")

                else:
                    print("Player 3 loses.")

            elif player1Hand != [] and player2Hand == [] and player3Hand != [] and dealerHand != []:
                print("\nPlayer 2 guessed wrong.")
                print("Player 1's correct guesses: ", len(player1Hand))
                print("Player 3's correct guesses: ", len(player3Hand))
                print("The dealer's correct guesses: ", len(dealerHand))
                if len(player1Hand) > len(dealerHand):
                    if len(player1Hand) != 6:
                        print("Player 1 wins!")

                elif len(player1Hand) == len(dealerHand):
                    if len(player1Hand) != 6:
                        print("Player 1 ties.")

                else:
                    print("Player 1 loses.")

                if len(player3Hand) > len(dealerHand):
                    if len(player3Hand) != 6:
                        print("Player 3 wins!")

                elif len(player3Hand) == len(dealerHand):
                    if len(player3Hand) != 6:
                        print("Player 3 ties.")

                else:
                    print("Player 3 loses.")

            elif player1Hand != [] and player2Hand != [] and player3Hand == [] and dealerHand != []:
                print("\nPlayer 3 guessed wrong.")
                print("\nPlayer 1's correct guesses: ", len(player1Hand))
                print("Player 2's correct guesses: ", len(player2Hand))
                print("The dealer's correct guesses: ", len(dealerHand))
                if len(player1Hand) > len(dealerHand):
                    if len(player1Hand) != 6:
                        print("Player 1 wins!")

                elif len(player1Hand) == len(dealerHand):
                    if len(player1Hand) != 6:
                        print("Player 1 ties.")

                else:
                    print("Player 1 loses.")

                if len(player2Hand) > len(dealerHand):
                    if len(player2Hand) != 6:
                        print("Player 2 wins!")

                elif len(player2Hand) == len(dealerHand):
                    if len(player2Hand) != 6:
                        print("Player 2 ties.")

                else:
                    print("Player 2 loses.")
            
            elif player1Hand != [] and player2Hand != [] and player3Hand != [] and  dealerHand == []:
                print("The dealer guessed wrong.")
                if len(player1Hand) != 6:
                    if len(player2Hand) != 6:
                        if len(player3Hand) != 6:
                            print("Player 1, player 2, and player 3 win!")

                        else:
                            print("Player 1 and player 2 win!")

                    else:
                        print("Player 1 wins!")

                elif len(player2Hand) != 6:
                    if len(player3Hand) != 6:
                        print("Player 2 and plyer 3 win!")

                    else:
                        print("Player 2 wins!")

                elif len(player3Hand) != 6:
                    print("Player 3 wins!")


            elif player1Hand == [] and player2Hand == [] and player3Hand == [] and dealerHand != []:
                print("Player 1, player 2, and player 3 guessed wrong.")
                print("The dealer wins.")

            elif player1Hand == [] and player2Hand != [] and player3Hand != [] and dealerHand == []:
                print("Player 1 and the dealer guessed wrong.")
                if len(player2Hand) != 6:
                    if len(player3Hand) != 6:
                        print("Player 2 and player 3 win!")

                    else:
                        print("Player 2 wins!")

                elif len(player3Hand) != 6:
                    print("Player 3 wins!")

            elif player1Hand != [] and player2Hand == [] and player3Hand != [] and dealerHand == []:
                print("Player 2 and the dealer guessed wrong.")
                if len(player1Hand) != 6:
                    if len(player3Hand) != 6:
                        print("Player 1 and player 3 win!")

                    else:
                        print("Player 1 wins!")

                elif len(player3Hand) != 6:
                    print("Player 3 wins!")

            elif player1Hand != [] and player2Hand != [] and player3Hand == [] and dealerHand == []:
                print("Player 3 and the dealer guessed wrong.")
                if len(player1Hand) != 6:
                    if len(player2Hand) != 6:
                        print("Player 1 and player 2 win!")

                    else:
                        print("Player 1 wins!")

                elif len(player2Hand) != 6:
                    print("Player 2 wins!")

            elif player1Hand != [] and player2Hand == [] and player3Hand == [] and dealerHand == []:
                print("Player 2, player 3, and the dealer guessed wrong.")
                if len(player1Hand) != 6:
                    print("Player 1 wins!")
                
            elif player1Hand == [] and player2Hand != [] and player3Hand == [] and dealerHand == []:
                print("Player 1, player 3, and the dealer guessed wrong.")
                if len(player2Hand) != 6:
                    print("Player 2 wins!")

            elif player1Hand == [] and player2Hand == [] and player3Hand != [] and dealerHand == []:
                print("Player 1, player 2, and the dealer guessed wrong.")
                if len(player3Hand) != 6:
                    print("Player 3 wins!")

            elif player1Hand != [] and player2Hand == [] and player3Hand == [] and dealerHand != []:
                print("Player 2 and player 3 guessed wrong.")
                print("Player 1's correct guesses: ", len(player1Hand))
                print("The dealer's correct guesses: ", len(dealerHand))
                if len(player1Hand) > len(dealerHand):
                    if len(player1Hand) != 6:
                        print("Player 1 wins!")

                elif len(player1Hand) == len(dealerHand):
                    if len(player1Hand) != 6:
                        print("Player 1 ties.")

                else:
                    print("Player 1 loses.")

            elif player1Hand == [] and player2Hand != [] and player3Hand == [] and dealerHand != []:
                print("Player 1 and player 3 guessed wrong.")
                print("Player 2's correct guesses: ", len(player2Hand))
                print("The dealer's correct guesses: ", len(dealerHand))
                if len(player2Hand) > len(dealerHand):
                    if len(player2Hand) != 6:
                        print("Player 2 wins!")

                elif len(player2Hand) == len(dealerHand):
                    if len(player2Hand) != 6:
                        print("Player 2 ties.")

                else:
                    print("Player 2 loses.")

            elif player1Hand == [] and player2Hand == [] and player3Hand != [] and dealerHand != []:
                print("Player 1 and player 2 guessed wrong.")
                print("Player 3's correct guesses: ", len(player3Hand))
                print("The dealer's correct guesses: ", len(dealerHand))
                if len(player3Hand) > len(dealerHand):
                    if len(player3Hand) != 6:
                        print("Player 3 wins!")

                elif len(player3Hand) == len(dealerHand):
                    if len(player3Hand) != 6:
                        print("Player 3 ties.")

                else:
                    print("Player 3 loses.")

            else:
                print("\nPlayer 1's correct guesses: ", len(player1Hand))
                print("Player 2's correct guesses: ", len(player2Hand))
                print("Player 3's correct guesses: ", len(player3Hand))
                print("The dealer's correct guesses: ", len(dealerHand))
                if len(player1Hand) > len(dealerHand):
                    if len(player1Hand) != 6:
                        print("Player 1 wins!")

                elif len(player1Hand) == len(dealerHand):
                    if len(player1Hand) != 6:
                        print("Player 1 ties.")

                else:
                    print("Player 1 loses.")

                if len(player2Hand) > len(dealerHand):
                    if len(player2Hand) != 6:
                        print("Player 2 wins!")

                elif len(player2Hand == len(dealerHand)):
                    if len(player2Hand) != 6:
                        print("Player 2 ties.")

                else:
                    print("Player 2 loses.")

                if len(player3Hand) > len(dealerHand):
                    if len(player3Hand) != 6:
                        print("Player 3 wins!")

                elif len(player3Hand == len(dealerHand)):
                    if len(player3Hand) != 6:
                        print("Player 3 ties.")

                else:
                    print("Player 3 loses.")

    else:
        print("You must type a number from 1 to 3.")

def player1Turn():
    global player1Hand
    player1Hand.append(deck.pop(0))
    print("Player 1's turn")
    finished = False
    while finished == False:
        print("\nPlayer 1's hand: ", player1Hand)
        print("Last card: ", player1Hand[-1])
        choice = input("Do you want to stand guess higher, or guess lower? ")
        if choice == "stand" or choice == "s":
            finished = True

        elif choice == "higher" or choice == "h":
            player1Hand.append(deck.pop(0))
            oldCard = player1Hand[-2]
            newCard = player1Hand[-1]
            print("New card: ", newCard)
            oldValue = 0
            if oldCard[0] == "Jack":
                oldValue = 11

            elif oldCard[0] == "Queen":
                oldValue = 12

            elif oldCard[0] == "King":
                oldValue = 13

            elif oldCard[0] == "Ace":
                oldValue = 14

            else:
                oldValue = int(oldCard[0])

            if newCard[0] == "Jack":
                newValue = 11

            elif newCard[0] == "Queen":
                newValue = 12

            elif newCard[0] == "King":
                newValue = 13

            elif newCard[0] == "Ace":
                newValue = 14

            else:
                newValue = int(newCard[0])

            if newValue >= oldValue:
                print("Correct!")
                if len(player1Hand) == 6:
                    print("You ride the tide!")
                    finished = True

                else:
                    continue

            else:
                print("Wrong")
                player1Hand.clear()
                finished = True

        elif choice == "lower" or choice == "l":
            player1Hand.append(deck.pop(0))
            oldCard = player1Hand[-2]
            newCard = player1Hand[-1]
            print("New card: ", newCard)
            oldValue = 0
            if oldCard[0] == "Jack":
                oldValue = 11

            elif oldCard[0] == "Queen":
                oldValue = 12

            elif oldCard[0] == "King":
                oldValue = 13

            elif oldCard[0] == "Ace":
                oldValue = 14

            else:
                oldValue = int(oldCard[0])

            if newCard[0] == "Jack":
                newValue = 11

            elif newCard[0] == "Queen":
                newValue = 12

            elif newCard[0] == "King":
                newValue = 13

            elif newCard[0] == "Ace":
                newValue = 14

            else:
                newValue = int(newCard[0])

            if newValue <= oldValue:
                print("Correct!")
                if len(player1Hand) == 6:
                    print("You ride the tide!")
                    finished = True

                else:
                    continue

            else:
                print("Wrong")
                player1Hand.clear()
                finished = True


        else:
            print("You must type 'stand', 'higher', or 'lower'.")
            break

def player2Turn():
    global player2Hand
    player2Hand.append(deck.pop(0))
    print("_____________________________________________________________________")
    print("Player 2's turn")
    finished = False
    while finished == False:
        print("\nPlayer 2's hand: ", player2Hand)
        print("Last card: ", player2Hand[-1])
        choice = input("Do you want to stand guess higher, or guess lower? ")
        if choice == "stand" or choice == "s":
            finished = True

        elif choice == "higher" or choice == "h":
            player2Hand.append(deck.pop(0))
            oldCard = player2Hand[-2]
            newCard = player2Hand[-1]
            print("New card: ", newCard)
            oldValue = 0
            if oldCard[0] == "Jack":
                oldValue = 11

            elif oldCard[0] == "Queen":
                oldValue = 12

            elif oldCard[0] == "King":
                oldValue = 13

            elif oldCard[0] == "Ace":
                oldValue = 14

            else:
                oldValue = int(oldCard[0])

            if newCard[0] == "Jack":
                newValue = 11

            elif newCard[0] == "Queen":
                newValue = 12

            elif newCard[0] == "King":
                newValue = 13

            elif newCard[0] == "Ace":
                newValue = 14

            else:
                newValue = int(newCard[0])

            if newValue >= oldValue:
                print("Correct!")
                if len(player2Hand) == 6:
                    print("You ride the tide!")
                    finished = True

                else:
                    continue

            else:
                print("Wrong")
                player2Hand.clear()
                finished = True

        elif choice == "lower" or choice == "l":
            player2Hand.append(deck.pop(0))
            oldCard = player2Hand[-2]
            newCard = player2Hand[-1]
            print("New card: ", newCard)
            oldValue = 0
            if oldCard[0] == "Jack":
                oldValue = 11

            elif oldCard[0] == "Queen":
                oldValue = 12

            elif oldCard[0] == "King":
                oldValue = 13

            elif oldCard[0] == "Ace":
                oldValue = 14

            else:
                oldValue = int(oldCard[0])

            if newCard[0] == "Jack":
                newValue = 11

            elif newCard[0] == "Queen":
                newValue = 12

            elif newCard[0] == "King":
                newValue = 13

            elif newCard[0] == "Ace":
                newValue = 14

            else:
                newValue = int(newCard[0])

            if newValue <= oldValue:
                print("Correct!")
                if len(player2Hand) == 6:
                    print("You ride the tide!")
                    finished = True

                else:
                    continue

            else:
                print("Wrong")
                player2Hand.clear()
                finished = True


        else:
            print("You must type 'stand', 'higher', or 'lower'.")
            break

def player3Turn():
    global player3Hand
    player3Hand.append(deck.pop(0))
    print("_____________________________________________________________________")
    print("Player 3's turn")
    finished = False
    while finished == False:
        print("\nPlayer 3's hand: ", player3Hand)
        print("Last card: ", player3Hand[-1])
        choice = input("Do you want to stand guess higher, or guess lower? ")
        if choice == "stand" or choice == "s":
            finished = True

        elif choice == "higher" or choice == "h":
            player3Hand.append(deck.pop(0))
            oldCard = player3Hand[-2]
            newCard = player3Hand[-1]
            print("New card: ", newCard)
            oldValue = 0
            if oldCard[0] == "Jack":
                oldValue = 11

            elif oldCard[0] == "Queen":
                oldValue = 12

            elif oldCard[0] == "King":
                oldValue = 13

            elif oldCard[0] == "Ace":
                oldValue = 14

            else:
                oldValue = int(oldCard[0])

            if newCard[0] == "Jack":
                newValue = 11

            elif newCard[0] == "Queen":
                newValue = 12

            elif newCard[0] == "King":
                newValue = 13

            elif newCard[0] == "Ace":
                newValue = 14

            else:
                newValue = int(newCard[0])

            if newValue >= oldValue:
                print("Correct!")
                if len(player3Hand) == 6:
                    print("You ride the tide!")
                    finished = True

                else:
                    continue

            else:
                print("Wrong")
                player3Hand.clear()
                finished = True

        elif choice == "lower" or choice == "l":
            player3Hand.append(deck.pop(0))
            oldCard = player3Hand[-2]
            newCard = player3Hand[-1]
            print("New card: ", newCard)
            oldValue = 0
            if oldCard[0] == "Jack":
                oldValue = 11

            elif oldCard[0] == "Queen":
                oldValue = 12

            elif oldCard[0] == "King":
                oldValue = 13

            elif oldCard[0] == "Ace":
                oldValue = 14

            else:
                oldValue = int(oldCard[0])

            if newCard[0] == "Jack":
                newValue = 11

            elif newCard[0] == "Queen":
                newValue = 12

            elif newCard[0] == "King":
                newValue = 13

            elif newCard[0] == "Ace":
                newValue = 14

            else:
                newValue = int(newCard[0])

            if newValue <= oldValue:
                print("Correct!")
                if len(player3Hand) == 6:
                    print("You ride the tide!")
                    finished = True

                else:
                    continue

            else:
                print("Wrong")
                player3Hand.clear()
                finished = True


        else:
            print("You must type 'stand', 'higher', or 'lower'.")
            break

def dealerTurn():
    global dealerHand
    dealerHand.append(deck.pop(0))
    print("_____________________________________________________________________")
    print("\nThe dealer's turn")
    finished = False
    while finished == False:
        print("\nThe dealer's hand: ", dealerHand)
        print("Last card: ", dealerHand[-1])
        choice = input("Do you want to stand guess higher, or guess lower? ")
        if choice == "stand" or choice == "s":
            finished = True

        elif choice == "higher" or choice == "h":
            dealerHand.append(deck.pop(0))
            oldCard = dealerHand[-2]
            newCard = dealerHand[-1]
            print("New card: ", newCard)
            oldValue = 0
            if oldCard[0] == "Jack":
                oldValue = 11

            elif oldCard[0] == "Queen":
                oldValue = 12

            elif oldCard[0] == "King":
                oldValue = 13

            elif oldCard[0] == "Ace":
                oldValue = 14

            else:
                oldValue = int(oldCard[0])

            if newCard[0] == "Jack":
                newValue = 11

            elif newCard[0] == "Queen":
                newValue = 12

            elif newCard[0] == "King":
                newValue = 13

            elif newCard[0] == "Ace":
                newValue = 14

            else:
                newValue = int(newCard[0])

            if newValue >= oldValue:
                print("Correct!")
                if len(dealerHand) == 6:
                    finished = True

                else:
                    continue

            else:
                print("Wrong")
                dealerHand.clear()
                finished = True

        elif choice == "lower" or choice == "l":
            dealerHand.append(deck.pop(0))
            oldCard = dealerHand[-2]
            newCard = dealerHand[-1]
            print("New card: ", newCard)
            oldValue = 0
            if oldCard[0] == "Jack":
                oldValue = 11

            elif oldCard[0] == "Queen":
                oldValue = 12

            elif oldCard[0] == "King":
                oldValue = 13

            elif oldCard[0] == "Ace":
                oldValue = 14

            else:
                oldValue = int(oldCard[0])

            if newCard[0] == "Jack":
                newValue = 11

            elif newCard[0] == "Queen":
                newValue = 12

            elif newCard[0] == "King":
                newValue = 13

            elif newCard[0] == "Ace":
                newValue = 14

            else:
                newValue = int(newCard[0])

            if newValue <= oldValue:
                print("Correct!")
                if len(dealerHand) == 6:
                    finished = True

                else:
                    continue

            else:
                print("Wrong")
                dealerHand.clear()
                finished = True


        else:
            print("You must type 'stand', 'higher', or 'lower'.")
            break

playRideTheTide()