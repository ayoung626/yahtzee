import simpy
import statistics
import statistics as stat
import random
import time
import basicfunctions as bf
import strategies as strat

start_time = time.time()
strategylist = [strat.strategy1, strat.strategy2]
resultlist = []
for s in strategylist:
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
    resultlist.append((str(s).split(" ")[1], stat.mean(finalscoreslist), stat.stdev(finalscoreslist)))
    #print(str(s).split(" ")[1])
    #print(stat.mean(finalscoreslist))
    #print(stat.stdev(finalscoreslist))
for r in resultlist:
    print(r)
print("%s seconds" % round((time.time() - start_time), 2))