import random

waysToScore = ["Count and add only Ones", "Count and add only Twos", "Count and add only Threes", "Count and add only Fours", 
"Count and add only Fives", "Count and add only Sixes", "Total", "63+ scores a 35 bonus", "Total of Upper Section", "3 of a kind    Total of all dice", 
"Four of a kind     Total of all dice", "Full House     25", "Small Straight  30", "Large Straight     40", "Yahtzee   50", "Chance    Total of all dice",
"Yahtzee Bonus  100", "Total of Lower Section", "Total of Upper Section", "Grand Total"]
rowPoints = [25, 30, 40, 50, 100] #Full House, Small Straight, Large Straight, Yahtzee, Yahtzee Bounus
card = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for round in range(1, 13):
    print("Round ", round)
    keptDice = [0, 0, 0, 0, 0]
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
                print("\n".join(str(i) for i in waysToScore))
                print("\n")
                print("Kept Dice:", " ".join(str(i) for i in keptDice))
                rowScore = int(input("What type of score do you want? Enter a number from 1 to 6 (Upper Section) or from 10 to 17 (Lower Section) "))

                #Ones
                if rowScore == 1:
                    print("You pick Ones.")
                    for die in keptDice:
                        if die == 1:
                            card[int(rowScore) - 1] += die

                #Twos
                elif rowScore == 2:
                    print("You pick Twos.")
                    for die in keptDice:
                        if die == 2:
                            card[int(rowScore) - 1] += die

                #Threes
                elif rowScore == 3:
                    print("You pick Threes.")
                    for die in keptDice:
                        if die == 3:
                            card[int(rowScore) - 1] += die

                #Fours
                elif rowScore == 4:
                    print("You pick Fours.")
                    for die in keptDice:
                        if die == 4:
                            card[int(rowScore) - 1] += die

                #Fives
                elif rowScore == 5:
                    print("You pick Fives")
                    for die in keptDice:
                        if die == 5:
                            card[int(rowScore) - 1] += die

                #Sixes
                elif rowScore == 6:
                    print("You pick Sixes.")
                    for die in keptDice:
                        if die == 6:
                            card[int(rowScore) - 1] += die

                #Three of a Kind
                elif rowScore == 10:
                    print("You pick Three of a Kind.")
                    threeOfAKind = input("What number is a 3 of a kind? ")
                    three = 0
                    for die in keptDice:
                          if die == int(threeOfAKind):
                            three += die

                    card[int(rowScore) - 1] += three

                #Four of a Kind
                elif rowScore == 11:
                    print("You pick Four of a Kind.")
                    fourOfAKind = input("What number is a 4 of a kind? ")
                    four = 0
                    for die in keptDice:
                        if die == int(fourOfAKind):
                            four += die

                    card[int(rowScore) - 1] += four

                #Full House
                elif rowScore == 12:
                    print("You pick Full House.")
                    card[int(rowScore) - 1] = rowPoints[0]

                #Small Straight
                elif rowScore == 13:
                    print("You pick Small Straight.")
                    card[int(rowScore) - 1] = rowPoints[1]

                #Large Straight
                elif rowScore == 14:
                    print("You pick Large Straight.")
                    card[int(rowScore) - 1] = rowPoints[2]

                #Yahtzee
                elif rowScore == 15:
                    print("Yahtzee!")
                    card[int(rowScore) - 1] = rowPoints[3]

                elif rowScore == 16:
                    if card[14] == 50:
                        print("Yahtzee Bounus!")
                        card[int(rowScore) - 1] = rowPoints[4]

                #Chance
                elif rowScore == 17:
                    print("You pick Chance.")
                    score = 0
                    for die in keptDice:
                        score += die

                    card[int(rowScore) - 1] += score

                else:
                    print("You must type a number from 1 to 6 or from 10 to 17.")
                    break

                #Upper Section Subtotal
                card[6] = card[0] + card[1] + card[2]+ card[3] + card[4] + card[5]
                
                #35-Point Bonus
                if card[6] >= 63:
                    card[7] = 35

                #Upper Section Total
                card[8] = card[6] + card[7]
                card[17] = card[8]

                #Lower Section Total
                card[18] = card[9] + card[10] + card[11]+ card[12] + card[13] + card[14] + card[15] + card[16]

                #Grand Total
                card[19] = card[17] + card[18]

                print("\n".join(str(i) for i in card))
                print("\n")

        
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
                print("\n".join(str(i) for i in waysToScore))
                print("\n")
                print("Kept Dice:", " ".join(str(i) for i in keptDice))
                rowScore = int(input("What type of score do you want? Enter a number from 1 to 6 (Upper Section) or from 10 to 17 (Lower Section). "))

                #Ones
                if rowScore == 1:
                    print("You pick Ones.")
                    for die in keptDice:
                        if die == 1:
                            card[int(rowScore) - 1] += die

                #Twos
                elif rowScore == 2:
                    print("You pick Twos.")
                    for die in keptDice:
                        if die == 2:
                            card[int(rowScore) - 1] += die

                #Threes
                elif rowScore == 3:
                    print("You pick Threes.")
                    for die in keptDice:
                        if die == 3:
                            card[int(rowScore) - 1] += die

                #Fours
                elif rowScore == 4:
                    print("You pick Fours.")
                    for die in keptDice:
                        if die == 4:
                            card[int(rowScore) - 1] += die

                #Fives
                elif rowScore == 5:
                    print("You pick Fives")
                    for die in keptDice:
                        if die == 5:
                            card[int(rowScore) - 1] += die

                #Sixes
                elif rowScore == 6:
                    print("You pick Sixes.")
                    for die in keptDice:
                        if die == 6:
                            card[int(rowScore) - 1] += die

                #Three of a Kind
                elif rowScore == 10:
                    print("You pick Three of a Kind.")
                    threeOfAKind = input("What number is a 3 of a kind? ")
                    three = 0
                    for die in keptDice:
                          if die == int(threeOfAKind):
                            three += die

                    card[int(rowScore) - 1] += three

                #Four of a Kind
                elif rowScore == 11:
                    print("You pick Four of a Kind.")
                    fourOfAKind = input("What number is a 4 of a kind? ")
                    four = 0
                    for die in keptDice:
                        if die == int(fourOfAKind):
                            four += die

                    card[int(rowScore) - 1] += four

                #Full House
                elif rowScore == 12:
                    print("You pick Full House.")
                    card[int(rowScore) - 1] = rowPoints[0]

                #Small Straight
                elif rowScore == 13:
                    print("You pick Small Straight.")
                    card[int(rowScore) - 1] = rowPoints[1]

                #Large Straight
                elif rowScore == 14:
                    print("You pick Large Straight.")
                    card[int(rowScore) - 1] = rowPoints[2]

                #Yahtzee
                elif rowScore == 15:
                    print("Yahtzee!")
                    card[int(rowScore) - 1] = rowPoints[3]

                elif rowScore == 16:
                    if card[14] == 50:
                        print("Yahtzee Bounus!")
                        card[int(rowScore) - 1] = rowPoints[4]

                #Chance
                elif rowScore == 17:
                    print("You pick Chance.")
                    score = 0
                    for die in keptDice:
                        score += die

                    card[int(rowScore) - 1] += score

                else:
                    print("You must type a number from 1 to 6 or from 10 to 17.")
                    break

                #Upper Section Subtotal
                card[6] = card[0] + card[1] + card[2]+ card[3] + card[4] + card[5]
                
                #35-Point Bonus
                if card[6] >= 63:
                    card[7] = 35

                #Upper Section Total
                card[8] = card[6] + card[7]
                card[17] = card[8]

                #Lower Section Total
                card[18] = card[9] + card[10] + card[11]+ card[12] + card[13] + card[14] + card[15] + card[16]

                #Grand Total
                card[19] = card[17] + card[18]

                print("\n".join(str(i) for i in card))
                print("\n")

        else:
            print("\nRoll 3")

           #Roll the die or dice you don't keep
            for die in range(0, len(dice)):
                if dice[die] not in keptDice:
                    dice[die] = random.randint(1, 6)

            print(" ".join(str(i) for i in dice))
            for die in range(0, 5):
                if keptDice[die] != dice[die]:
                    keptDice[die] = dice[die]

            print("Kept Die or Dice:", " ".join(str(i) for i in keptDice))
            rowScore = int(input("What type of score do you want? Enter a number from 1 to 6 (Upper Section) or from 10 to 17 (Lower Section). "))

            #Write the points on the card
            if rowScore == 1:
                print("You pick Ones.")
                for die in keptDice:
                    if die == 1:
                        card[int(rowScore) - 1] += die

            #Twos
            elif rowScore == 2:
                print("You pick Twos.")
                for die in keptDice:
                    if die == 2:
                        card[int(rowScore) - 1] += die

            #Threes
            elif rowScore == 3:
                print("You pick Threes.")
                for die in keptDice:
                    if die == 3:
                        card[int(rowScore) - 1] += die

            #Fours
            elif rowScore == 4:
                print("You pick Fours.")
                for die in keptDice:
                    if die == 4:
                        card[int(rowScore) - 1] += die

            #Fives
            elif rowScore == 5:
                print("You pick Fives")
                for die in keptDice:
                    if die == 5:
                        card[int(rowScore) - 1] += die

            #Sixes
            elif rowScore == 6:
                print("You pick Sixes.")
                for die in keptDice:
                    if die == 6:
                        card[int(rowScore) - 1] += die

            #Three of a Kind
            elif rowScore == 10:
                print("You pick Three of a Kind.")
                threeOfAKind = input("What number is a 3 of a kind? ")
                three = 0
                for die in keptDice:
                      if die == int(threeOfAKind):
                        three += die

                card[int(rowScore) - 1] += three

            #Four of a Kind
            elif rowScore == 11:
                print("You pick Four of a Kind.")
                fourOfAKind = input("What number is a 4 of a kind? ")
                four = 0
                for die in keptDice:
                    if die == int(fourOfAKind):
                        four += die

                card[int(rowScore) - 1] += four

            #Full House
            elif rowScore == 12:
                print("You pick Full House.")
                card[int(rowScore) - 1] = rowPoints[0]

            #Small Straight
            elif rowScore == 13:
                print("You pick Small Straight.")
                card[int(rowScore) - 1] = rowPoints[1]

            #Large Straight
            elif rowScore == 14:
                print("You pick Large Straight.")
                card[int(rowScore) - 1] = rowPoints[2]

            #Yahtzee
            elif rowScore == 15:
                print("Yahtzee!")
                card[int(rowScore) - 1] = rowPoints[3]

            elif rowScore == 16:
                if card[14] == 50:
                    print("Yahtzee Bounus!")
                    card[int(rowScore) - 1] = rowPoints[4]

            #Chance
            elif rowScore == 17:
                print("You pick Chance.")
                score = 0
                for die in keptDice:
                    score += die

                card[int(rowScore) - 1] += score

            else:
                print("You must type a number from 1 to 6 or from 10 to 17.")
                break

            #Upper Section Subtotal
            card[6] = card[0] + card[1] + card[2]+ card[3] + card[4] + card[5]
                
            #35-Point Bonus
            if card[6] >= 63:
                card[7] = 35

            #Upper Section Total
            card[8] = card[6] + card[7]
            card[17] = card[8]

            #Lower Section Total
            card[18] = card[9] + card[10] + card[11]+ card[12] + card[13] + card[14] + card[15] + card[16]

            #Grand Total
            card[19] = card[17] + card[18]

            print("\n".join(str(i) for i in card))
            print("\n")