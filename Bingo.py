import random

row = 5
column = 5
card = [[0 for i in range(column)] for j in range(row)]
markedCard = [[False for i in range(column)] for j in range(row)]
calledNumbers = []
cardNumbers = []
letters = ["B", "I", "N", "G", "O"]
bingo = False

#Ways to get bingos
row1 = [False, False, False, False, False]
row2 = [False, False, False, False, False]
row3 = [False, False, False, False, False]
row4 = [False, False, False, False, False]
row5 = [False, False, False, False, False]
column1 = [False, False, False, False, False]
column2 = [False, False, False, False, False]
column3 = [False, False, False, False, False]
column4 = [False, False, False, False, False]
column5 = [False, False, False, False, False]
topLeftBottomRight = [False, False, False, False, False]
bottomLeftTopRight = [False, False, False, False, False]

#Make the card
for c in range(column):
    if c == 0:
        for r in range(row):
            onCard = False
            while onCard == False:
                b = random.randint(1, 15)
                if b not in cardNumbers:
                    card[r][c] = b
                    cardNumbers.append(b)
                    onCard = True

                else:
                    continue

                
            
    elif c == 1:
        for r in range(row):
            onCard = False
            while onCard == False:
                i = random.randint(16, 30)
                if i not in cardNumbers:
                    card[r][c] = i
                    cardNumbers.append(i)
                    onCard = True

                else:
                    continue

    elif c == 2:
         for r in range(row):
            onCard = False
            while onCard == False:
                n = random.randint(31, 45)
                if n not in cardNumbers:
                    card[r][c] = n
                    cardNumbers.append(n)
                    onCard = True

                else:
                    continue

    elif c == 3:
        for r in range(row):
            onCard = False
            while onCard == False:
                g = random.randint(46, 60)
                if g not in cardNumbers:
                    card[r][c] = g
                    cardNumbers.append(g)
                    onCard = True

                else:
                    continue

    else:
        for r in range(row):
            onCard = False
            while onCard == False:
                o = random.randint(61, 75)
                if o not in cardNumbers:
                    card[r][c] = o
                    cardNumbers.append(o)
                    onCard = True

                else:
                    continue

print("   ".join(str(i) for i in letters))
print("\n".join(str(i) for i in card))
print("\n")

