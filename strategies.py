import basicfunctions as bf

#Very primitive strategy: Choose the highest points category from the first roll
def primitive(scoringdict):
    #Roll the dice and save the results in dicedict and the possible scoring categories in the categorydict
    dicedict, categorydict = bf.scoredice(bf.diceroll())
    highestscore = 0
    highestkey = ""
    #Loop through the possible scoring categories and select the highest available
    for k,v in categorydict.items():
        if scoringdict[k] is None:
            if v > highestscore:
                highestscore = v
                highestkey = k
    #Assign the value to the scoringdict as the turn score
    if highestkey != "":
        scoringdict[highestkey] = highestscore
    #If none of the possible combinations are available (already filled), fill in one of the open categories with a zero
    else:
        for k in scoringdict.keys():
            if scoringdict[k] is None:
                scoringdict[k] = 0
                break

#More human-like strategy: try to make "3 of a kind"s into "4 of a kind"s into yahtzees; "small straight"s into "large straight"s
def advanced(scoringdict):
    rolldict = []
    # Loop through three turns
    for t in range(3):
        dicedict, categorydict = bf.scoredice(bf.diceroll(rolldict))
        #Check for yahtzees first of all
        if 'Y' in categorydict:
            if scoringdict['Y'] is None:
                scoringdict['Y'] = categorydict['Y']
                break
            #If we get a yahtzee for a second time, add a yahtzee bonus (+100) to all other categories
            elif scoringdict['Y'] != 0:
                for k in categorydict:
                    if k != 'Y':
                        categorydict[k] = categorydict[k] + 100
        #Check for 4 of a kind
        if '4ok' in categorydict and scoringdict['4ok'] is None:
            #On the last turn, or in the case of a yahtzee bonus, add the score and end the turn
            if t == 2 or categorydict['4ok'] > 100:
                scoringdict['4ok'] = categorydict['4ok']
                break
            #Otherwise, take the group of 4 dice that match and add it to the rolldict to be excluded from roling again
            for k,v in dicedict.items():
                if v == 4:
                    rolldict = [k] * 4
                    continue
        #Full houses are rare enough that here we would end the round automatically, regardless of the turn
        if 'FH' in categorydict and scoringdict['FH'] is None:
            scoringdict['FH'] = categorydict['FH']
            break

        #Check for 3 of a kind
        if '3ok' in categorydict and scoringdict['3ok'] is None:
            #On the last turn, or in the case of a yahtzee bonus, add the score and end the turn
            if t == 2 or categorydict['3ok'] > 100:
                scoringdict['3ok'] = categorydict['3ok']
                break
            #Otherwise, take the group of 3 dice that match and add it to the rolldict to be excluded from roling again
            for k,v in dicedict.items():
                if v == 3:
                    rolldict = [k] * 3
                    continue
        #Check for a large straight and automatically end the round if there is one
        if 'LS' in categorydict and scoringdict['LS'] is None:
            scoringdict['LS'] = categorydict['LS']
            break
        #Check for small straight
        if 'SS' in categorydict and scoringdict['SS'] is None:
            #On the last turn, add the score to the scoringdict
            if t == 2:
                scoringdict['SS'] = categorydict['SS']
                break
            #Otherwise, use the dicedict to determine which Small Straight was found and exclude it from the next roll
            if 1 in dicedict and 2 in dicedict:
                rolldict = [1,2,3,4]
                continue
            if 6 in dicedict and 5 in dicedict:
                rolldict = [3,4,5,6]
                continue
            rolldict = [2,3,4,5]
            continue
        #If none of the lower categories were found, re-roll
        if t<2:
            continue

        #On the last turn, if we get to this point, apply the primitive logic
        highestscore = 0
        highestkey = ""
        for k,v in categorydict.items():
            if scoringdict[k] is None:
                if v > highestscore:
                    highestscore = v
                    highestkey = k
        if highestkey != "":
            scoringdict[highestkey] = highestscore
        else:
            for k in scoringdict.keys():
                if scoringdict[k] is None:
                    scoringdict[k] = 0
                    break

