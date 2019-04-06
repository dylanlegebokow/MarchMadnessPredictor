----------------------------------------
March Madness Bracket Predictor

Dylan Legebokow		V00846654
Chengyang He		V00791092
----------------------------------------

Created using Python 3.


Relavent files and folders:
- \data : Raw data used for creating data points for logistic regression
- \data\ConferenceTournament : Contains data on which teams won their conference tournament for a given year
- \data\DataForML : Contains team vectors for a given year
- \data\PredictionData : All data pertaining to 2019 March Madness
- \data\RatingStats : Contains data on team's advanced statistics for a given year
- \data\TeamStats : Contains data on team's basic statistics for a given year
- \data\data.csv : Data points used for logistic regression
- data.py : Creates an individual team's vector of attributes for training data
- format_2019_data.py : Creates an individual team's vector of attributes for data to predict
- get_data_points.py : Creates the difference vectors used for training
- get_weights.py : Runs logistic regression with gradient descent, returns weights
- predict.py : Uses the weights created by get_weights.py and applies them to 2019 data and outputs results
- utils.py : Contains many helper functions for data processing
- weights.csv : The output of running get_weights.py, used for predicting


For the basic use-case of running our code, run the following commands:
1) $ python get_weights.py
	Runs logistic regression with gradient descent on \data\data.csv (already pre-processed data)
	Finds weights and outputs them to weights.csv
2) $ python predict.py
	Predicts the likelihood of the higher seeded team winning using weights.csv and \data\PredictionData\data_2019.csv
	Outputs to console of which team will win each game
	Outputs winning team's ID to winners_2019.csv


For a more complete use-case of running our code (includes processing data), run the following commands:
1) $ python data.py
2) $ python format_2019_data.py
3) $ python get_data_points.py
4) $ python get_weights.py
5) $ python predict.py