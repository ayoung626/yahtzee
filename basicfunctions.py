import random
from collections import Counter

def diceroll(rolllist=None):
    if rolllist is None:
        rolllist = []
    keeplist = rolllist.copy()
    dicenum = 5 - len(keeplist)
    for i in range(dicenum):
        roll=random.randint(1,6)
        keeplist.append(roll)
    #print(keeplist)
    return Counter(keeplist)

def scoredice(dicedict):
    categorydict = {}
    dicesum = sum(k * v for k, v in dicedict.items())
    counts = list(dicedict.values())
    max_count = max(counts) if counts else 0
    
    # Yahtzee (5 of a kind)
    if max_count >= 5:
        categorydict['Y'] = 50
    # Four of a kind
    if max_count >= 4:
        categorydict['4ok'] = dicesum
    # Three of a kind
    if max_count >= 3:
        categorydict['3ok'] = dicesum
    # Full House (3 of one number and 2 of another)
    if 3 in counts and 2 in counts:
        categorydict['FH'] = 25
        
    dice_set = set(dicedict.keys())
    # Large Straight (5 consecutive values)
    if len(dice_set) == 5 and (max(dice_set) - min(dice_set) == 4):
        categorydict['LS'] = 40
    # Small Straight (4 consecutive values)
    if ({1, 2, 3, 4}.issubset(dice_set) or 
        {2, 3, 4, 5}.issubset(dice_set) or 
        {3, 4, 5, 6}.issubset(dice_set)):
        categorydict['SS'] = 30
        
    # Chance
    categorydict['C'] = dicesum
    
    # Upper Section Scoring
    for i in range(1, 7):
        if dicedict[i] > 0:
            categorydict[str(i)] = dicedict[i] * i
            
    return dicedict, categorydict