# Yahtzee
This Repository contains the files for My (Group 42's) submission for the ISYE 6644 final project. Running the index.py file will simulate a large number of yahtzee games and provide score means and confidence intervals for different game strategies. It also shows how the different strategies affect the probability of scoring in a certain category with each strategy.
## Contents
### index.py
This file conains the logic for running the simulations and printing the figures. It is set to 10,000 replications by default, but can be easily changed to run for more or fewer replications. When running the code, two graphics will be printed, as well as some descriptive tuples containing the name of each strategy, the mean score, the 95% confidence interval, and the time (proxy for relative complexity of the strategies) to run all of the replications
### basicfunctions.py
This file contains the logic for rolling the dice (diceroll function) and determining all available categories for the set of dice (scoredice function).
### strategies.py
