import basicfunctions as bf

def strategy1(scoringdict):
    dicedict, categorydict = bf.scoredice(bf.diceroll())
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
    return

def strategy2(scoringdict):
    rolldict = []
    for t in range(3):
        dicedict, categorydict = bf.scoredice(bf.diceroll(rolldict))
        if 'Y' in categorydict:
            if scoringdict['Y'] is None:
                scoringdict['Y'] = categorydict['Y']
                break
            elif scoringdict != 0:
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
            for k in scoringdict.keys():
                if scoringdict[k] is None:
                    scoringdict[k] = 0
                    break
        
    return

def strategy3(scoringdict):
    rolldict = []
    for t in range(3):
        dicedict, categorydict = bf.scoredice(bf.diceroll(rolldict))
        if 'Y' in categorydict:
            if scoringdict['Y'] is None:
                scoringdict['Y'] = categorydict['Y']
                break
            elif scoringdict != 0:
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
            for k in reversed(scoringdict.keys()):
                if scoringdict[k] is None:
                    scoringdict[k] = 0
                    break
        
    return

def strategy4(scoringdict):
    rolldict = []
    for t in range(3):
        dicedict, categorydict = bf.scoredice(bf.diceroll(rolldict))
        if 'Y' in categorydict:
            if scoringdict['Y'] is None:
                scoringdict['Y'] = categorydict['Y']
                break
            elif scoringdict != 0:
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
        
    return

def strategy5(scoringdict):
    rolldict = []
    for t in range(3):
        dicedict, categorydict = bf.scoredice(bf.diceroll(rolldict))
        if 'Y' in categorydict:
            if scoringdict['Y'] is None:
                scoringdict['Y'] = categorydict['Y']
                break
            elif scoringdict != 0:
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
        
    return
