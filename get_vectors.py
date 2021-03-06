# Reads all data_xxxx.csv files and creates data points that will be used to train our model

import os
import numpy as np

# Files and Partial Files
difference_vectors = 'data\difference_vectors.csv'
team_data = 'data\DataForML\data_'
mm_outcomes = 'data\MMScores.csv'

vector_length = 26


# Reads in a team's statistics
def get_team_data(input_file, team_id):
    team_vector = np.zeros((vector_length,))
    with open(input_file) as g:
        raw_datas = g.readlines()
        for raw_data in raw_datas:
            this_team_id = str(raw_data[:4])
            if team_id == this_team_id:
                team_stats = raw_data.strip('\n').split(',')
                for i in range(len(team_stats)):
                    team_vector[i] = team_stats[i]
    return team_vector


# Appends each vector to the difference_vectors file
def append_vectors(point):
    string_to_write = []
    for i in point:
        string_to_write.append(str(i))
    string_to_write = ','.join(string_to_write)
    string_to_write = string_to_write + '\n'
    with open(difference_vectors, 'a') as h:
        h.write(string_to_write)


def get_vectors():

    # Removes the old data
    os.remove(difference_vectors)

    with open(mm_outcomes) as f:
        lines = f.readlines()
        for line in lines:
            season, _, winning_team_id, _, losing_team_id, _, _, _ = line.split(',')

            # Because the first instance is the title 'Season' and that isn't a year
            if season == 'Season':
                continue
            season = str(season)
            input_file = team_data+season+'.csv'

            # Finds the team stats and turns them into np.arrays
            winning_team_vector = get_team_data(input_file, winning_team_id)
            losing_team_vector = get_team_data(input_file, losing_team_id)

            # Used so we always minus the higher seeded team from the lower seeded team, then give the label
            if winning_team_vector[1] <= losing_team_vector[1]:
                point = winning_team_vector - losing_team_vector
                point[0] = 1
            else:
                point = losing_team_vector - winning_team_vector
                point[0] = 0
            point = np.roll(point, -1)

            # Append the string to the data.csv file
            append_vectors(point)
