# MarchMadnessPredictor
This software using logistic regression and gradient descent to predict the outcome of March Madness. The software uses historical data from March Madness tournaments between 1993 and 2016. It compares the difference in two teams' statistics for a game, and categorizes the output depending on if the higher-seeded team won the game.

### Prerequisits
- Python3

### Running the Software
This software can be run using the command line 
1. Clone this repository to your local machine
2. Using the command line, ``` $cd ``` into the location you copied this repository
3. Run ``` $python script.py <param_1> <param_2>``` to predict this year's bracket
<param_1> {0,1} : Set to 1 if you want the entire software to run, including formatting all the old data, creating the weights, and predicting the 2019 tournament. Set to 0 to only predict as all the files have already been created.
<param_2> {0,1} : Set to 1 to use a probabilistic approach, where if team X is given a 75% chance to win, we select them to win 3/4 times. Set to 0 to use a classifying approach to determine which team won, where the winning team is the team that has above 50% chance to win the game. 

### Parameters Used for Logistic Regression
- LIST PARAMETERS HERE
Definitions of terms found at:
https://www.basketball-reference.com/about/glossary.html

### Things To Improve
- Currently, data.py and data_2019.py are doing almost identical tasks. Should be consolidated into one file so changes are easier to implement in the future.
- Use variables as file names instead of hardcoding them into the software
- Improve functions for setting vectors

### Built With
- Python3

### Authors
- Dylan Legebokow
