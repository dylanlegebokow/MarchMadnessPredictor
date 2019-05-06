# Computes Sigmoid Function on 2019 dataset and outputs winners

import numpy as np
import os
import random
import sys
num_weights = 28
file_weights = 'data\weights.csv'
team_data = 'data\PredictionData\DataForML\data_2019.csv'
mm_bracket = 'data\PredictionData\MMBracket_2019.csv'
winners_file = 'data\PredictionData\Winners_2019.csv'
uf_winners_file = 'winners_2019.txt'
team_names = 'data\Team_IDs.csv'


# Returns a school's name
def get_team_name(team_id):
    with open(team_names) as x:
        lines = x.readlines()
        for line in lines:
            id, name = line.split(',')
            if team_id == id:
                return name.strip('\n')
    return False


# Returns the school's statistics
def get_team_stats(team_id):
    with open(team_data) as h:
        stats = h.readlines()
        for stat in stats:
            if stat[:4] == team_id:
                team_stats = stat.strip('\n').split(',')
                team_stats[0] = '1'
                team_stats = list(map(float, team_stats))
                return np.array(team_stats)
    return False


# Returns a school's ID
def get_team_id(mm_seed):
    with open('data\PredictionData\MMSeeds_with_Team_IDs.csv') as a:
        a_lines = a.readlines()
        for a_line in a_lines:
            _, seed, team_id = a_line.split(',')
            if mm_seed == seed:
                return team_id.strip('\n')
    with open(winners_file) as a:
        a_lines = a.readlines()
        for a_line in a_lines:
            seed, team_id = a_line.strip('\n').split(',')
            if mm_seed == seed:
                return team_id
    return False


# Classifies the probability as to either the higher seeded team won (1) or lower seeded team won (0)
def classify_probability(prob):
    if prob >= 0.5: return 1
    else: return 0


# Returns a random number between 0 and 1, and determines the winner of a game based on probability
# Returns 1 if higher seeded team won, 0 if lower seeded team won
def classify_with_rng(prob):
    rand_num = random.random()
    if rand_num <= prob: return 1
    else: return 0


# Returns the probability that the higher seeded team will win
def sigmoid_function(z):
    return 1.0 / (1.0 + np.exp(-z))


def calculate_odds(weights, team_difference):
    ans = np.dot(team_difference, weights.T)
    return sigmoid_function(ans)


# Writes to file that is only useful for computer computation
def append_to_winners(game_id, team_id):
    to_write = str(game_id) + ',' + str(team_id) + '\n'
    with open(winners_file, "a") as w:
        w.write(to_write)


# Writes to user friendly file that shows predicted winners and losers
def append_to_uf_winners(team_1, team_2, winner, prob):
    to_write_1 = "Game:\t" + str(team_1) + " vs " + str(team_2) + "\nWinner:\t" + str(winner) + \
                 "\nWin %:\t" + str(prob) + "\n-------------------------\n"
    with open(uf_winners_file, "a") as y:
        y.write(to_write_1)


# Removes old prediction file if exists, creates a new one
def initialize():
    if os.path.isfile(winners_file):
        os.remove(winners_file)
    if os.path.isfile(uf_winners_file):
        os.remove(uf_winners_file)


def predict(rng_flag):

    # If rng_flag is set, software uses probability along with random number to determine who wins (non-deterministic)
    # If rng_flag is not set, software only selects team with highest winning probability (deterministic)

    initialize()

    # Read the weights and cast as an np.array
    with open(file_weights) as f:
        for i, line in enumerate(f):
            if i == 1:
                weights = np.zeros((num_weights,))
                weights_list = line.strip('\n').split(',')
                for i in range(num_weights):
                    weights[i] = weights_list[i]

    # Read each game one at a time and figure out the probability of one team winning
    # Needs to be done this way, as previous predictions are used to make future predictions
    with open(mm_bracket) as g:
        games = g.readlines()
        for game in games:
            _, game_id, team_1_seed, team_2_seed = game.split(',')
            team_2_seed = team_2_seed.strip('\n')

            if game_id == 'Slot':
                continue

            team_1_seed = str(team_1_seed)
            team_2_seed = str(team_2_seed)

            team_1_id = get_team_id(team_1_seed)
            team_2_id = get_team_id(team_2_seed)

            team_1_stats = get_team_stats(team_1_id)
            team_2_stats = get_team_stats(team_2_id)

            if team_1_stats[1] > team_2_stats[1]:
                temp = team_1_stats
                team_1_stats = team_2_stats
                team_2_stats = temp
                temp = team_1_id
                team_1_id = team_2_id
                team_2_id = temp

            difference = team_1_stats - team_2_stats
            difference[0] = 1 #Done so w * x works as: w0 + w1x1 + w2x2...
            assert(difference[1] <= 0)  # Asserts that we minused the lower seeded team from the higher seeded team

            high_seed_win_odds = calculate_odds(difference, weights)
            if rng_flag == 0:
                winning_team = classify_probability(high_seed_win_odds)
            elif rng_flag == 1:
                winning_team = classify_with_rng(high_seed_win_odds)
            else:
                print('ERROR: rng_flag has invalid value.')
                sys.exit()


            # Outputs game results to two different files
            team_1_string = get_team_name(team_1_id) + '(' + str(int(team_1_stats[1])) + ')'
            team_2_string = get_team_name(team_2_id) + '(' + str(int(team_2_stats[1])) + ')'
            if winning_team == 1:
                append_to_uf_winners(team_1_string, team_2_string, team_1_string, round(high_seed_win_odds, 5))
                append_to_winners(game_id, team_1_id)
            else:
                append_to_uf_winners(team_1_string, team_2_string, team_2_string, round((1 - high_seed_win_odds), 5))
                append_to_winners(game_id, team_2_id)