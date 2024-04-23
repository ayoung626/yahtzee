import random
from collections import Counter

def diceroll(rolllist = []):
    keeplist = rolllist.copy()
    dicenum = 5 - len(keeplist)
    for i in range(dicenum):
        roll=random.randint(1,6)
        keeplist.append(roll)
    #print(keeplist)
    return Counter(keeplist)

def scoredice(dicedict):
    #initialize a dictionary that stores possible scoring categories from the dice roll
    categorydict = {}
    dicesum = 0
    threeplus = False
    for k,v in dicedict.items():
        #If there are 5 of any number, a yahtzee is added as an option (worth 50 points)
        if v == 5:
            categorydict['Y'] = 50
        #If there are more than three, change the threeplus flag to True to check for four of a kind and full house as well as three of a kind
        if v >= 3:
            threeplus = True
        #sum all of the dice for four of a kind and three of a kind scoring
        dicesum += k
        
        
    if threeplus == True:
        for v in dicedict.values():
            #Check for four of a kind
            if v==4:
                categorydict['4ok'] = dicesum
            #Check for full house
            if v==2:
                categorydict['FH'] = 25
            categorydict['3ok'] = dicesum
    try:
        #Check for large straights
        if (dicedict[1] ==1 and dicedict[2] == 1 and dicedict[3] == 1 and dicedict[4] == 1 and dicedict[5] == 1) or (dicedict[2] == 1 and dicedict[3] == 1 and dicedict[4] == 1 and dicedict[5] == 1 and dicedict[6]==1):
            categorydict['LS'] = 40
    except:
        pass
    try:
        #Check for small straights
        if (dicedict[1] >=1 and dicedict[2] >= 1 and dicedict[3] >= 1 and dicedict[4] >= 1) or (dicedict[2] >= 1 and dicedict[3] >= 1 and dicedict[4] >= 1 and dicedict[5] >= 1) or (dicedict[3] >= 1 and dicedict[4] >= 1 and dicedict[5] >= 1 and dicedict[6] >=1):
            categorydict['SS'] = 30
    except:
        pass
    
    categorydict['C'] = dicesum
    
    #Upper Section Scoring
    for i in range(1,7):
        upperscore = dicedict[i]*i
        if upperscore == 0:
            continue
        else:
            categorydict[str(i)] = upperscore
    
    return(dicedict, categorydict)