import statistics as stat
import random
import time
import basicfunctions as bf
import strategies as strat

strategylist = [strat.strategy1, strat.strategy2, strat.strategy3, strat.strategy4, strat.strategy5]
resultlist = []
for s in strategylist:
    start_time = time.time()
    random.seed = 12345
    finalscoreslist = []
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
        for i in range(13):
            s(scoringdict)
        totalscore = 0
        uppersectionscore = 0
        for k,v in scoringdict.items():
            totalscore +=v
            if k in ['1','2','3','4','5','6']:
                uppersectionscore += v
        if uppersectionscore>=63:
            totalscore+=35
        finalscoreslist.append(totalscore)
    totaltime = "%s seconds" % round((time.time() - start_time), 2)
    resultlist.append((str(s).split(" ")[1], stat.mean(finalscoreslist), stat.stdev(finalscoreslist), totaltime))
for r in resultlist:
    print(r)