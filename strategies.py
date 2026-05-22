import basicfunctions as bf

# -----------------------------------------------------------------------------
# HELPER FUNCTIONS TO ELIMINATE CODE DUPLICATION AND BOILERPLATE
# -----------------------------------------------------------------------------

def _handle_yahtzee_bonus(scoringdict, categorydict):
    """
    Checks if a Yahtzee is rolled and updates scoringdict.
    If it is the first Yahtzee, scores 50 and returns True (ends the turn).
    If it is a subsequent Yahtzee (and the first was scored as 50), applies a +100 bonus
    to all other scoring options in categorydict.
    """
    if 'Y' in categorydict:
        if scoringdict['Y'] is None:
            scoringdict['Y'] = categorydict['Y']
            return True
        elif scoringdict['Y'] != 0:
            for k in categorydict:
                if k != 'Y':
                    categorydict[k] += 100
    return False

def _score_highest_available(scoringdict, categorydict, custom_zero_order=None):
    """
    Scores the highest points category among those available in categorydict.
    If none are available, fills in the first open category in custom_zero_order (or default keys) with 0.
    """
    highestscore = 0
    highestkey = ""
    for k, v in categorydict.items():
        if scoringdict[k] is None:
            if v > highestscore:
                highestscore = v
                highestkey = k
    if highestkey != "":
        scoringdict[highestkey] = highestscore
    else:
        zero_order = custom_zero_order or list(scoringdict.keys())
        for k in zero_order:
            if scoringdict[k] is None:
                scoringdict[k] = 0
                break

def _score_mode_upper(scoringdict, categorydict, dicedict):
    """
    Scores in the upper category corresponding to the mode of the rolled dice.
    If the mode upper category is already filled, attempts to score in Chance ('C').
    Otherwise, fills in the first available category with 0.
    """
    modevalue = 0
    modekey = ""
    for k in categorydict:
        # Check if the category is an upper section category ('1' to '6') safely using isdigit()
        if k.isdigit() and scoringdict[k] is None:
            if dicedict[int(k)] > modevalue:
                modevalue = dicedict[int(k)]
                modekey = k
    if modekey != "":
        scoringdict[modekey] = categorydict[modekey]
    elif 'C' in categorydict and scoringdict['C'] is None:
        scoringdict['C'] = categorydict['C']
    else:
        for k in scoringdict.keys():
            if scoringdict[k] is None:
                scoringdict[k] = 0
                break

# -----------------------------------------------------------------------------
# YAHTZEE STRATEGIES
# -----------------------------------------------------------------------------

# Very primitive strategy: Choose the highest points category from the first roll
def primitive(scoringdict):
    dicedict, categorydict = bf.scoredice(bf.diceroll())
    _score_highest_available(scoringdict, categorydict)

# More human-like strategy: try to make "3 of a kind"s into "4 of a kind"s into yahtzees; "small straight"s into "large straight"s
def advanced(scoringdict):
    rolldict = []
    # Loop through three turns
    for t in range(3):
        dicedict, categorydict = bf.scoredice(bf.diceroll(rolldict))
        
        # Check for yahtzees first of all
        if _handle_yahtzee_bonus(scoringdict, categorydict):
            break
            
        # Check for 4 of a kind
        if '4ok' in categorydict and scoringdict['4ok'] is None:
            if t == 2 or categorydict['4ok'] > 100:
                scoringdict['4ok'] = categorydict['4ok']
                break
            for k, v in dicedict.items():
                if v == 4:
                    rolldict = [k] * 4
                    continue
                    
        # Full houses are rare enough that here we would end the round automatically, regardless of the turn
        if 'FH' in categorydict and scoringdict['FH'] is None:
            scoringdict['FH'] = categorydict['FH']
            break

        # Check for 3 of a kind
        if '3ok' in categorydict and scoringdict['3ok'] is None:
            if t == 2 or categorydict['3ok'] > 100:
                scoringdict['3ok'] = categorydict['3ok']
                break
            for k, v in dicedict.items():
                if v == 3:
                    rolldict = [k] * 3
                    continue
                    
        # Check for a large straight and automatically end the round if there is one
        if 'LS' in categorydict and scoringdict['LS'] is None:
            scoringdict['LS'] = categorydict['LS']
            break
            
        # Check for small straight
        if 'SS' in categorydict and scoringdict['SS'] is None:
            if t == 2:
                scoringdict['SS'] = categorydict['SS']
                break
            if 1 in dicedict and 2 in dicedict:
                rolldict = [1, 2, 3, 4]
                continue
            if 6 in dicedict and 5 in dicedict:
                rolldict = [3, 4, 5, 6]
                continue
            rolldict = [2, 3, 4, 5]
            continue
            
        if t < 2:
            continue

        # On the last turn, apply primitive logic
        _score_highest_available(scoringdict, categorydict)

