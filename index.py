import statistics as stat
import random
import time
import numpy as np
import basicfunctions as bf
import strategies as strat
import scipy.stats as st
from matplotlib import pyplot as plt

#A list of the strategies from the strategies.py file.
strategylist = [strat.primitive, strat.advanced, strat.advancedCustomOrder, strat.advancedModeUpper, strat.advancedModeUpperPlus]
resultlist = []
roundedlist = []
numberofreplications = 10000
#Loop through the strategies, games, and turns
#STRATEGY LEVEL
for s in strategylist:
    start_time = time.time()
    random.seed = 123456
    finalscoreslist = []
    #Create a dictionary to keep track of the percentage of games that score in each category
    percentagecategoriesdict = {'Y':0.,
                            'FH':0.,
                            'LS':0.,
                            'SS':0.,
                            'C':0.,
                            '4ok':0.,
                            '3ok':0.,
                            '1':0.,
                            '2':0.,
                            '3':0.,
                            '4':0.,
                            '5':0.,
                            '6':0.}
    #GAME LEVEL
    for _ in range(numberofreplications):
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
        #ROUND LEVEL
        #13 rounds per game
        for i in range(13):
            s(scoringdict)
        totalscore = 0
        uppersectionscore = 0
        #Sum the scores for each category
        for k,v in scoringdict.items():
            #Ensure that no category is left empty
            if v is None:
                raise ValueError("The value of the key '{}' is None.".format(k))
            totalscore +=v
            if v != 0:
                percentagecategoriesdict[k] = percentagecategoriesdict[k] + 1/numberofreplications
            #Also get the total score for the upper section categories
            if k in ['1','2','3','4','5','6']:
                uppersectionscore += v
        #If the upper section categories add up to 63 or more, then 35 is added to the total score
        if uppersectionscore>=63:
            totalscore+=35
        finalscoreslist.append(totalscore)
    totaltime = "%s seconds" % round((time.time() - start_time), 2)
    #Add the name of the strategy, the mean score, the 95% confidence interval, the standard deviation of the score, and the total time to a list for printing.
    scoresmean = np.mean(finalscoreslist)
    scoresscale = st.sem(finalscoreslist)
    confidenceinterval = st.t.interval(0.95, df=len(finalscoreslist)-1, loc=scoresmean,  scale=scoresscale)
    resultlist.append((str(s).split(" ")[1], scoresmean, confidenceinterval , "Time of the Run: "+ str(totaltime)))
    roundeddict = {key: round(percentagecategoriesdict[key], 2) for key in percentagecategoriesdict}
    roundedlist.append(roundeddict)

#Create a grouped bar chart showing the proportion of games that were able to score in each category
strats = [r[0] for r in resultlist]
percentages = {key: [v for i in roundedlist for k, v in i.items() if k==key] for key in roundedlist[0].keys()}
x = np.arange(len(strats))
width = 0.075
multiplier = 0
fig, ax = plt.subplots(layout='constrained', figsize=(14,6))
for attribute, measurement in percentages.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3, fontsize = 6)
    multiplier += 1
ax.set_ylabel('Percentage of the Time Scored')
#ax.set_title('Strategies')
ax.set_xticks(x + 6.5*width, strats)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 1.25)
plt.show()

#Create another graphic for the score means and confidence intervals
plt.style.use('default')
fig, ax = plt.subplots(figsize=(14,6))
colorlist = ['r', 'y', 'g', 'b', 'm']
#Also print a tuple containing the results
for i, e in enumerate(resultlist):
    print(e)
    ax.errorbar(e[1], i, xerr=(e[2][1] - e[2][0]) / 2, fmt ='o', markersize=8, capsize=5, label = e[0], color = colorlist[i])
    plt.text(e[1]-0.8, i+0.2, round(e[1], 2))
ax.set_ylim(-0.6, 4.6)
ax.legend(loc='best', fontsize=11, framealpha=1, frameon = True)
ax.set_xlabel('Average Score', fontsize = 12)
ax.yaxis.set_major_formatter(plt.NullFormatter())
fig.tight_layout()
plt.show()