#In mu version of Yahtzee, there is not a Yahtzee bonus and your turn ends if you write points on the card.

import random

finished = False
keptDice = [0, 0, 0, 0, 0]
games = ["Game 1"]
waysToScore = ["Count and add only Ones", "Count and add only Ones", "Count and add only Twos", "Count and add only Threes", "Count and add only Fours", 
"Count and add only Fives", "Count and add only Sixes", "Total", "63+ scores a 35 bonus", "Total of Upper Section", "3 of a kind    Total of all dice", 
"Four of a kind     Total of all dice", "Full House     25", "Small Straight  30", "Large Straight     40", "Yahtzee   50", "Chance    Total of all dice",
"Yahtzee Bonus  100", "Total of Lower Section", "Total of Upper Section", "Grand Total"]
rowPoints = [25, 30, 40, 50, 100]
row, column = (20, 1)
card = [[0 for i in range(column)] for j in range(row)]

while finished == False:
    for roll in range(1, 4):
        if roll == 1:
            print("Roll 1")
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            die3 = random.randint(1, 6)
            die4 = random.randint(1, 6)
            die5 = random.randint(1, 6)
            dice = [die1, die2, die3, die4, die5]
            print(" ".join(str(i) for i in dice))
            die1Keep = input("Do you want to keep die 1? ")
            die2Keep = input("Do you want to keep die 2? ")
            die3Keep = input("Do you want to keep die 3? ")
            die4Keep = input("Do you want to keep die 4? ")
            die5Keep = input("Do you want to keep die 5? ")
            if die1Keep == "yes" or die1Keep == "y":
                keptDice[0] = die1

            if die2Keep == "yes" or die2Keep == "y":
                keptDice[1] = die2

            if die3Keep == "yes" or die3Keep == "y":
                keptDice[2] = die3

            if die4Keep == "yes" or die4Keep == "y":
                keptDice[3] = die4

            if die5Keep == "yes" or die5Keep == "y":
                keptDice[4] = die5


            print("Kept Die or Dice:", " ".join(str(i) for i in keptDice))

            #Write the points on the card
            if 0 not in keptDice:
                print("\n")
                print("                                                         ", " ".join(str(games) for i in games))
                print("\n".join(str(i) for i in waysToScore))
                print("\n")
                print("Kept Dice:", " ".join(str(i) for i in keptDice))
                rowScore = int(input("What type of score do you want? Enter a number from 1 to 6 (Upper Section) or from 10 to 17 (Lower Section) "))
                columnScore = input("What game is this? ")#1

                #Ones
                if rowScore == 1:
                    for die in dice:
                        if die == 1:
                            card[int(rowScore)][int(columnScore - 1)] += die

                #Twos
                elif rowScore == 2:
                    for die in dice:
                        if die == 2:
                            card[int(rowScore)][int(columnScore - 1)] += die

                #Threes
                elif rowScore == 3:
                    for die in dice:
                        if die == 3:
                            card[int(rowScore)][int(columnScore - 1)] += die

                #Fours
                elif rowScore == 4:
                    for die in dice:
                        if die == 4:
                            card[int(rowScore)][int(columnScore - 1)] += die

                #Fives
                elif rowScore == 5:
                    for die in dice:
                        if die == 5:
                            card[int(rowScore)][int(columnScore - 1)] += die

                #Sixes
                elif rowScore == 6:
                    for die in dice:
                        if die == 6:
                            card[int(rowScore)][int(columnScore - 1)] += die

                #Three of A Kind
                elif rowScore == 10:
                    threeOfAKind = input("What number is a 3 of a kind? ")
                    three = 0
                    for die in range(0, len(keptDice)):
                          if keptDice[die] == int(threeOfAKind):
                            three += keptDice[die]

                    card[int(rowScore) - 1][int(columnScore) - 1] += three

                #Four of A Kind
                elif rowScore == 11:
                    fourOfAKind = input("What number is a 4 of a kind? ")
                    four = 0
                    for die in range(0, len(keptDice)):
                        if keptDice[die] == int(fourOfAKind):
                            four += keptDice[die]

                    card[int(rowScore) - 1][int(columnScore) - 1] += four

                #Full House
                elif rowScore == 12:
                    card[int(rowScore) - 1][int(columnScore) - 1] = rowPoints[0]

                #Small Straight
                elif rowScore == 13:
                    card[int(rowScore) - 1][int(columnScore) - 1] = rowPoints[1]

                #Large Straight
                elif rowScore == 14:
                    card[int(rowScore) - 1][int(columnScore) - 1] = rowPoints[2]

                #Yahtzee
                elif rowScore == 15:
                    card[int(rowScore) - 1][int(columnScore) - 1] = rowPoints[3]
                    print("Yahtzee!")

                #Chance
                elif rowScore == 17:
                    score = 0
                    for die in keptDice:
                        score += die

                    card[int(rowScore) - 1][int(columnScore) - 1] += score

                #Upper Section Subtotal
                card[6][int(columnScore) - 1] = card[0][int(columnScore) - 1] + card[1][int(columnScore) - 1] + card[2][int(columnScore) - 1]
                + card[3][int(columnScore) - 1] + card[4][int(columnScore) - 1] + card[5][int(columnScore) - 1]
                
                #35-Point Bonus
                if card[6][int(columnScore) - 1] >= 63:
                    card[7][int(columnScore) - 1] = 35

                #Upper Section Grand Total
                card[8][int(columnScore) - 1] = card[6][int(columnScore) - 1] + card[7][int(columnScore) - 1]

                card[17][int(columnScore) - 1] = card[8][int(columnScore) - 1]

                #Lower Section Total
                card[18][int(columnScore) - 1] = card[9][int(columnScore) - 1] + card[10][int(columnScore) - 1] + card[11][int(columnScore) - 1]
                + card[12][int(columnScore) - 1] + card[13][int(columnScore) - 1] + card[14][int(columnScore) - 1] + card[15][int(columnScore) - 1] 
                + card[16][int(columnScore) - 1]

                #Grand Total
                card[19][int(columnScore) - 1] = card[17][int(columnScore) - 1] + card[18][int(columnScore) - 1]

                print("\n".join(str(i) for i in card))
                finished = True

        
        elif roll == 2:
            print("\nRoll 2")
            
            #Roll the die or dice you don't keep
            for die in range(0, len(dice)):
                if dice[die] not in keptDice:
                    dice[die] = random.randint(1, 6)

            print(" ".join(str(i) for i in dice))
            print("Kept Die or Dice:", " ".join(str(i) for i in keptDice))

            for die in range(0, 5):
                if keptDice[die] != dice[die]:
                    print("Die ", die + 1)
                    dieKeep = input("Do you want to keep a new die? ")
                    if dieKeep == "yes" or dieKeep == "y":
                        keptDice[die] = dice[die]

            print("Kept Die or Dice:", " ".join(str(i) for i in keptDice))

            #Write the points on the card
            if 0 not in keptDice:
                print("\n")
                print("                                                         ", " ".join(str(games) for i in games))
                print("\n".join(str(i) for i in waysToScore))
                print("\n")
                print("Kept Dice:", " ".join(str(i) for i in keptDice))
                rowScore = int(input("What type of score do you want? Enter a number from 1 to 6 (Upper Section) or from 10 to 17 (Lower Section) "))
                columnScore = input("What game is this? ")#1
                print("Kept Dice:", " ".join(str(i) for i in keptDice))
                #Ones
                if rowScore == 1:
                    for die in dice:
                        if die == 1:
                            card[int(rowScore)][int(columnScore - 1)] += die

                #Twos
                elif rowScore == 2:
                    for die in dice:
                        if die == 2:
                            card[int(rowScore)][int(columnScore - 1)] += die

                #Threes
                elif rowScore == 3:
                    for die in dice:
                        if die == 3:
                            card[int(rowScore)][int(columnScore - 1)] += die

                #Fours
                elif rowScore == 4:
                    for die in dice:
                        if die == 4:
                            card[int(rowScore)][int(columnScore - 1)] += die

                #Fives
                elif rowScore == 5:
                    for die in dice:
                        if die == 5:
                            card[int(rowScore)][int(columnScore - 1)] += die

                #Sixes
                elif rowScore == 6:
                    for die in dice:
                        if die == 6:
                            card[int(rowScore)][int(columnScore - 1)] += die

                #Three of A Kind
                elif rowScore == 10:
                    threeOfAKind = input("What number is a 3 of a kind? ")
                    three = 0
                    for die in range(0, len(keptDice)):
                          if keptDice[die] == int(threeOfAKind):
                            three += keptDice[die]

                    card[int(rowScore) - 1][int(columnScore) - 1] += three

                #Four of A Kind
                elif rowScore == 11:
                    fourOfAKind = input("What number is a 4 of a kind? ")
                    four = 0
                    for die in range(0, len(keptDice)):
                        if keptDice[die] == int(fourOfAKind):
                            four += keptDice[die]

                    card[int(rowScore) - 1][int(columnScore) - 1] += four

                #Full House
                elif rowScore == 12:
                    card[int(rowScore) - 1][int(columnScore) - 1] = rowPoints[0]

                #Small Straight
                elif rowScore == 13:
                    card[int(rowScore) - 1][int(columnScore) - 1] = rowPoints[1]

                #Large Straight
                elif rowScore == 14:
                    card[int(rowScore) - 1][int(columnScore) - 1] = rowPoints[2]

                #Yahtzee
                elif rowScore == 15:
                    card[int(rowScore) - 1][int(columnScore) - 1] = rowPoints[3]
                    print("Yahtzee!")

                #Chance
                elif rowScore == 17:
                    score = 0
                    for die in keptDice:
                        score += die

                    card[int(rowScore) - 1][int(columnScore) - 1] += score

                #Upper Section Subtotal
                card[6][int(columnScore) - 1] = card[0][int(columnScore) - 1] + card[1][int(columnScore) - 1] + card[2][int(columnScore) - 1]
                + card[3][int(columnScore) - 1] + card[4][int(columnScore) - 1] + card[5][int(columnScore) - 1]
                
                #35-Point Bonus
                if card[6][int(columnScore) - 1] >= 63:
                    card[7][int(columnScore) - 1] = 35

                #Upper Section Grand Total
                card[8][int(columnScore) - 1] = card[6][int(columnScore) - 1] + card[7][int(columnScore) - 1]

                card[17][int(columnScore) - 1] = card[8][int(columnScore) - 1]

                #Lower Section Total
                card[18][int(columnScore) - 1] = card[9][int(columnScore) - 1] + card[10][int(columnScore) - 1] + card[11][int(columnScore) - 1]
                + card[12][int(columnScore) - 1] + card[13][int(columnScore) - 1] + card[14][int(columnScore) - 1] + card[15][int(columnScore) - 1] 
                + card[16][int(columnScore) - 1]

                #Grand Total
                card[19][int(columnScore) - 1] = card[17][int(columnScore) - 1] + card[18][int(columnScore) - 1]

                print("\n".join(str(i) for i in card))
                finished = True

        else:
            print("\nRoll 3")

           #Roll the die or dice you don't keep
            for die in range(0, len(dice)):
                if dice[die] not in keptDice:
                    dice[die] = random.randint(1, 6)

            print(" ".join(str(i) for i in dice))
            print("Kept Die or Dice:", " ".join(str(i) for i in keptDice))

            for die in range(0, 5):
                if keptDice[die] != dice[die]:
                    keptDice[die] = dice[die]

            print("Kept Die or Dice:", " ".join(str(i) for i in keptDice))

            #Write the points on the card
            if 0 not in keptDice:
                print("\n")
                print("                                                         ", " ".join(str(games) for i in games))
                print("\n".join(str(i) for i in waysToScore))
                print("\n")
                print("Kept Dice:", " ".join(str(i) for i in keptDice))
                rowScore = int(input("What type of score do you want? Enter a number from 1 to 6 (Upper Section) or from 10 to 17 (Lower Section) "))
                columnScore = input("What game is this? ")#1

                #Ones
                if rowScore == 1:
                    for die in dice:
                        if die == 1:
                            card[int(rowScore)][int(columnScore - 1)] += die

                #Twos
                elif rowScore == 2:
                    for die in dice:
                        if die == 2:
                            card[int(rowScore)][int(columnScore - 1)] += die

                #Threes
                elif rowScore == 3:
                    for die in dice:
                        if die == 3:
                            card[int(rowScore)][int(columnScore - 1)] += die

                #Fours
                elif rowScore == 4:
                    for die in dice:
                        if die == 4:
                            card[int(rowScore)][int(columnScore - 1)] += die

                #Fives
                elif rowScore == 5:
                    for die in dice:
                        if die == 5:
                            card[int(rowScore)][int(columnScore - 1)] += die

                #Sixes
                elif rowScore == 6:
                    for die in dice:
                        if die == 6:
                            card[int(rowScore)][int(columnScore - 1)] += die

                #Three of A Kind
                elif rowScore == 10:
                    threeOfAKind = input("What number is a 3 of a kind? ")
                    three = 0
                    for die in range(0, len(keptDice)):
                          if keptDice[die] == int(threeOfAKind):
                            three += keptDice[die]

                    card[int(rowScore) - 1][int(columnScore) - 1] += three

                #Four of A Kind
                elif rowScore == 11:
                    fourOfAKind = input("What number is a 4 of a kind? ")
                    four = 0
                    for die in range(0, len(keptDice)):
                        if keptDice[die] == int(fourOfAKind):
                            four += keptDice[die]

                    card[int(rowScore) - 1][int(columnScore) - 1] += four

                #Full House
                elif rowScore == 12:
                    card[int(rowScore) - 1][int(columnScore) - 1] = rowPoints[0]

                #Small Straight
                elif rowScore == 13:
                    card[int(rowScore) - 1][int(columnScore) - 1] = rowPoints[1]

                #Large Straight
                elif rowScore == 14:
                    card[int(rowScore) - 1][int(columnScore) - 1] = rowPoints[2]

                #Yahtzee
                elif rowScore == 15:
                    card[int(rowScore) - 1][int(columnScore) - 1] = rowPoints[3]
                    print("Yahtzee!")

                #Chance
                elif rowScore == 17:
                    score = 0
                    for die in keptDice:
                        score += die

                    card[int(rowScore) - 1][int(columnScore) - 1] += score

                #Upper Section Subtotal
                card[6][int(columnScore) - 1] = card[0][int(columnScore) - 1] + card[1][int(columnScore) - 1] + card[2][int(columnScore) - 1]
                + card[3][int(columnScore) - 1] + card[4][int(columnScore) - 1] + card[5][int(columnScore) - 1]
                
                #35-Point Bonus
                if card[6][int(columnScore) - 1] >= 63:
                    card[7][int(columnScore) - 1] = 35

                #Upper Section Grand Total
                card[8][int(columnScore) - 1] = card[6][int(columnScore) - 1] + card[7][int(columnScore) - 1]

                card[17][int(columnScore) - 1] = card[8][int(columnScore) - 1]

                #Lower Section Total
                card[18][int(columnScore) - 1] = card[9][int(columnScore) - 1] + card[10][int(columnScore) - 1] + card[11][int(columnScore) - 1]
                + card[12][int(columnScore) - 1] + card[13][int(columnScore) - 1] + card[14][int(columnScore) - 1] + card[15][int(columnScore) - 1] 
                + card[16][int(columnScore) - 1]

                #Grand Total
                card[19][int(columnScore) - 1] = card[17][int(columnScore) - 1] + card[18][int(columnScore) - 1]

                print("\n".join(str(i) for i in card))
                finished = True