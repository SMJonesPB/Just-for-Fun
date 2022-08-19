import random

"""
My version of Blackjack includes having up to four hands by splitting your original one and splitting the 2 new ones and 5-Card Charlies, 
which are in the game Casino Island to Go. A 5-Card Charlie is having 5 cards in your hand without busting, and you automatically win if you get one.
"""

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
player1Hand = []
player2Hand = []
player3Hand = []
dealerHand = []
player1Total = []
player2Total = []
player3Total = []
dealerTotal = 0
numberOfPlayers = input("How many players are there from 1 to 3 except the dealer? ")
if numberOfPlayers == "1":
    player1Hand.append(deck.pop(-1))
    dealerHand.append(deck.pop(-1))
    player1Hand.append(deck.pop(-1))
    dealerHand.append(deck.pop(-1))
    
elif numberOfPlayers == "2":
    player1Hand.append(deck.pop(-1))
    player2Hand.append(deck.pop(-1))
    dealerHand.append(deck.pop(-1))
    player1Hand.append(deck.pop(-1))
    player2Hand.append(deck.pop(-1))
    dealerHand.append(deck.pop(-1))

elif numberOfPlayers == "3":
    player1Hand.append(deck.pop(-1))
    player2Hand.append(deck.pop(-1))
    player3Hand.append(deck.pop(-1))
    dealerHand.append(deck.pop(-1))
    player1Hand.append(deck.pop(-1))
    player2Hand.append(deck.pop(-1))
    player3Hand.append(deck.pop(-1))
    dealerHand.append(deck.pop(-1))

else:
    print("You must enter a number from 1 to 3.")

def playBlackjack():
    if numberOfPlayers == "1":
        generalPlayer(player1Hand, 1, player1Total)
        dealerTurn()
        for total in player1Total:
            if total == 0:
                print("Player 1 surrenders.")
            
            elif total == "Blackjack":
                print("Player 1 has a Blackjack!")

            elif total == "5-Card Charlie":
                print("Player 1 has a 5-Card Charlie!")

            elif (total > dealerTotal and total <= 21) or (total <= 21 and dealerTotal > 21):
                print("Player 1 wins!")
 
            elif total < dealerTotal and dealerTotal <= 21:
                print("Player 1 loses.")

            elif total == dealerTotal and total <= 21:
                print("Player 1 pushes.")

            elif total > 21:
                print("Player 1 busts.")

    elif numberOfPlayers == "2":
        generalPlayer(player1Hand, 1, player1Total)
        generalPlayer(player2Hand, 2, player2Total)
        dealerTurn()
        for total in player1Total:
            if total == 0:
                print("Player 1 surrenders.")
            
            elif total == "Blackjack":
                print("Player 1 has a Blackjack!")

            elif total == "5-Card Charlie":
                print("Player 1 has a 5-Card Charlie!")

            elif (total > dealerTotal and total <= 21) or (total <= 21 and dealerTotal > 21):
                print("Player 1 wins!")

            elif total < dealerTotal and dealerTotal <= 21:
                print("Player 1 loses.")

            elif total == dealerTotal and total <= 21:
                print("Player 1 pushes.")
                          
            elif total > 21:
                print("Player 1 busts.")

        for total in player2Total:
            if total == 0:
                print("Player 2 surrenders.")
            
            elif total == "Blackjack":
                print("Player 2 has a blackjack!")

            elif total == "5-Card Charlie":
                print("Player 2 has a 5-Card Charlie!")

            elif (total > dealerTotal and total <= 21) or (total <= 21 and dealerTotal > 21):
                print("Player 2 wins!")

            elif total < dealerTotal and dealerTotal <= 21:
                print("Player 2 loses.")

            elif total == dealerTotal and total <= 21:
                print("Player 2 pushes.")
                
            elif total > 21:
                print("Player 2 busts.")

    elif numberOfPlayers == "3":
        generalPlayer(player1Hand, 1, player1Total)
        generalPlayer(player2Hand, 2, player2Total)
        generalPlayer(player3Hand, 3, player3Total)
        dealerTurn()
        for total in player1Total:
            if total == 0:
                print("Player 1 surrenders.")
                
            elif total == "Blackjack":
                print("Player 1 has a Blackjack!")

            elif total == "5-Card Charlie":
                print("Player 1 has a 5-Card Charlie!")

            elif (total > dealerTotal and total <= 21) or (total <= 21 and dealerTotal > 21):
                print("Player 1 wins!")

            elif total < dealerTotal and dealerTotal <= 21:
                print("Player 1 loses.")

            elif total == dealerTotal and total <= 21:
                print("Player 1 pushes.")
                
            elif total >21:
                print("Player 1 busts.")

        for total in player2Total:
            if total == 0:
                print("Player 2 surrenders.")
            
            elif total == "Blackjack":
                print("Player 2 has a Blackjack!")

            elif total == "5-Card Charlie":
                print("Player 2 has a 5-Card Charlie!")
                
            elif (total > dealerTotal and total <= 21) or (total <= 21 and dealerTotal > 21):
                print("Player 2 wins!")

            elif total < dealerTotal and dealerTotal <= 21:
                print("Player 2 loses.")

            elif total == dealerTotal and total <= 21:
                print("Player 2 pushes.")
                
            elif total > 21:
                print("Player 2 busts.")

        for total in player3Total:
            if total == 0:
                print("Player 3 surrenders.")
            
            elif total == "Blackjack":
                print("Player 3 has a Blackjack!")

            elif total == "5-Card Charlie":
                print("Player 3 has a 5-Card Charlie!")
                
            elif (total > dealerTotal and total <= 21) or (total <= 21 and dealerTotal > 21):
                print("Player 3 wins!")

            elif total < dealerTotal and dealerTotal <= 21:
                print("Player 3 loses.")

            elif total == dealerTotal and total <= 21:
                print("Player 3 pushes.")

            elif total > 21:
                print("Player 3 busts.")

