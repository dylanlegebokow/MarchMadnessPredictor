# MarchMadnessPredictor
This software uses logistic regression and gradient descent to predict the outcome of the 2019 March Madness Tournament. The training dataset includes individual March Madness tournament game outcomes between 1993 and 2016. Each datapoint is the difference in two teams' season statistics for a single game. Lastly, the software categorizes the output depending on if the higher-seeded team won the game or not.

### Prerequisits
- Python3
- NumPy v1.16.0

### Running the Software
1. Clone this repository to your local machine
2. Using the command line, ``` $cd ``` into the location you copied this repository
3. In the main directory, run ``` $python script.py <param_1> <param_2>```<br>
	- <param_1> {0,1} : Set to 1 if you want the entire software to run, including formatting all the old data, creating the weights, and predicting the 2019 tournament. Set to 0 to only predict as all the files have already been created.<br>
	- <param_2> {0,1} : Set to 1 to use a probabilistic approach, where if team X is given a 75% chance to win, we select them to win 3/4 times. Set to 0 to use a classifying approach to determine which team won, where the winning team is the team that has above 50% chance to win the game. 
4. Once the software has completed running, check the ```winners_2019.txt``` file in the main directory to see the predicted outcomes of the tournament. Example run: 
```ShellSession
$python script.py 1 0
```

### Built With
- Python3

### Authors
- Dylan Legebokow

---

### How It Works
1. For each team in March Madness for a given year, create a vector where each element in the vector corresponds to some statistic. For example:<br>
```python
North Carolina = [1, 40, 33, 30.875, ..., 1, 0]
```
2. For each game in March Madness for a given year, subtract the lower-seeded team's vector from the higher-seeded team's vector, and label the vector depending on if the higher-seeded team won. For example:<br>
```python
	North Carolina 	       -      Florida Gulf Coast       = 	 Game Vector	        Label
[1, 40, 33, 30.875, ..., 1, 0] - [16, 35, 21, 28.8, ..., 0, 0] = [-15, 5, 12, 2.075, ... 1, 0]   [1]
```
3. After creating every game vector in each March Madness Tournament, we use the Game Vectors as our training data for gradient descent with logistic regression.
4. After calculating the weights, we use the weights to predict each game in the 2019 March Madness Tournament. For example:
```python
	   Gonzaga	       -	   F Dickinson		 = 	    Game Vector
[1, 34, 31, 32.235, ..., 0, 1] - [16, 35, 21, 26.314, ..., 0, 0] = [-15, -1, 10, 5.912, ..., 0, 1]

	  Game Vector 		   * 			Weights				    = High Seed Wins %
[1, -15, -1, 10, 5.912, ..., 0, 1] * [0.104, 0.032, 0.091, 0.067, 0.054, ..., 0.043, 0.061] = 	   0.982
```

### Parameters Used
G, W, FGM, FGP, 3P, 3P%, FT, FT%, ORB, TRB, AST, STL, BLK, TOV, PF, PPG, OPPG, SOS, OSRS, DSRS, ORTG, DRTG, CTW, CTL
- CTW = Conference Tournament Winner
- CTL = Conference Tournament Runner-Up
- Rest of definitions found at:
https://www.basketball-reference.com/about/glossary.html

### 2019 Tournament Predictions
To see the text output for the 2019 tournament predictions (including the probability the higher seeded team wins), click [here](https://github.com/dylanlegebokow/MarchMadnessPredictor/blob/master/winners_2019.txt)
To see a filled out bracket based on predictions and also see how accurate the predictions were to the actual results, click [here](https://github.com/dylanlegebokow/MarchMadnessPredictor/blob/master/2019_Predictions.jpg).

### Future Work
- Don't use the NumPy package as it is relatively slow
- Research what statistics are most accurate at predicting basketball game outcomes and use those statistics
- Include data on 2017, 2018 tournaments

### Issues with Accuracy
- Not using statistics that are most consistent with predicting basketball game outcomes
- Very small training dataset (1546 datapoints between 1993 and 2016 March Madness Tournament Winners)
- Some datapoints have missing entries (IE in 1993 season, there is no information on ORTG or DRTG. However, I decided to include this data so our training set would be bigger) 

### Data
Data mostly collected from:
- https://www.sports-reference.com/cbb/
- https://github.com/adeshpande3/March-Madness-2017