#Same logic as "advanced", but with a different order for filling in Zeros on missed rolls
def advancedCustomOrder(scoringdict):
    rolldict = []
    for t in range(3):
        dicedict, categorydict = bf.scoredice(bf.diceroll(rolldict))
        if 'Y' in categorydict:
            if scoringdict['Y'] is None:
                scoringdict['Y'] = categorydict['Y']
                break
            elif scoringdict['Y'] != 0:
                for k in categorydict:
                    if k != 'Y':
                        categorydict[k] = categorydict[k] + 100

        if '4ok' in categorydict and scoringdict['4ok'] is None:
            if t == 2 or categorydict['4ok'] > 100:
                scoringdict['4ok'] = categorydict['4ok']
                break
            for k,v in dicedict.items():
                if v == 4:
                    rolldict = [k] * 4
                    continue

        if 'FH' in categorydict and scoringdict['FH'] is None:
            scoringdict['FH'] = categorydict['FH']
            break

        if '3ok' in categorydict and scoringdict['3ok'] is None:
            if t == 2 or categorydict['3ok'] > 100:
                scoringdict['3ok'] = categorydict['3ok']
                break
            for k,v in dicedict.items():
                if v == 3:
                    rolldict = [k] * 3
                    continue

        if 'LS' in categorydict and scoringdict['LS'] is None:
            scoringdict['LS'] = categorydict['LS']
            break

        if 'SS' in categorydict and scoringdict['SS'] is None:
            if t == 2:
                scoringdict['SS'] = categorydict['SS']
                break
            if 1 in dicedict and 2 in dicedict:
                rolldict = [1,2,3,4]
                continue
            if 6 in dicedict and 5 in dicedict:
                rolldict = [3,4,5,6]
                continue
            rolldict = [2,3,4,5]
            continue

        if t<2:
            continue

        highestscore = 0
        highestkey = ""
        for k,v in categorydict.items():
            if scoringdict[k] is None:
                if v > highestscore:
                    highestscore = v
                    highestkey = k
        if highestkey != "":
            scoringdict[highestkey] = highestscore
        else:
            for k in ['1','2','3','4','5','6','C','3ok','4ok', 'FH', 'SS', 'LS', 'Y']:
                if scoringdict[k] is None:
                    scoringdict[k] = 0
                    break

#Lots of the same logic as for the other advanced strategies, but with a different focus for the upper categories:
    #Instead of filling in the upper category with the highest possible score of those available, this strategy chooses the mode.
    #This helps in cases where a player ends a turn with a list of dice like [1,1,3,5,6] where the other advanced models might
    #fill in the '6' category with it's lowest possible value, severely limiting the total possible score of the game and especially
    #the upper category bonus.
def advancedModeUpper(scoringdict):
    rolldict = []
    for t in range(3):
        dicedict, categorydict = bf.scoredice(bf.diceroll(rolldict))
        if 'Y' in categorydict:
            if scoringdict['Y'] is None:
                scoringdict['Y'] = categorydict['Y']
                break
            elif scoringdict['Y'] != 0:
                for k in categorydict:
                    if k != 'Y':
                        categorydict[k] = categorydict[k] + 100

        if '4ok' in categorydict and scoringdict['4ok'] is None:
            if t == 2 or categorydict['4ok'] > 100:
                scoringdict['4ok'] = categorydict['4ok']
                break
            for k,v in dicedict.items():
                if v == 4:
                    rolldict = [k] * 4
                    continue

        if 'FH' in categorydict and scoringdict['FH'] is None:
            scoringdict['FH'] = categorydict['FH']
            break

        if '3ok' in categorydict and scoringdict['3ok'] is None:
            if t == 2 or categorydict['3ok'] > 100:
                scoringdict['3ok'] = categorydict['3ok']
                break
            for k,v in dicedict.items():
                if v == 3:
                    rolldict = [k] * 3
                    continue

        if 'LS' in categorydict and scoringdict['LS'] is None:
            scoringdict['LS'] = categorydict['LS']
            break

        if 'SS' in categorydict and scoringdict['SS'] is None:
            if t == 2:
                scoringdict['SS'] = categorydict['SS']
                break
            if 1 in dicedict and 2 in dicedict:
                rolldict = [1,2,3,4]
                continue
            if 6 in dicedict and 5 in dicedict:
                rolldict = [3,4,5,6]
                continue
            rolldict = [2,3,4,5]
            continue

        if t<2:
            continue

        modevalue = 0
        modekey = ""
        for k,v in categorydict.items():
            if k != 'C':
                if scoringdict[k] is None:
                    if dicedict[int(k)] > modevalue:
                        modevalue = dicedict[int(k)]
                        modekey = k
        if modekey != "":
            scoringdict[modekey] = categorydict[modekey]
            break
        else:
            if 'C' in categorydict and scoringdict['C'] is None:
                scoringdict['C'] = categorydict['C']
                break
            for k in scoringdict.keys():
                if scoringdict[k] is None:
                    scoringdict[k] = 0
                    break