#Play the game
while bingo == False:
    calledNumber = random.randint(1, 75)
    if calledNumber >= 1 and calledNumber <= 15:
        if calledNumber not in calledNumbers:
            print("B ", calledNumber)
            calledNumbers.append(calledNumber)

        else:
            continue

    elif calledNumber >= 16 and calledNumber <= 30:
        if calledNumber not in calledNumbers:
            print("I ", calledNumber)
            calledNumbers.append(calledNumber)

        else:
            continue

    elif calledNumber >= 31 and calledNumber <= 45:
        if calledNumber not in calledNumbers:
            print("N ", calledNumber)
            calledNumbers.append(calledNumber)

        else:
            continue

    elif calledNumber >= 46 and calledNumber <= 60:
        if calledNumber not in calledNumbers:
            print("G ", calledNumber)
            calledNumbers.append(calledNumber)

        else:
            continue

    elif calledNumber >= 61 and calledNumber <= 75:
        if calledNumber not in calledNumbers:
            print("O ", calledNumber)
            calledNumbers.append(calledNumber)

        else:
            continue

    for c in range(column):
        for r in range(row):
            if card[r][c] == calledNumber:
                if c == 0:
                    if r == 0:
                        row1[0] = True
                        column1[0] = True
                        topLeftBottomRight[0] = True
                        markedCard[r][c] = True
                        print("Match!")
                        print("\n".join(str(i) for i in markedCard))

                    elif r == 1:
                        row2[0] = True
                        column1[1] = True
                        markedCard[r][c] = True
                        print("Match!")
                        print("\n".join(str(i) for i in markedCard))

                    elif r == 2:
                        row3[0] = True
                        column1[2] = True
                        markedCard[r][c] = True
                        print("Match!")
                        print("\n".join(str(i) for i in markedCard))

                    elif r == 3:
                        row4[0] = True
                        column1[3] = True
                        markedCard[r][c] = True
                        print("\n".join(str(i) for i in markedCard))

                    else:
                        row5[0] = True
                        column1[4] = True
                        bottomLeftTopRight[0] = True
                        markedCard[r][c] = True
                        print("Match!")
                        print("\n".join(str(i) for i in markedCard))

                elif c == 1:
                    if r == 0:
                        row1[1] = True
                        column2[0] = True
                        markedCard[r][c] = True
                        print("Match!")
                        print("\n".join(str(i) for i in markedCard))

                    elif r == 1:
                        row2[1] = True
                        column2[1] = True
                        topLeftBottomRight[1] = True
                        markedCard[r][c] = True
                        print("Match!")
                        print("\n".join(str(i) for i in markedCard))

                    elif r == 2:
                        row3[1] = True
                        column1[2] = True
                        markedCard[r][c] = True
                        print("Match!")
                        print("\n".join(str(i) for i in markedCard))

                    elif r == 3:
                        row4[1] = True
                        column1[3] = True
                        bottomLeftTopRight[1] = True
                        markedCard[r][c] = True
                        print("Match!")
                        print("\n".join(str(i) for i in markedCard))

                    else:
                        row5[1] = True
                        column1[4] = True
                        markedCard[r][c] = True
                        print("Match!")
                        print("\n".join(str(i) for i in markedCard))
                
                elif c == 2:
                    if r == 0:
                        row1[2] = True
                        column3[0] = True
                        markedCard[r][c] = True
                        print("Match!")
                        print("\n".join(str(i) for i in markedCard))

                    elif r == 1:
                        row2[2] = True
                        column3[1] = True
                        markedCard[r][c] = True
                        print("Match!")
                        print("\n".join(str(i) for i in markedCard))

                    elif r == 2:
                        row3[2] = True
                        column3[2] = True
                        topLeftBottomRight[2] = True
                        bottomLeftTopRight[2] = True
                        markedCard[r][c] = True
                        print("Match!")
                        print("\n".join(str(i) for i in markedCard))

                    elif r == 3:
                        row4[2] = True
                        column1[3] = True
                        markedCard[r][c] = True
                        print("Match!")
                        print("\n".join(str(i) for i in markedCard))

                    else:
                        row5[2] = True
                        column3[4] = True
                        markedCard[r][c] = True
                        print("Match!")
                        print("\n".join(str(i) for i in markedCard))

                elif c == 3:
                    if r == 0:
                        row1[3] = True
                        column4[0] = True
                        markedCard[r][c] = True
                        print("Match!")
                        print("\n".join(str(i) for i in markedCard))

                    elif r == 1:
                        row2[3] = True
                        column4[1] = True
                        bottomLeftTopRight[3] = True
                        markedCard[r][c] = True
                        print("Match!")
                        print("\n".join(str(i) for i in markedCard))

                    elif r == 2:
                        row3[3] = True
                        column4[2] = True
                        markedCard[r][c] = True
                        print("Match!")
                        print("\n".join(str(i) for i in markedCard))

                    elif r == 3:
                        row4[3] = True
                        column4[3] = True
                        topLeftBottomRight[3] = True
                        markedCard[r][c] = True
                        print("Match!")
                        print("\n".join(str(i) for i in markedCard))
    
                    else:
                        row5[3] = True
                        column4[4] = True
                        markedCard[r][c] = True
                        print("Match!")
                        print("\n".join(str(i) for i in markedCard))

                else:

                    if r == 0:
                        row1[4] = True
                        column5[0] = True
                        bottomLeftTopRight[4] = True
                        markedCard[r][c] = True
                        print("Match!")
                        print("\n".join(str(i) for i in markedCard))

                    elif r == 1:
                        row2[4] = True
                        column5[1] = True
                        markedCard[r][c] = True
                        print("Match!")
                        print("\n".join(str(i) for i in markedCard))

                    elif r == 2:
                        row3[4] = True
                        column5[2] = True
                        markedCard[r][c] = True
                        print("Match!")
                        print("\n".join(str(i) for i in markedCard))

                    elif r == 3:
                        row4[4] = True
                        column1[3] = True
                        markedCard[r][c] = True
                        print("Match!")
                        print("\n".join(str(i) for i in markedCard))

                    else:
                        row5[4] = True
                        column5[4] = True
                        topLeftBottomRight[4] = True
                        markedCard[r][c] = True
                        print("Match!")
                        print("\n".join(str(i) for i in markedCard))


            else:
                continue
  #End the game if you have a bingo              
    if row1 == [True, True, True, True, True]:
        print("Bingo! Row 1")
        bingo = True

    elif row2 == [True, True, True, True, True]:
        print("Bingo! Row 2")
        bingo = True

    elif row3 == [True, True, True, True, True]:
        print("Bingo! Row 3")
        bingo = True

    elif row4 == [True, True, True, True, True]:
        print("Bingo! Row 4")
        bingo = True

    elif row5 == [True, True, True, True, True]:
        print("Bingo! Row 5")
        bingo = True

    elif column1 == [True, True, True, True, True]:
        print("Bingo! Column 1")
        bingo = True

    elif column2 == [True, True, True, True, True]:
        print("Bingo! Column 2")
        bingo = True

    elif column3 == [True, True, True, True, True]:
        print("Bingo! Column 3")
        bingo = True

    elif column4 == [True, True, True, True, True]:
        print("Bingo! Column 4")
        bingo = True

    elif column5 == [True, True, True, True, True]:
        print("Bingo! Column 5")
        bingo = True

    elif topLeftBottomRight == [True, True, True, True, True]:
        print("Bingo! From the top left to the bottom right")
        bingo = True

    elif bottomLeftTopRight == [True, True, True, True, True]:
        print("Bingo! From the bottom left to the top right")
        bingo = True

    else:
        continue