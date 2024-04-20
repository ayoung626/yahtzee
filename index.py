import statistics as stat
import random
import time
import numpy as np
import basicfunctions as bf
import strategies as strat
import scipy.stats as st

#A list of the strategies from the strategies.py file.
strategylist = [strat.primitive, strat.advanced, strat.advancedCustomOrder, strat.advancedModeUpper, strat.advancedModeUpperPlus]
resultlist = []
#Loop through the strategies, games, and turns
for s in strategylist:
    start_time = time.time()
    random.seed = 123456
    finalscoreslist = []
    #10,000 game replications
    for _ in range(10000):
        scoringdict = {'Y':None,
                       'FH':None,
                       'LS':None,
                       'SS':None,
                       'C':None,
                       '4ok':None,
                       '3ok':None,
                       '1':None,
                       '2':None,
                       '3':None,
                       '4':None,
                       '5':None,
                       '6':None}
        #13 turns per game
        for i in range(13):
            s(scoringdict)
        totalscore = 0
        uppersectionscore = 0
        #Sum the scores for each category
        for k,v in scoringdict.items():
            totalscore +=v
            #Also get the total score for the upper section categories
            if k in ['1','2','3','4','5','6']:
                uppersectionscore += v
        #If the upper section categories add up to 63 or more, then 35 is added to the total score
        if uppersectionscore>=63:
            totalscore+=35
        finalscoreslist.append(totalscore)
    totaltime = "%s seconds" % round((time.time() - start_time), 2)
    #Add the name of the strategy, the mean score, the 95% confidence interval, the standard deviation of the score, and the total time to a list for printing.
    resultlist.append((str(s).split(" ")[1], np.mean(finalscoreslist), st.t.interval(0.95, df=len(finalscoreslist)-1, loc=np.mean(finalscoreslist),  scale=st.sem(finalscoreslist)), stat.stdev(finalscoreslist), totaltime))
for r in resultlist:
    print(r)