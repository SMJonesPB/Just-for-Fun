#Photonic Officer(PO) in Star Trek Online(STO)
#PO cooldown(cd) is 30s
#PO is active for 20s
#assume PO and another ability activate at the same time
# go to desmos.com and graph y, z, and w

level = int(input("What level is PO? "))
x = float(input("What's the original cd of another ability? "))
percents = [.02, .03, .04]
percent = percents[level - 1]
y = x / (percent * x + 1) #such that x <= 20, the cd if PO is active for the whole time
z = percent * x + 1 #the cd you lose every second
w = 20 * z #total amount of cd you lose while PO is active, the ability keeps cooling down and activating\
print("y = ", y)
print("z = ", z)
print("w = ", w)

if (x / y) == z: #always equal, the same line on a graph
    print("If the cooldown is ", x, "s, you lose ", z, "s/ real second while PO is active.")

if x <= 20.0:
    print("PO is active for the whole cooldown, so the new cooldown is ", y)
    print("While PO is active, you can use the ability ", w / y, "time(s).")

else:
    remainingCD = x
    count = 0
    newCD = .0
    while remainingCD > 0.0: 
        count += 1 #PO activates no matter what
        if remainingCD - w > 0.0: #if there's enough time to go through the full 20s
            remainingCD -= w
            newCD += 20

        else:
            newCD += remainingCD / (percent * remainingCD + 1)
            remainingCD -= remainingCD #finishes cooling down while PO is active

        if remainingCD - 30.0 > 0.0: #PO cools down
            remainingCD -= 30.0
            newCD += 30

        else:
            newCD += remainingCD
            remainingCD -= remainingCD #not enough time for PO to cool down

    print("PO activates ", count, "time(s).")
    print("The new cd is ", newCD, "s.")
    

