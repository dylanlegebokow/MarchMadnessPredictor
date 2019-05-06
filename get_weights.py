import csv
import numpy as np
import os

# Files
filename = 'data\difference_vectors.csv'
file_weights = 'data\weights.csv'

epochs = 1000
learning_rate = 0.0000006

# Normalizes all the values in the matrix
def normalize(this_X):
    minimums = np.min(this_X, axis=0)
    maximums = np.max(this_X, axis=0)
    max_minus_min = maximums - minimums
    normalized_X = 1 - ((maximums - this_X) / max_minus_min)
    return normalized_X


# Returns the probability of an event happening
def sigmoid_function(this_beta, this_X):
    return 1.0 / (1 + np.exp(-np.dot(this_X, this_beta.transpose())))


# Returns the log gradient
def log_gradient(this_beta, this_X, this_y):
    return np.dot((sigmoid_function(this_beta, this_X) - this_y.reshape(this_X.shape[0], -1)).T, this_X)


# Calculates the cost function
def calculate_cost(this_beta, this_X, this_y):
    this_y = np.squeeze(this_y)
    probability = sigmoid_function(this_beta, this_X)
    return np.mean(-(this_y * np.log(probability)) - ((1 - this_y) * np.log(1 - probability)))


# Runs gradient descent
def gradient_descent(this_X, this_y, this_beta):
    for m in range(epochs):
        this_beta = this_beta - (learning_rate * log_gradient(this_beta, this_X, this_y))
    return this_beta


# Predicts values off of our training dataset
def predict_values(beta, X):
    probability_of_win = sigmoid_function(beta, X)
    team_won = np.where(probability_of_win >= 0.5, 1, 0)
    return np.squeeze(team_won)


# Creates weights' value string
def create_string(weights):
    weights = weights.tolist()
    w = ''
    for i in weights:
        for j in i:
            w = w + str(j) + ','
    w = w.strip(',')
    return w


# Creates string of weight labels
def create_labels(count):
    labels = []
    for i in range(count):
        labels.append('w'+str(i))
    labels = ','.join(labels).strip(',') + '\n'
    return labels


# Print the weights to file
def print_weights(labels, w):
    with open(file_weights, 'w+') as f:
        f.writelines([labels, w])


def get_weights():

    # Remove old values of weights
    os.remove(file_weights)

    # Reads in the datapoints
    with open(filename, "r") as f:
        lines = csv.reader(f)
        dataset = list(lines)
        for i in range(len(dataset)):
            dataset[i] = [float(x) for x in dataset[i]]
    dataset = np.array(dataset)

    # Normalizes X matrix
    X = normalize(dataset[:, :-1])

    # Adds column of 1's to beginning of X matrix
    X = np.hstack((np.matrix(np.ones(X.shape[0])).T, X))

    # Creates the vector of labels
    y = dataset[:, -1]

    # Initialize weights matrix, runs gradient descent
    weights = np.matrix(np.zeros(X.shape[1]))
    weights = gradient_descent(X, y, weights)

    # Run predictions against old dataset
    predictions = predict_values(weights, X)
    correct_predictions = np.sum(y==predictions)
    total_predictions = np.size(y)
    prediction_accuracy = "  Correct Labels:   " + str(correct_predictions) + ' / ' + str(total_predictions) + "    (" \
                +str(round((correct_predictions / total_predictions), 5)) + ")"

    # Write new values of weights
    w = create_string(weights)
    count = w.count(',')

    # Write weights' labels
    labels = create_labels(count + 1)

    # Print w to file
    print_weights(labels, w)

    return prediction_accuracy