# Same logic as "advanced", but with a different order for filling in Zeros on missed rolls
def advancedCustomOrder(scoringdict):
    rolldict = []
    for t in range(3):
        dicedict, categorydict = bf.scoredice(bf.diceroll(rolldict))
        
        if _handle_yahtzee_bonus(scoringdict, categorydict):
            break

        if '4ok' in categorydict and scoringdict['4ok'] is None:
            if t == 2 or categorydict['4ok'] > 100:
                scoringdict['4ok'] = categorydict['4ok']
                break
            for k, v in dicedict.items():
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
            for k, v in dicedict.items():
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
                rolldict = [1, 2, 3, 4]
                continue
            if 6 in dicedict and 5 in dicedict:
                rolldict = [3, 4, 5, 6]
                continue
            rolldict = [2, 3, 4, 5]
            continue

        if t < 2:
            continue

        # On the last turn, fill in zeros in custom order
        _score_highest_available(
            scoringdict, 
            categorydict, 
            custom_zero_order=['1', '2', '3', '4', '5', '6', 'C', '3ok', '4ok', 'FH', 'SS', 'LS', 'Y']
        )

# Lots of the same logic as for the other advanced strategies, but with a different focus for the upper categories:
# Instead of filling in the upper category with the highest possible score of those available, this strategy chooses the mode.
def advancedModeUpper(scoringdict):
    rolldict = []
    for t in range(3):
        dicedict, categorydict = bf.scoredice(bf.diceroll(rolldict))
        
        if _handle_yahtzee_bonus(scoringdict, categorydict):
            break

        if '4ok' in categorydict and scoringdict['4ok'] is None:
            if t == 2 or categorydict['4ok'] > 100:
                scoringdict['4ok'] = categorydict['4ok']
                break
            for k, v in dicedict.items():
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
            for k, v in dicedict.items():
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
                rolldict = [1, 2, 3, 4]
                continue
            if 6 in dicedict and 5 in dicedict:
                rolldict = [3, 4, 5, 6]
                continue
            rolldict = [2, 3, 4, 5]
            continue

        if t < 2:
            continue

        # Score upper category corresponding to the mode of the rolled dice
        _score_mode_upper(scoringdict, categorydict, dicedict)

# This strategy uses the same logic as "advancedModeUpper", but goes even further to prioritize the upper categories:
# In cases where three of a kind or four of a kind are possible, if the number that occurs multiple times is 4 or
# greater, this strategy will opt to fill in the upper category first to get better odds on the upper category bonus.
def advancedModeUpperPlus(scoringdict):
    rolldict = []
    for t in range(3):
        dicedict, categorydict = bf.scoredice(bf.diceroll(rolldict))
        
        if _handle_yahtzee_bonus(scoringdict, categorydict):
            break

        if 'LS' in categorydict and scoringdict['LS'] is None:
            scoringdict['LS'] = categorydict['LS']
            break

        if 'SS' in categorydict and scoringdict['SS'] is None:
            if t == 2:
                scoringdict['SS'] = categorydict['SS']
                break
            if 1 in dicedict and 2 in dicedict:
                rolldict = [1, 2, 3, 4]
                continue
            if 6 in dicedict and 5 in dicedict:
                rolldict = [3, 4, 5, 6]
                continue
            rolldict = [2, 3, 4, 5]
            continue

        if 'FH' in categorydict and scoringdict['FH'] is None:
            scoringdict['FH'] = categorydict['FH']
            break

        if '4ok' in categorydict and scoringdict['4ok'] is None:
            if t == 2 or categorydict['4ok'] > 100:
                scored_upper = False
                for x in [4, 5, 6]:
                    if dicedict[x] >= 4 and scoringdict[str(x)] is None:
                        scoringdict[str(x)] = categorydict[str(x)]
                        scored_upper = True
                        break
                if not scored_upper:
                    scoringdict['4ok'] = categorydict['4ok']
                break
            for k, v in dicedict.items():
                if v == 4:
                    rolldict = [k] * 4
                    continue

        if '3ok' in categorydict and scoringdict['3ok'] is None:
            if t == 2 or categorydict['3ok'] > 100:
                scored_upper = False
                for x in [4, 5, 6]:
                    if dicedict[x] >= 3 and scoringdict[str(x)] is None:
                        scoringdict[str(x)] = categorydict[str(x)]
                        scored_upper = True
                        break
                if not scored_upper:
                    scoringdict['3ok'] = categorydict['3ok']
                break
            for k, v in dicedict.items():
                if v == 3:
                    rolldict = [k] * 3
                    continue

        if t < 2:
            continue

        # Score upper category corresponding to the mode of the rolled dice
        _score_mode_upper(scoringdict, categorydict, dicedict)