def generalPlayer(playerHand, playerNumber, playerTotal):
    total = 0
    softNumberCheck = False
    softNumberValue = 0
    for card in range(0, len(playerHand)):
        if playerHand[card][0] == "Jack" or playerHand[card][0] == "Queen" or playerHand[card][0] == "King":
            total += 10

        elif playerHand[card][0] == "Ace":
            softNumberCheck = True
            if total < 11:
                total += 11

            else:
                total += 1

        else:
            total += int(playerHand[card][0])

    turn = True
    while turn == True:
        softNumberValue = total - 10
        if softNumberCheck == True:
            print("Player " + str(playerNumber) + "'s hand")
            print("\n".join(str(i) for i in playerHand))
            print("\n")
            print("Total: ", softNumberValue, "/", total)
            print("\n")
            print("The dealer's hand")
            print(dealerHand[0])
            print("\n")

        else:
            print("Player " + str(playerNumber) + "'s hand")
            print("\n".join(str(i) for i in playerHand))
            print("\n")
            print("Total: ", total)
            print("\n")
            print("The dealer's hand")
            print(dealerHand[0])
            print("\n")
        
        if len(playerHand) == 2 and total == 21:
            playerTotal.append("Blackjack")
            turn = False
            break

        if len(playerHand) == 2:
            if playerHand[0][0] == playerHand[1][0]:
                choice = input("Do you want to hit, stand, surrender, or split? ")

            else:
                choice = input("Do you want to hit, stand, or surrender? ")

        else:
            choice = input("Do you want to hit or stand? " )
        
        if choice == "hit":
            playerHand.append(deck.pop(-1))
            last = playerHand[-1][0]
            if last == "Jack" or last == "Queen" or last == "King":
                total += 10

            elif last == "Ace":
                if total < 11:
                    softNumberCheck = True
                    total += 11
                    softNumberValue = total - 10

                else:
                    total += 1

            else:
                total += int(last)

            if total > 21:
                if softNumberCheck == True:
                    softNumberCheck = False
                    if last == "Jack" or last == "Queen" or last == "King":
                        total = softNumberValue + 10
                        continue

                    else:
                        total = softNumberValue + int(last)
                        continue

                else:
                    print("Player " + str(playerNumber) + "'s hand")
                    print("\n".join(str(i) for i in playerHand))
                    print("\n")
                    print("Total: ", total)
                    print("Bust")
                    playerTotal.append(total)
                    turn = False

            elif total <= 21 and len(playerHand) == 5:
                if softNumberCheck == True:
                    softNumberValue = total - 10
                    print("Player " + str(playerNumber) + "'s hand")
                    print("\n".join(str(i) for i in playerHand))
                    print("\n")
                    print("Total: ", softNumberValue, "/", total)
                    print("\n")
                    playerTotal.append("5-Card Charlie")
                    turn = False

                else:
                    print("Player " + str(playerNumber) + "'s hand")
                    print("\n".join(str(i) for i in playerHand))
                    print("\n")
                    print("Total: ", total)
                    print("\n")
                    playerTotal.append("5-Card Charlie")
                    turn = False

            elif total == 21:
                if softNumberCheck == True:
                    softNumberValue = total - 10
                    print("Player " + str(playerNumber) + "'s hand")
                    print("\n".join(str(i) for i in playerHand))
                    print("\n")
                    print("Total: ", softNumberValue, "/", total)
                    playerTotal.append(total)

                    turn = False
                
                else:
                    print("Player " + str(playerNumber) + "'s hand")
                    print("\n".join(str(i) for i in playerHand))
                    print("\n")
                    print("Total: ", total)
                    playerTotal.append(total)
                    turn = False
            
            else:
                continue

        elif choice == "stand":
            playerTotal.append(total)
            turn = False

        elif choice == "surrender":
            playerTotal.append(0)
            turn = False

        elif choice == "split":
            hand1 = [player1Hand[0]]
            hand2 = [player1Hand[1]]
            
            #The first half of the split
            hand1.append(deck.pop(-1))
            total1 = 0
            softNumberCheck = False
            softNumberValue = 0 
            for card in range(0, len(hand1)):
                if hand1[card][0] == "Jack" or hand1[card][0] == "Queen" or hand1[card][0] == "King":
                    total1 += 10

                elif hand1[card][0] == "Ace":
                    if total1 < 11:
                        softNumberCheck = True
                        total1 += 11

                    else:
                        total1 += 1

                else:
                    total1 += int(hand1[card][0])
            turnHand1 = True
            while turnHand1 == True:
                softNumberValue = total1 - 10
                if softNumberCheck == True:
                    print("Player " + str(playerNumber) + "'s hand 1")
                    print("\n".join(str(i) for i in hand1))
                    print("\n")
                    print("Total: ", softNumberValue, "/", total1)
                    print("\n")
                    print("The dealer's hand")
                    print(dealerHand[0])
                    print("\n")

                else:
                    print("Player " + str(playerNumber) + "'s hand 1")
                    print("\n".join(str(i) for i in hand1))
                    print("\n")
                    print("Total: ", total1)
                    print("\n")
                    print("The dealer's hand")
                    print(dealerHand[0])
                    print("\n")

                if len(hand1) == 2 and total1 == 21:
                    playerTotal.append(total1)
                    turnHand1 = False

                if len(hand1) == 2:
                    if hand1[0][0] == hand1[1][0]:
                        if hand1[0][0] != "Ace":
                            choice = input("Do you want to hit, stand, or split? ")
                        
                        else:
                            choice = input("Do you want to stand or split? ")


                    else:
                        if hand1[0][0] != "Ace":
                            choice = input("Do you want to hit or stand? ")

                        else:
                            playerTotal.append(total1)
                            turnHand1 = False

                else:
                    choice = input("Do you want to hit or stand? ")
                
                if choice == "hit":
                    hand1.append(deck.pop(-1))
                    last = hand1[-1][0]
                    if last == "Jack" or last == "Queen" or last == "King":
                        total1 += 10

                    elif last == "Ace":
                        if total1 < 11:
                            softNumberCheck = True
                            total1 += 11
                            softNumberValue = total1 - 10

                        else:
                            total1 += 1

                    else:
                        total1 += int(last)

                    if total1 > 21:
                        if softNumberCheck == True:
                            softNumberCheck = False
                            if last == "Jack" or last == "Queen" or last == "King":
                                total1 = softNumberValue + 10
                                continue

                            else:
                                total1 = softNumberValue + int(last)
                                continue

                        else:
                            print("Player " + str(playerNumber) + "'s hand 1")
                            print("\n".join(str(i) for i in hand1))
                            print("\n")
                            print("Total: ", total1)
                            print("Bust")
                            playerTotal.append(total1)
                            turnHand1 = False

                    elif total1 <= 21 and len(hand1) == 5:
                        if softNumberCheck == True:
                            softNumberValue = total1 - 10
                            print("Player " + str(playerNumber) + "'s hand 1")
                            print("\n".join(str(i) for i in hand1))
                            print("\n")
                            print("Total: ", softNumberValue, "/", total1)
                            print("\n")
                            playerTotal.append("5-Card Charlie")
                            turnHand1 = False
                        
                        else:
                            print("Player " + str(playerNumber) + "'s hand 1")
                            print("\n".join(str(i) for i in hand1))
                            print("\n")
                            print("Total: ", total1)
                            print("\n")
                            playerTotal.append("5-Card Charlie")
                            turnHand1 = False

                    elif total1 == 21:
                        if softNumberCheck == True:
                            softNumberValue = total1 - 10
                            print("Player " + str(playerNumber) + "'s hand 1")
                            print("\n".join(str(i) for i in hand1))
                            print("\n")
                            print("Total: ", softNumberValue, "/", total1)
                            playerTotal.append(total1)
                            turn = False
                            
                        else:
                            print("Player " + str(playerNumber) + "'s hand 1")
                            print("\n".join(str(i) for i in hand1))
                            print("\n")
                            print("Total: ", total1)
                            playerTotal.append(total1)
                            turn = False
                    
                    else:
                        continue


                elif choice == "stand":
                    playerTotal.append(total1)
                    turnHand1 = False

                elif choice == "split":
                    hand11 = [hand1[0]]
                    hand12 = [hand1[1]]

                    #The first half of the first half of the split
                    hand11.append(deck.pop(-1))
                    total11 = 0
                    for card in range(0, len(hand11)):
                        if hand11[card][0] == "Jack" or hand11[card][0] == "Queen" or hand11[card][0] == "King":
                            total11 += 10

                        elif hand11[card][0] == "Ace":
                            softNumberCheck = True
                            if total11 < 11:
                                total11 += 11

                            else:
                                total11 += 1

                        else:
                            total11 += int(hand11[card][0])

                    turnHand11 = True
                    while turnHand11 == True:
                        softNumberValue = total11 - 10
                        if softNumberCheck == True:
                            print("\n")
                            print("Player " + str(playerNumber) + "'s hand 1-1")
                            print("\n".join(str(i) for i in hand11))
                            print("\n")
                            print("Total: ", softNumberValue, "/", total11)
                            print("\n")
                            print("The dealer's hand")
                            print("\n")
                            print(dealerHand[0])
                            print("\n")

                        else:
                            print("\n")
                            print("Player " + str(playerNumber) + "'s hand 1-1")
                            print("\n".join(str(i) for i in hand11))
                            print("\n")
                            print("Total: ", total11)
                            print("\n")
                            print("The dealer's hand")
                            print("\n")
                            print(dealerHand[0])
                            print("\n")

                        if len(hand11) == 2 and total11 == 21:
                            playerTotal.append("Blackjack")
                            turnHand11 = False

                        if len(hand11) == 2:
                            if hand11[0][0] != "Ace":
                                choice = input("Do you want to hit or stand? ")
                                
                            else:
                                playerTotal.append(total11)
                                turnHand11 = False

                        else:
                            choice = input("Do you want to hit or stand? ")
                        
                        if choice == "hit":
                            hand11.append(deck.pop(-1))
                            last = hand11[-1][0]
                            if last == "Jack" or last == "Queen" or last == "King":
                                total11 += 10

                            elif last == "Ace":
                                if total11 < 11:
                                    total11 += 11

                                else:
                                    total11 += 1

                            else:
                                total11 += int(last)

                            if total11 > 21:
                                if softNumberCheck == True:
                                    softNumberCheck = False
                                    if last == "Jack" or last == "Queen" or last == "King":
                                        total11 = softNumberValue + 10
                                        continue
                                    
                                    else:
                                        total11 = softNumberValue + int(last)
                                        continue
                                    
                                else:
                                    print("Player " + str(playerNumber) + "'s hand 1-1")
                                    print("\n".join(str(i) for i in hand11))
                                    print("\n")
                                    print("Total: ", total11)
                                    print("Bust")
                                    if playerNumber == 1:
                                        player1Total.append(total11)
                                            
                                    elif playerNumber == 2:
                                        player2Total.append(total11)

                                    else:
                                        player3Total.append(total11)

                                    turnHand11 = False

                            elif total11 <= 21 and len(hand11) == 5:
                                if softNumberCheck == True:
                                    softNumberValue = total11 - 10
                                    print("Player " + str(playerNumber) + "'s hand 1-1")
                                    print("\n".join(str(i) for i in hand11))
                                    print("\n")
                                    print("Total: ", softNumberValue, "/", total11)
                                    print("\n")
                                    playerTotal.append("5-Card Charlie")
                                    turnHand11 = False

                                else:
                                    print("Player " + str(playerNumber) + "'s hand 1-1")
                                    print("\n".join(str(i) for i in hand11))
                                    print("\n")
                                    print("Total: ", total11)
                                    print("\n")
                                    playerTotal.append("5-Card Charlie")
                                    turnHand11 = False
                                    
                            elif total11 == 21:
                                if softNumberCheck == True:
                                    softNumberValue = total11 - 10
                                    print("Player " + str(playerNumber) + "'s hand 1-1")
                                    print("\n".join(str(i) for i in hand11))
                                    print("\n")
                                    print("Total: ", softNumberValue, "/", total11)
                                    playerTotal.append(total11)
                                    turn = False
                                
                                else:
                                    print("Player " + str(playerNumber) + "'s hand 1-1")
                                    print("\n".join(str(i) for i in hand1))
                                    print("\n")
                                    print("Total: ", total11)
                                    playerTotal.append(total11)
                                    turn = False
                            
                            else:
                                continue

                        else:
                            playerTotal.append(total11)
                            turnHand11 = False

                    #The second half of the first half of the split
                    hand12.append(deck.pop(-1))
                    total12 = 0
                    softNumberCheck = False
                    softNumberValue = 0
                    for card in range(0, len(hand12)):
                        if hand12[card][0] == "Jack" or hand12[card][0] == "Queen" or hand12[card][0] == "King":
                            total12 += 10

                        elif hand12[card][0] == "Ace":
                            softNumberCheck = True
                            if total12 < 11:
                                total12 += 11

                            else:
                                total12 += 1

                        else:
                            total12 += int(hand12[card][0])

                    turnHand12 = True
                    while turnHand12 == True:
                        softNumberValue = total12 - 10
                        if softNumberCheck == True:
                            print("\n")
                            print("Player " + str(playerNumber) + "'s hand 1-2")
                            print("\n".join(str(i) for i in hand12))
                            print("\n")
                            print("Total: ", softNumberValue, "/", total12)
                            print("\n")
                            print("The dealer's hand")
                            print("\n")
                            print(dealerHand[0])
                            print("\n")
                        
                        else:
                            print("\n")
                            print("Player " + str(playerNumber) + "'s hand 1-2")
                            print("\n".join(str(i) for i in hand12))
                            print("\n")
                            print("Total: ", total12)
                            print("\n")
                            print("The dealer's hand")
                            print("\n")
                            print(dealerHand[0])
                            print("\n")

                        if len(hand12) == 2 and total12 == 21:
                            playerTotal.append("Blackjack")

                        if len(hand1) == 2:
                            if hand12[0][0] != "Ace":
                                choice = input("Do you want to hit or stand? ")
                                
                            else:   
                                playerTotal.append(total12)
                                turnHand12 = False
                                turnHand1 = False

                        else:
                            choice = input("Do you want to hit or stand? ")

                        if choice == "hit":
                            hand12.append(deck.pop(-1))
                            last = hand12[-1][0]
                            if last == "Jack" or last == "Queen" or last == "King":
                                total12 += 10

                            elif last == "Ace":
                                if total12 < 11:
                                    total12 += 11

                                else:
                                    total12 += 1

                            else:
                                total12 += int(last)

                            if total12 > 21:
                                if softNumberCheck == True:
                                    softNumberCheck = False
                                    if last == "Jack" or last == "Queen" or last == "King":
                                        total12 = softNumberValue + 10
                                        continue

                                    else:
                                        total12 = softNumberValue + int(last)
                                        continue

                                else:
                                    print("Player " + str(playerNumber) + "'s hand 1-2")
                                    print("\n".join(str(i) for i in hand12))
                                    print("\n")
                                    print("Total: ", total12)
                                    print("Bust")
                                    playerTotal.append(total12)
                                    turnHand12 = False
                                    turnHand1 = False

                            elif total12 <= 21 and len(hand12) == 5:
                                if softNumberCheck == True:
                                    softNumberValue = total12 - 10
                                    print("Player " + str(playerNumber) + "'s hand 1-2")
                                    print("\n".join(str(i) for i in hand12))
                                    print("\n")
                                    print("Total: ", softNumberValue, "/", total12)
                                    print("\n")
                                    playerTotal.append("5-Card Charlie")
                                    turnHand12 = False
                                    turnHand1 = False

                                else:
                                    print("Player " + str(playerNumber) + "'s hand 1-2")
                                    print("\n".join(str(i) for i in hand12))
                                    print("\n")
                                    print("Total: ", total12)
                                    print("\n")
                                    playerTotal.append("5-Card Charlie")
                                    turnHand12 = False
                                    turnHand1 = False
                            
                            elif total12 == 21:
                                if softNumberCheck == True:
                                    softNumberValue = total12 - 10
                                    print("Player " + str(playerNumber) + "'s hand 1-2")
                                    print("\n".join(str(i) for i in hand12))
                                    print("\n")
                                    print("Total: ", softNumberValue, "/", total12)
                                    playerTotal.append(total12)
                                    turnHand12 = False
                                    turnHand1 = False
                                
                                else:
                                    print("Player " + str(playerNumber) + "'s hand 1-2")
                                    print("\n".join(str(i) for i in hand12))
                                    print("\n")
                                    print("Total: ", total12)
                                    playerTotal.append(total12)
                                    turnHand12 = False
                                    turnHand1 = False
                            
                            else:
                                continue
                            
                        else:
                            playerTotal.append(total12)
                            turnHand12 = False
                            turnHand1 = False

            #The second half of the split
            else:
                hand2.append(deck.pop(-1))
                total2 = 0
                softNumberCheck = False
                softNumberValue = 0
                for card in range(0, len(hand2)):
                    if hand2[card][0] == "Jack" or hand2[card][0] == "Queen" or hand2[card][0] == "King":
                        total2 += 10

                    elif hand2[card][0] == "Ace":
                        softNumberCheck = True
                        if total2 < 11:
                            total2 += 11

                        else:
                            total2 += 1

                    else:
                        total2 += int(hand2[card][0])

                turnHand2 = True
                while turnHand2 == True:
                    softNumberValue = total2 - 10
                    if softNumberCheck == True:
                        print("\n")
                        print("Player " + str(playerNumber) + "'s hand 2")
                        print("\n".join(str(i) for i in hand2))
                        print("\n")
                        print("Total: ", softNumberValue, "/", total2)
                        print("\n")
                        print("The dealer's hand")
                        print("\n")
                        print(dealerHand[0])
                        print("\n")
                    
                    else:
                        print("\n")
                        print("Player " + str(playerNumber) + "'s hand 2")
                        print("\n".join(str(i) for i in hand2))
                        print("\n")
                        print("Total: ", total2)
                        print("\n")
                        print("The dealer's hand")
                        print("\n")
                        print(dealerHand[0])
                        print("\n")

                    if len(hand2) == 2 and total2 == 21:
                        playerTotal.append("Blackjack")
                        turnHand2 = False
                        turn = False

                    if len(hand2) == 2:
                        if hand2[0][0] == hand2[1][0]:
                            if hand2[0][0] != "Ace":
                                choice = input("Do you want to hit, stand, or split? ")
                            
                            else:
                                choice = input("Do you want to stand or split? ")


                        else:
                            if hand2[0][0] != "Ace":
                                choice = input("Do you want to hit or stand? ")

                            else:
                                playerTotal.append(total2)
                                turnHand2 = False
                                turn = False

                    else:
                        choice = input("Do you want to hit or stand? ")

                    if choice == "hit":
                        hand2.append(deck.pop(-1))
                        last = hand2[-1][0]
                        if last == "Jack" or last == "Queen" or last == "King":
                            total2 += 10

                        elif last == "Ace":
                            if total2 < 11:
                                softNumberCheck = True
                                total2 += 11
                                softNumberValue = total2 - 10

                            else:
                                total2 += 1

                        else:
                            total2 += int(last)

                        if total2 > 21:
                            if softNumberCheck == True:
                                softNumberCheck = False
                                if last == "Jack" or last == "Queen" or last == "King":
                                    total2 = softNumberValue + 10
                                    continue

                                else:
                                    total2 = softNumberValue + int(last)
                                    continue

                            else:
                                print("Player " + str(playerNumber) + "'s hand 2")
                                print("\n".join(str(i) for i in hand2))
                                print("\n")
                                print("Total: ", total2)
                                print("Bust")
                                playerTotal.append(total2)
                                turnHand2 = False
                                turn = False

                        elif total2 <= 21 and len(hand2) == 5:
                            if softNumberCheck == True:
                                softNumberValue = total2 - 10
                                print("Player " + str(playerNumber) + "'s hand 2")
                                print("\n".join(str(i) for i in hand2))
                                print("\n")
                                print("Total: ", softNumberValue, "/", total2)
                                playerTotal.append("5-Card Charlie")

                                turnHand2 = False
                                turn = False
                            
                            else:
                                print("Player " + str(playerNumber) + "'s hand 2")
                                print("\n".join(str(i) for i in hand2))
                                print("\n")
                                print("Total: ", total2)
                                print("\n")
                                playerTotal.append("5-Card Charlie")
                                turnHand2 = False
                                turn = False

                        elif total2 == 21:
                            if softNumberCheck == True:
                                softNumberValue = total2 - 10
                                print("Player " + str(playerNumber) + "'s hand 2")
                                print("\n".join(str(i) for i in hand2))
                                print("\n")
                                print("Total: ", softNumberValue, "/", total2)
                                playerTotal.append(total2)
                                turnHand2 = False
                                turn = False
                                
                            else:
                                print("Player " + str(playerNumber) + "'s hand 2")
                                print("\n".join(str(i) for i in hand2))
                                print("\n")
                                print("Total: ", total2)
                                playerTotal.append(total2)
                                turnHand2 = False
                                turn = False
                        
                        else:
                            continue
                    
                    elif choice == "stand":
                        playerTotal.append(total2)
                        turnHand2 = False
                        turn = False
                    
                    elif choice == "split":
                        hand21 = [hand2[0]]
                        hand22 = [hand2[1]]

                        #The first half of the second half of the split
                        hand21.append(deck.pop(-1))
                        total21 = 0
                        softNumberCheck = False
                        softNumberValue = 0
                        for card in range(0, len(hand21)):
                            if hand21[card][0] == "Jack" or hand21[card][0] == "Queen" or hand21[card][0] == "King":
                                total21 += 10

                            elif hand21[card][0] == "Ace":
                                softNumberCheck = True
                                if total21 < 11:
                                    total21 += 11

                                else:
                                    total21 += 1

                            else:
                                total21 += int(hand21[card][0])

                        turnHand21 = True
                        while turnHand21 == True:
                            softNumberValue = total21 - 10
                            if softNumberCheck == True:
                                print("\n")
                                print("Player " + str(playerNumber) + "'s hand 2-1")
                                print("\n".join(str(i) for i in hand21))
                                print("\n")
                                print("Total: ", softNumberValue, "/", total21)
                                print("\n")
                                print("The dealer's hand")
                                print("\n")
                                print(dealerHand[0])
                                print("\n")

                            else:
                                print("\n")
                                print("Player " + str(playerNumber) + "'s hand 2-1")
                                print("\n".join(str(i) for i in hand21))
                                print("\n")
                                print("Total: ", total21)
                                print("\n")
                                print("The dealer's hand")
                                print("\n")
                                print(dealerHand[0])
                                print("\n")

                            if len(hand21) == 2 and total21 == 21:
                                playerTotal.append("Blackjack")
                                turnHand21 = False

                            if len(hand21) == 2:
                                if hand21[0][0] != "Ace":
                                    choice = input("Do you want to hit or stand? ")
                                    
                                else:
                                    playerTotal.append("Blackjack")
                                    turnHand21 = False

                            else:
                                choice = input("Do you want to hit or stand? ")

                            if choice == "hit":
                                hand21.append(deck.pop(-1))
                                last = hand21[-1][0]
                                if last == "Jack" or last == "Queen" or last == "King":
                                    total21 += 10

                                elif last == "Ace":
                                    if total21 < 11:
                                        softNumberCheck = True
                                        total21 += 11
                                        softNumberValue = total21 - 10

                                    else: total21 += 1

                                else:
                                    total21 += int(last)

                                if total21 > 21:
                                    if softNumberCheck == True:
                                        softNumberCheck = False
                                        if last == "Jack" or last == "Queen" or last == "King":
                                            total21 = softNumberValue + 10
                                            continue
                                        
                                        else:
                                            total21 = softNumberValue + int(last)
                                            continue
                                    
                                    else:
                                        print("Player " + str(playerNumber) + "'s hand 2-1")
                                        print("\n".join(str(i) for i in hand21))
                                        print("\n")
                                        print("Total: ", total21)
                                        print("Bust")
                                        playerTotal.append(total21)
                                        turnHand21 = False

                                elif total21 <= 21 and len(hand21) == 5:
                                    if softNumberCheck == True:
                                        softNumberValue = total21 - 10
                                        print("Player " + str(playerNumber) + "'s hand 2-1")
                                        print("\n".join(str(i) for i in hand21))
                                        print("\n")
                                        print("Total: ", softNumberValue, "/", total21)
                                        print("\n")
                                        playerTotal.append("5-Card Charlie")
                                        turnHand21 = False

                                    else:
                                        print("Player " + str(playerNumber) + "'s hand 2-1")
                                        print("\n".join(str(i) for i in hand21))
                                        print("\n")
                                        print("Total: ", total21)
                                        print("\n")
                                        playerTotal.append("5-Card Charlie")
                                        turnHand21 = False
                                
                                elif total21 == 21:
                                    if softNumberCheck == True:
                                        softNumberValue = total21 - 10
                                        print("Player " + str(playerNumber) + "'s hand 2-1")
                                        print("\n".join(str(i) for i in hand21))
                                        print("\n")
                                        print("Total: ", softNumberValue, "/", total21)
                                        playerTotal.append(total21)
                                        turnHand21 = False
                                        
                                    else:
                                        print("Player " + str(playerNumber) + "'s hand 2-1")
                                        print("\n".join(str(i) for i in hand21))
                                        print("\n")
                                        print("Total: ", total21)
                                        playerTotal.append(total21)
                                        turnHand21 = False
                                
                                else:
                                    continue

                            else:
                                playerTotal.append(total21)
                                turnHand21 = False

                        #The second half of the second half of the split
                        else:
                            hand22.append(deck.pop(-1))
                            total22 = 0
                            softNumberCheck = False
                            softNumberValue = 0
                            for card in range(0, len(hand22)):
                                if hand22[card][0] == "Jack" or hand22[card][0] == "Queen" or hand22[card][0] == "King":
                                    total22 += 10

                                elif hand22[card][0] == "Ace":
                                    softNumberCheck = True
                                    if total22 < 11:
                                        total22 += 11

                                    else:
                                        total22 += 1

                                else:
                                    total22 += int(hand22[card][0])

                            turnHand22 = True
                            while turnHand22 == True:
                                softNumberValue = total22 - 10
                                if softNumberCheck == True:
                                    print("\n")
                                    print("Player " + str(playerNumber) + "'s hand 2-2")
                                    print("\n".join(str(i) for i in hand22))
                                    print("\n")
                                    print("Total: ", softNumberValue, "/", total22)
                                    print("\n")
                                    print("The dealer's hand")
                                    print("\n")
                                    print(dealerHand[0])
                                    print("\n")

                                else:
                                    print("\n")
                                    print("Player " + str(playerNumber) + "'s hand 2-2")
                                    print("\n".join(str(i) for i in hand22))
                                    print("\n")
                                    print("Total: ", total22)
                                    print("\n")
                                    print("The dealer's hand")
                                    print("\n")
                                    print(dealerHand[0])
                                    print("\n")

                                if len(hand22) == 2 and total22 == 21:
                                    playerTotal.append("Blackjack")
                                    turnHand22 = False
                                    turnHand2 = False
                                    turn = False

                                if len(hand22) == 2:
                                    if hand1[0][0] != "Ace":
                                        choice = input("Do you want to hit or stand? ")
                                        
                                    else:
                                        playerTotal.append(total22)
                                        turnHand22 = False
                                        turnHand2 = False
                                        turn = False

                                else:
                                    choice = input("Do you want to hit or stand? ")

                                if choice == "hit":
                                    hand22.append(deck.pop(-1))
                                    last = hand22[-1][0]
                                    if last == "Jack" or last == "Queen" or last == "King":
                                        total22 += 10

                                    elif last == "Ace":
                                        if total22 < 11:
                                            softNumberCheck = True
                                            total22 += 11
                                            softNumberValue = total22 - 10

                                        else:
                                            total22 += 1

                                    else:
                                        total22 += int(last)

                                    if total22 > 21:
                                        if softNumberCheck == True:
                                            softNumberCheck = False
                                            if last == "Jack" or last == "Queen" or last == "King":
                                                total22 = softNumberValue + 10
                                                continue

                                            else:
                                                total22 = softNumberValue + int(last)
                                                continue
                                        
                                        else:
                                            print("Player " + str(playerNumber) + "'s hand 2-2")
                                            print("\n".join(str(i) for i in hand22))
                                            print("\n")
                                            print("Total: ", total22)
                                            print("Bust")
                                            playerTotal.append(total22)
                                            turnHand22 = False
                                            turnHand2 = False
                                            turn = False

                                    elif total22 <= 21 and len(hand22) == 5:
                                        if softNumberCheck == True:
                                            softNumberValue = total22 - 10
                                            print("Player " + str(playerNumber) + "'s hand 2-2")
                                            print("\n".join(str(i) for i in hand22))
                                            print("\n")
                                            print("Total: ", softNumberValue, "/", total22)
                                            print("\n")
                                            playerTotal.append("5-Card Charlie")
                                            turnHand22 = False
                                            turnHand2 = False
                                            turn = False

                                        else:
                                            print("Player " + str(playerNumber) + "'s hand 2-2")
                                            print("\n".join(str(i) for i in hand22))
                                            print("\n")
                                            print("Total: ", total22)
                                            print("\n")
                                            playerTotal.append("5-Card Charlie")
                                            turnHand22 = False
                                            turnHand2 = False
                                            turn = False
                                    
                                    elif total22 == 21:
                                        if softNumberCheck == True:
                                            softNumberValue = total22 - 10
                                            print("Player " + str(playerNumber) + "'s hand 2-2")
                                            print("\n".join(str(i) for i in hand22))
                                            print("\n")
                                            print("Total: ", softNumberValue, "/", total22)
                                            playerTotal.append(total22)
                                            turnHand22 = False
                                            turnHand2 = False
                                            turn = False
                                            
                                        else:
                                            print("Player " + str(playerNumber) + "'s hand 2-2")
                                            print("\n".join(str(i) for i in hand22))
                                            print("\n")
                                            print("Total: ", total22)
                                            playerTotal.append(total22)
                                            turnHand22 = False
                                            turnHand2 = False
                                            turn = False
                                    
                                    else:
                                        continue

                                else:
                                    playerTotal.append(total22)
                                    turnHand22 = False
                                    turnHand2 = False
                                    turn = False

