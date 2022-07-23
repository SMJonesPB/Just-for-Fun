import random

"""
Ride the Tide ia a card game in Casino Island to Go where you guess whether the next card is higher or lower to get 6 correct gueeses in a row. Aces are high.
In Casino Island to Go, you lose if the next card has the same value, but you don't in my version.
You can stand at anytime, and if you get more correct guesses in a row than the delaer, you win.
"""

#Make and shuffle the deck
row = 52
column = 2
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
        generalPlayer(player1Hand, 1)
        dealerTurn()
        player1Guesses = len(player1Hand)
        dealerGuesses = len(dealerHand)
        print("\n")
        if player1Guesses == 0 and dealerGuesses == 0:
            print("\nPlayer 1 and the dealer guessed wrong.")
        
        else:
            if player1Guesses == 6:
                print("Player 1 rides the tide!")
            
            elif player1Guesses == 0:
                print("\nPlayer 1 guessed wrong.")
                print("The dealer wins.")

            elif dealerGuesses == 0:
                print("The dealer guessed wrong.")
                print("Player 1 wins!")

            else:
                print("\nPlayer 1's correct guesses: ", player1Guesses)
                print("The dealer's correct guesses: ", dealerGuesses)
                if player1Guesses > dealerGuesses:
                    print("Player 1 wins!")

                elif player1Guesses == dealerGuesses:
                    print("Player 1 ties.")

                else:
                    print("Player 1 loses.")

    elif numberOfPlayers == "2":
        generalPlayer(player1Hand, 1)
        generalPlayer(player2Hand, 2)
        dealerTurn()
        player1Guesses = len(player1Hand)
        player2Guesses = len(player2Hand)
        dealerGuesses = len(dealerHand)
        print("\n")
        if player1Guesses == 0 and player2Guesses == 0 and dealerGuesses == 0:
            print("Player 1, player 2, and the dealer guessed wrong.")
        
        else:
            if player1Guesses == 6:
                if player2Guesses == 6:
                    print("Players 1 and 2 ride the tide!")

                else:
                    print("Player 1 rides the tide!")

            elif player2Guesses == 6:
                print("Player 2 rides the tide!")

            if player1Guesses == 0:
                if player2Guesses == 0:
                    print("Players 1 and 2 guessed wrong.")

                else:
                    if dealerGuesses == 0:
                        print("Player 1 and the dealer guessed wrong.")

            elif player2Guesses == 0:
                if dealerGuesses == 0:
                    print("Player 2 and the dealer guessed wrong")

                else:
                    print("Player 2 guessed wrong.")

            elif dealerGuesses == 0:
                print("The dealer guessed wrong.")

            print("Player 1's correct guesses: ", player1Guesses)
            print("Player 2's correct guesses: ", player2Guesses)
            print("The dealer's correct guesses: ", dealerGuesses)
            if player1Guesses > dealerGuesses and player1Guesses < 6:
                print("Player 1 wins!")

            elif player1Guesses == dealerGuesses and player1Guesses < 6:
                print("Player 1 ties.")

            else:
                if player1Guesses > 0:
                    print("Player 1 loses.")

            if player2Guesses > dealerGuesses and player2Guesses < 6:
                print("Player 2 wins!")

            elif player2Guesses == dealerGuesses and player2Guesses < 6:
                print("Player 2 ties.")

            else:
                if player2Guesses > 0:
                    print("Player 2 loses.")

    elif numberOfPlayers == "3":
        generalPlayer(player1Hand, 1)
        generalPlayer(player2Hand, 2)
        generalPlayer(player3Hand, 3)
        dealerTurn()
        player1Guesses = len(player1Hand)
        player2Guesses = len(player2Hand)
        player3Guesses = len(player3Hand)
        dealerGuesses = len(dealerHand)
        print("\n")
        if player1Guesses == 0 and player2Guesses == 0 and player3Guesses == 0 and dealerGuesses == 0:
            print("Player 1, player 2, player 3, and the dealer guessed wrong.")
        
        else:
            if player1Guesses == 6:
                if player2Guesses == 6:
                    if player3Guesses == 6:
                        print("Players 1, 2, and 3 ride the tide!")

                    else:
                        print("Players 1 and 2 ride the tide!")

                elif player3Guesses == 6:
                    print("Players 1 and 3 ride the tide!")

                else:
                    print("Player 1 rides the tide!")

            elif player2Guesses == 6:
                if player3Guesses == 6:
                    print("Players 2 and 3 ride the tide!")

                else:
                    print("Player 2 rides the tide!")

            elif player3Guesses == 6:
                print("Player 3 rides the tide!")

            else:
                print("Neither player 1, player 2, nor player 3 rides the tide.")

            if player1Guesses == 0:
                if player2Guesses == 0:
                    if player3Guesses == 0:
                        print("Players 1, 2, and 3 guessed wrong")

                    else:
                        if dealerGuesses == 0:
                            print("Player 1, player 2, and the dealer guessed wrong.")

                        else:
                            print("Players 1 and 2 guessed wrong.")

                else:
                    if player3Guesses == 0:
                        if dealerGuesses == 0:
                            print("Player 1, player 3, and the dealer guessed wrong.")

                        else:
                            print("Players 1 and 3 guessed wrong.")

                    else:
                        print("Player 1 guessed wrong.")

            elif player2Guesses == 0:
                if player3Guesses == 0:
                    if dealerGuesses == 0:
                        print("Player 2, player 3, and the dealer guessed wrong.")

                    else:
                        print("Players 2 and 3 guessed wrong.")

                else:
                    if dealerGuesses == 0:
                        print("Player 2 and the dealer guessed wrong.")

                    else:
                        print("Player 2 guessed wrong.")

            elif player3Guesses == 0:
                if dealerGuesses == 0:
                    print("Player 3 and the dealer guessed wrong.")

                else:
                    print("Player 3 guessed wrong.")

            elif dealerGuesses == 0:
                print("The dealer guessed wrong.")
            
            print("Player 1's correct guesses: ", player1Guesses)
            print("Player 2's correct guesses: ", player2Guesses)
            print("Player 3's correct guesses: ", player3Guesses)
            print("The dealer's correct guesses: ", dealerGuesses)
            if player1Guesses > dealerGuesses:
                if player1Guesses < 6:
                    print("Player 1 wins!")

            elif player1Guesses == dealerGuesses:
                if player1Guesses < 6:
                    print("Player 1 ties.")

            else:
                print("Player 1 loses.")

            if player2Guesses > dealerGuesses:
                if player2Guesses < 6:
                    print("Player 2 wins!")

            elif player2Guesses == dealerGuesses:
                if player2Guesses < 6:
                    print("Player 2 ties.")

            else:
                print("Player 2 loses.")

            if player3Guesses > dealerGuesses:
                if player3Guesses < 6:
                    print("Player 3 wins!")

            elif player3Guesses == dealerGuesses:
                if player3Guesses < 6:
                    print("Player 3 ties.")

            else:
                print("Player 3 loses.")

    else:
        print("You must type a number from 1 to 3.")

