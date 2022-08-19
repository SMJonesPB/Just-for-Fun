"""In War, the deck is divided equally between or among the players. Every player shows the top card of his/her deck. The player with the higher or highest value takes all of the cards. 
Aces are high, and they beat Kings. Kings beat Queens. Queens beat Jacks. Jacks beat Tens. 
In a tie, every player with the higher or highest value places the top 3 cards of his/her deck face down, then shows the next one. This is called a "war." 
Again, the player with the higher or highest value wins.
If there's another tie, every player places the top 3 cards face down and shows the next one again. The game continues until every player except 1 has lost his/her deck.
If you run out of cards in a war and lose, you lose the game. If you win, you get all of the cards normally and stay in the game.
Also, if you get into a war with an empty deck, everyone else in the war plays his/her cards normally.
You play the card that just started the war if you have 1, 2, or 3 cards left in your deck.
"""

import random

#Make and shuffle the deck
deck = [["" for i in range(2)] for j in range(52)]
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
player1Deck = deck[0:26]
player2Deck = deck[26:52]
deck.clear()
player1Card = []
player2Card = []

def playWar():
    global player1Card
    global player2Card
    game = True
    while game == True:
        player1Card = player1Deck.pop(-1)
        player2Card = player2Deck.pop(-1)
        print("\nPlayer 1's card:", player1Card)
        print("Player 2's card:", player2Card)
        print("Player 1 has", len(player1Deck), "card(s) left.")
        print("Player 2 has", len(player2Deck), "card(s) left.")
        player1War = []
        player2War = []
            
        #War
        if player1Card[0][0] == player2Card[0][0]:
            player1War.append(player1Card)
            player2War.append(player2Card)
            war = True
            now = input("\nIt's a war! Tyoe 'now' when you're ready to continue. ")
            if now == "now":
                while war == True:
                    if len(player1Deck) == 0:
                        player2Deck.append(player1Card)
                        war = False

                    elif len(player1Deck) == 1:
                        player1Card = player1Deck.pop(-1)

                    elif len(player1Deck) == 2:
                        player1War.append(player1Deck.pop(-1))
                        player1Card = player1Deck.pop(-1)

                    elif len(player1Deck) == 3:
                        player1War.append(player1Deck.pop(-1))
                        player1War.append(player1Deck.pop(-1))
                        player1Card = player1Deck.pop(-1)

                    else:
                        player1War.append(player1Deck.pop(-1))
                        player1War.append(player1Deck.pop(-1))
                        player1War.append(player1Deck.pop(-1))
                        player1Card = player1Deck.pop(-1)

                    if len(player2Deck) == 0:
                        player1Deck.append(player1Card)
                        war = False

                    elif len(player2Deck) == 1:
                        player2Card = player2Deck.pop(-1)

                    elif len(player2Deck) == 2:
                        player2War.append(player2Deck.pop(-1))
                        player2Card = player2Deck.pop(-1)

                    elif len(player2Deck) == 3:
                        player2War.append(player2Deck.pop(-1))
                        player2War.append(player2Deck.pop(-1))
                        player2Card = player2Deck.pop(0)

                    else:
                        player2War.append(player2Deck.pop(-1))
                        player2War.append(player2Deck.pop(-1))
                        player2War.append(player2Deck.pop(-1))
                        player2Card = player2Deck.pop(-1)

                    print("\nPlayer 1's card:", player1Card)
                    print("Player 2's card:", player2Card)
                    print("Player 1 has", len(player1Deck), "card(s) left.")
                    print("Player 2 has", len(player2Deck), "card(s) left.")
                    
                    #Another war
                    if player1Card[0] == player2Card[0]:
                        player1War.append(player1Card)
                        player2War.append(player2Card)

                    #End the war
                    else:
                        war = False
                        player1War.append(player1Card)
                        player2War.append(player2Card)
                        player1Value = 0
                        player2Value = 0
                        if player1Card[0] == "Jack":
                            player1Value = 11

                        elif player1Card[0] == "Queen":
                            player1Value = 12

                        elif player1Card[0] == "King":
                            player1Value = 13

                        elif player1Card[0] == "Ace":
                            player1Value = 14

                        else:
                            player1Value = int(player1Card[0])

                        if player2Card[0] == "Jack":
                            player2Value = 11

                        elif player2Card[0] == "Queen":
                                player2Value = 12

                        elif player2Card[0] == "King":
                            player2Value = 13

                        elif player2Card[0] == "Ace":
                            player2Value = 14

                        else:
                            player2Value = int(player2Card[0])
                            
                        if player1Value > player2Value:
                            print("Player 1 wins the war!")
                            for card in range(0, len(player1War)):
                                player1Deck.append(player1War[card])
                                
                            for card in range(0, len(player2War)):
                                player1Deck.append(player2War[card])
                                
                            print("\nPlayer 1 has", len(player1Deck), "card(s) left.")
                            print("Player 2 has", len(player2Deck), "card(s) left.")

                        else:
                            print("Player 2 wins the war!")
                            for card in range(0, len(player2War)):
                                player2Deck.append(player2War[card])
                                
                            for card in range(0, len(player1War)):
                                player2Deck.append(player1War[card])

                            print("\nPlayer 1 has", len(player1Deck), "card(s) left.")    
                            print("Player 2 has", len(player2Deck), "card(s) left.")

            else:
                print("\nYou must type 'now' to continue the game.")
                break

        #No war
        else:
            if player1Card[0] == "Jack":
                player1Value = 11

            elif player1Card[0] == "Queen":
                player1Value = 12

            elif player1Card[0] == "King":
                player1Value = 13

            elif player1Card[0] == "Ace":
                player1Value = 14

            else:
                player1Value = int(player1Card[0])

            if player2Card[0] == "Jack":
                player2Value = 11

            elif player2Card[0] == "Queen":
                player2Value = 12

            elif player2Card[0] == "King":
                player2Value = 13

            elif player2Card[0] == "Ace":
                player2Value = 14

            else:
                player2Value = int(player2Card[0])

            if player1Value > player2Value:
                print("Player 1 wins this turn!")
                player1Deck.append(player1Card)
                player1Deck.append(player2Card)
                print("\nPlayer 1 has", len(player1Deck), "card(s) left.")    
                print("Player 2 has", len(player2Deck), "card(s) left.")

            else:
                print("Player 2 wins this turn!")
                player2Deck.append(player1Card)
                player2Deck.append(player2Card)
                print("\nPlayer 1 has", len(player1Deck), "card(s) left.")    
                print("Player 2 has", len(player2Deck), "card(s) left.")

        now = input("\nType 'now' when you're ready to continue. ")
        if now == "now":
            if player1Deck == [] and player2Deck == []:
                print("\nIt's a tie.")
                game = False

            elif player2Deck == []:
                print("\nPlayer 1 wins!")
                game = False

            elif player1Deck == []:
                print("\nPlayer 2 wins!")
                game = False

            else:
                continue
            
        else:
            print("\nYou must type 'now' to continue the game.")
            break

playWar()