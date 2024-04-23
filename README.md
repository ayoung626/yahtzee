# Yahtzee
This Repository contains the files for my (Group 42's) submission for the ISYE 6644 final project. Running the index.py file will simulate a large number of yahtzee games and provide score means and confidence intervals for different game strategies. It also shows how the different strategies affect the probability of scoring in a certain category with each strategy.
## Contents
### index.py
This file contains the logic for running the simulations and printing the figures. It is set to 10,000 replications by default, but can be easily changed to run for more or fewer replications. When running the code, two graphics will be printed, as well as some descriptive tuples containing the name of each strategy, the mean score, the 95% confidence interval, and the time (proxy for relative complexity of the strategies) to run all of the replications. This file uses the functions found in the other two python files.
### basicfunctions.py
This file contains the logic for rolling the dice (diceroll function) and determining all available categories for the set of dice (scoredice function). The diceroll function takes an optional list as a parameter to allow the "player" to keep dice for the following turn. The scoredice function will return all possible scoring combinations, which helps with the calculation of Yahtzee bonuses when a "player" has already gotten a Yahtzee.
### strategies.py
This file has the logic behind each of the strategies employed in the replications. Here is a brief explanation of each one.
* **primitive** \
This strategy does not make use of the three turns allotted to the player. It merely selects the highest scoring category of those available.
*  **advanced** \
The "advanced" strategy makes use of the three turns and has logic that keeps dice to try to increase the chances for some of the more difficult/rare lower category scoring sets like Yahtzees and Large Straights.
* **advancedCustomOrder** \
This strategy is exactly the same as the advanced strategy, but with a change in the order in which categories are "crossed out" in the case that the "player" does not end with a set of dice that match up with the open scoring categories. While the previous strategy crossed out the rarer categories first, this strategy crosses out the more common (and generally lower scoring) categories first. This strategy could be described as "risk seeking" while the previous is more "risk averse".
* **advancedModeUpper** \
Because the advancedCustomOrder strategy proved to be a step backward in terms of the mean score, this strategy places an emphasis on scoring in the upper category (aces, twos, threes, etc.). The major modification for this strategy is in the logic that governs which of upper categories to use when the lower categories (Yahtzee, Full House, Large Straight, etc.) are not open. The choice up until now was derived from the primitive strategy, basically saying that the "player" should choose whichever one has the highest score. The advancedModeUpper strategy takes a different approach. It uses the mode dice number instead of the maximum score. This helps the "player" to increase their chances of receiving the Upper Category Bonus, which adds 35 points on to the total score if the sum of scores in the upper categories is greater than 63.
* **advancedModeUpperPlus** \
This strategy is the same as advancedModeUpper, but further prioritizes the upper categories. In the case that a three or four of a kind is possible, this strategy will opt to score the dice set in the upper category instead of the lower category if the set is of fours, fives, or sixes. These help the "player" immensely as they try to get the Upper Category Bonus.
