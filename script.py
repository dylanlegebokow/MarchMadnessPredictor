from data import get_data_historical
from get_vectors import get_vectors
from get_weights import get_weights
from predict import predict

import sys

if __name__ == "__main__":

    if len(sys.argv) != 3:
        assert False, ('Incorrect number of parameters')

    # If rng_flag is set, software returns non-deterministic predictions based on probability
    full_build_flag = int(sys.argv[1])
    rng_flag = int(sys.argv[2])

    if full_build_flag != 1 and full_build_flag != 0:
        assert False, ('full_build_flag must be either \'1\' or \'0\'')
    if rng_flag != 1 and rng_flag != 0:
        assert False, ('rng_flag must be either \'1\' or \'0\'')

    if full_build_flag == 1:
        # Format raw data into datapoints that can be used
        print('Formatting historical data...')
        get_data_historical(1993, 2017, 'data\MMSeeds_with_Team_IDs.csv', 'data')

        # Format raw 2019 tournament data into points that can be manipulated
        print('Formatting 2018-2019 season data...')
        get_data_historical(2019, 2020, 'data\PredictionData\MMSeeds_with_Team_IDs.csv',
                            'data\PredictionData')

        # Create vectors that will be used as datapoints for Logistic Regression
        print('Creating vectors...')
        get_vectors()

        # Create the weights using Logistic Regression
        print('Determining weights...')
        get_weights()

    # Predict the 2019 tournament bracket
    print('Predicting...')
    predict(rng_flag)

    print('Done')