def dealerTurn():
    global dealerTotal
    softNumberCheck = False
    softNumberValue = 0
    for card in range(0, len(dealerHand)):
        if dealerHand[card][0] == "Jack" or dealerHand[card][0] == "Queen" or dealerHand[card][0] == "King":
            dealerTotal += 10

        elif dealerHand[card][0] == "Ace":
            softNumberCheck = True
            if dealerTotal < 11:
                dealerTotal += 11

            else:
                dealerTotal += 1

        else:
            dealerTotal += int(dealerHand[card][0])

    turn = True
    while turn == True:
        softNumberValue = dealerTotal - 10
        if softNumberCheck == True:
            print("\n")
            print("The dealer's hand")
            print("\n".join(str(i) for i in dealerHand))
            print("\n")
            print("Total: ", softNumberValue, "/", dealerTotal)
            print("\n")

        else:    
            print("\n")
            print("The dealer's hand")
            print("\n".join(str(i) for i in dealerHand))
            print("\n")
            print("Total: ", dealerTotal)
            print("\n")

        if len(dealerHand) == 2 and dealerTotal == 21:
            print("Blackjack")
            turn = False
            break

        choice = input("Do you want to hit or stand? ")
        if choice == "hit":
            dealerHand.append(deck.pop(-1))
            last = dealerHand[-1][0]
            if last == "Jack" or last == "Queen" or last == "King":
                dealerTotal += 10

            elif last == "Ace":
                if dealerTotal < 11:
                    softNumberCheck = True
                    dealerTotal += 11
                    softNumberValue = dealerTotal - 10

                else:
                    dealerTotal += 1

            else:
                dealerTotal += int(last)

            if dealerTotal > 21:
                if softNumberCheck == True:
                    softNumberCheck = False
                    if last == "Jack" or last == "Queen" or last == "King":
                        dealerTotal = softNumberValue + 10
                        continue

                    else:
                        dealerTotal = softNumberValue + int(last)
                        continue

                else:
                    print("\n")
                    print("The dealer's hand")
                    print("\n".join(str(i) for i in dealerHand))
                    print("\n")
                    print("Total: ", dealerTotal)
                    print("Bust")
                    turn = False

            elif dealerTotal == 21:
                if softNumberCheck == True:
                    softNumberValue = dealerTotal - 10
                    print("\n")
                    print("The dealer's hand")
                    print("\n".join(str(i) for i in dealerHand))
                    print("\n")
                    print("Total: ", softNumberValue, "/", dealerTotal)
                    turn = False

                else:
                    print("\n")
                    print("The dealer's hand")
                    print("\n".join(str(i) for i in dealerHand))
                    print("\n")
                    print("Total: ", dealerTotal)
                    turn = False
            
            else:
                continue

        elif choice == "stand":
            turn = False    

        else:
            print("You must tyoe 'hit' or 'stand'.")
            continue

playBlackjack()