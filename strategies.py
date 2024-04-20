def strategy1(dicedict, categorydict, scoringdict, current_turn = 0):
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
    #print((highestkey,highestscore))
    return