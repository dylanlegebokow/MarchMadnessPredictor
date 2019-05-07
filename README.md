# MarchMadnessPredictor
This software uses logistic regression and gradient descent to predict the outcome of the 2019 March Madness Tournament. The training dataset includes individual March Madness tournament game outcomes between 1993 and 2016. Each datapoint is the difference in two teams' season statistics for a single game. Lastly, the software categorizes the output depending on if the higher-seeded team won the game or not.

### Prerequisits
- Python3

### Running the Software
1. Clone this repository to your local machine
2. Using the command line, ``` $cd ``` into the location you copied this repository
3. In the main directory, run ``` $python script.py <param_1> <param_2>```<br>
	- <param_1> {0,1} : Set to 1 if you want the entire software to run, including formatting all the old data, creating the weights, and predicting the 2019 tournament. Set to 0 to only predict as all the files have already been created.<br>
	- <param_2> {0,1} : Set to 1 to use a probabilistic approach, where if team X is given a 75% chance to win, we select them to win 3/4 times. Set to 0 to use a classifying approach to determine which team won, where the winning team is the team that has above 50% chance to win the game. 
4. Once the software is completed, check the ```winners_2019.txt``` file in the main directory to see the predicted outcomes of the tournament<br><br>
Example method of running: ```$python script.py 1 0```

### Parameters Used
G, W, FGM, FGP, 3P, 3P%, FT, FT%, ORB, TRB, AST, STL, BLK, TOV, PF, PPG, OPPG, SOS, OSRS, DSRS, ORTG, DRTG, CTW, CTL
- CTW = Conference Tournament Winner
- CTL = Conference Tournament Runner-Up
- Rest of definitions found at:
https://www.basketball-reference.com/about/glossary.html

### Future Work
- Don't use NumPy as that package is relatively slow
- Research what statistics are more accurate at predicting basketball game outcomes and use those statistics
- Include data on 2017, 2018 tournaments

### Some Issues with Accuracy
- Not using statistics that are most consistent with predicting basketball game outcomes
- Very small training dataset (1546 datapoints between 1993 and 2016 March Madness Tournament Winners)
- Some datapoints have missing entries (IE in 1993 season, there is no information on ORTG or DRTG. However, I decided to include this data so our training set would be bigger) 

### Data
Collected mostly from https://www.sports-reference.com/cbb/

### Built With
- Python3

### Authors
- Dylan Legebokow