def generalPlayer(playerHand, playerNumber):
    playerHand.append(deck.pop(-1))
    print("_____________________________________________________________________")
    print("Player ", playerNumber, "'s turn")
    turn = True
    while turn == True:
        print("\nPlayer ", playerNumber, "'s hand: ", playerHand)
        print("Last card: ", playerHand[-1])
        choice = input("Do you want to stand, guess higher, or guess lower? ")
        if choice == "stand" or choice == "s":
            turn = False

        elif choice == "higher" or choice == "h":
            playerHand.append(deck.pop(-1))
            oldCard = playerHand[-2]
            newCard = playerHand[-1]
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
                if len(playerHand) == 6:
                    print("You ride the tide!")
                    turn = False

                else:
                    continue

            else:
                print("Wrong")
                player1Hand.clear()
                turn = False

        elif choice == "lower" or choice == "l":
            playerHand.append(deck.pop(-1))
            oldCard = playerHand[-2]
            newCard = playerHand[-1]
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
                if len(playerHand) == 6:
                    print("You ride the tide!")
                    turn = False

                else:
                    continue

            else:
                print("Wrong")
                playerHand.clear()
                turn = False


        else:
            print("You must type 'stand', 's', 'higher', 'h', 'lower', or 'l'.")
            break



def dealerTurn():
    global dealerHand
    dealerHand.append(deck.pop(-1))
    print("_____________________________________________________________________")
    print("\nThe dealer's turn")
    turn = True
    while turn == True:
        print("\nThe dealer's hand: ", dealerHand)
        print("Last card: ", dealerHand[-1])
        choice = input("Do you want to stand, guess higher, or guess lower? ")
        if choice == "stand" or choice == "s":
            turn = False

        elif choice == "higher" or choice == "h":
            dealerHand.append(deck.pop())
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
                    turn = False

                else:
                    continue

            else:
                print("Wrong")
                dealerHand.clear()
                turn = False

        elif choice == "lower" or choice == "l":
            dealerHand.append(deck.pop(-1))
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
                    turn = False

                else:
                    continue

            else:
                print("Wrong")
                dealerHand.clear()
                turn = False


        else:
            print("You must type 'stand', 's', 'higher', 'h', 'lower', or 'l'.")
            break

playRideTheTide()