#This strategy uses the same logic as "advancedModeUpper", but goes even further to prioritize the upper categories:
    #In cases where three of a kind or four of a kind are possible, if the number that occurs multiple times is 4 or
    #greater, this strategy will opt to fill in the upper category first to get better odds on the upper category bonus.
def advancedModeUpperPlus(scoringdict):
    rolldict = []
    for t in range(3):
        dicedict, categorydict = bf.scoredice(bf.diceroll(rolldict))
        if 'Y' in categorydict:
            if scoringdict['Y'] is None:
                scoringdict['Y'] = categorydict['Y']
                break
            elif scoringdict['Y'] != 0:
                for k in categorydict:
                    if k != 'Y':
                        categorydict[k] = categorydict[k] + 100

        if 'LS' in categorydict and scoringdict['LS'] is None:
            scoringdict['LS'] = categorydict['LS']
            break

        if 'SS' in categorydict and scoringdict['SS'] is None:
            if t == 2:
                scoringdict['SS'] = categorydict['SS']
                break
            if 1 in dicedict and 2 in dicedict:
                rolldict = [1,2,3,4]
                continue
            if 6 in dicedict and 5 in dicedict:
                rolldict = [3,4,5,6]
                continue
            rolldict = [2,3,4,5]
            continue

        if 'FH' in categorydict and scoringdict['FH'] is None:
            scoringdict['FH'] = categorydict['FH']
            break

        if '4ok' in categorydict and scoringdict['4ok'] is None:
            if t == 2 or categorydict['4ok'] > 100:
                for x in [4,5,6]:
                    if dicedict[x] >= 4 and scoringdict[str(x)] is None:
                        scoringdict[str(x)] = categorydict[str(x)]
                        break
                scoringdict['4ok'] = categorydict['4ok']
                break
            for k,v in dicedict.items():
                if v == 4:
                    rolldict = [k] * 4
                    continue

        if '3ok' in categorydict and scoringdict['3ok'] is None:
            if t == 2 or categorydict['3ok'] > 100:
                for x in [4,5,6]:
                    if dicedict[x] >= 3 and scoringdict[str(x)] is None:
                        scoringdict[str(x)] = categorydict[str(x)]
                        break
                scoringdict['3ok'] = categorydict['3ok']
                break
            for k,v in dicedict.items():
                if v == 3:
                    rolldict = [k] * 3
                    continue

        if t<2:
            continue

        modevalue = 0
        modekey = ""
        for k,v in categorydict.items():
            if k != 'C':
                if scoringdict[k] is None:
                    if dicedict[int(k)] > modevalue:
                        modevalue = dicedict[int(k)]
                        modekey = k
        if modekey != "":
            scoringdict[modekey] = categorydict[modekey]
            break
        else:
            if 'C' in categorydict and scoringdict['C'] is None:
                scoringdict['C'] = categorydict['C']
                break
            for k in scoringdict.keys():
                if scoringdict[k] is None:
                    scoringdict[k] = 0
                    break
