#############################################################
# FILE : ex5.py
# WRITER : konstantin , guybrush , 30888377
# EXERCISE : intro2cs ex5 2014-2015
# DESCRIPTION:
# This function sets perform a perceptron type of classification
# on a data set and can also check if the classifier derived is
# "perfect" or it hold errors in it.
#############################################################


def dot(lst_a, lst_b):
    """
    This function performs the Vector's Dot product, the sum of multiplying
    each part of the vector with the same part (index) in the other vector
    and return the sum of this multiplication process.
    this only work correctly if their sizes are the same.
    :param lst_a: Vector represented in a list
    :param lst_b: another Vector represented in a list
    :return: sum, the dot product of A & B
    """
    summation = 0
    for i in range(len(lst_a)):
        summation += lst_a[i]*lst_b[i]
    return summation


def update_w(weight, label, data_row):
    """
    This function updates the weights list with the new sign
    :param weight: will hold out Weights list from before
    :param label: is our label sign
    :param data_row: our vector in the data who we add
    :return: None
    """
    i = 0
    while i < len(weight):
        weight[i] = weight[i] + label*data_row[i]
        i += 1

def sign(num):
    """
    takes a number and returns it's sign
    :param: num is an int or float
    :return: -1,0,1 according to the sign of num
    """
    if num > 0:
        return 1
    elif num == 0:
        return 0
    return -1


def perceptron(data, labels):
    """
    Performs the Perceptron algorithm to try and find a classifier for data
    set given.
    :param data: list of lists, outer bound is m inner bound is n
    :param labels: list of a length m, representing the signs of the rows in
    data. Sign is represented with a 1 and -1.
    :return: a tuple constructed from a list of weights representing our
    linear classifier and a float bias b.
    """
    UPDATE_ITERATE_MAX = 10 * len(data)         # as per instruction

    weights = [0]*len(data[0])      # init weights as a list with n 0'z
    bias = 0                      #init bias as 0

    total_updates = 0

    while total_updates < UPDATE_ITERATE_MAX:
        # this part checks if the signs are equal, if they are opposite their
        # multiplication will give a negative number or 0 and we will need to
        # update our weights, start iterating a new, and update_count by 1
        # otherwise we continue on
        update_count = 0

        for i in range(len(data)):
            if (sign(dot(weights, data[i]) - bias)) != labels[i]:
                update_w(weights, labels[i], data[i])
                bias = bias - labels[i]
                update_count += 1
            
        if update_count == 0:
            return weights, bias
        
        total_updates += update_count
        
    #if a classifer is not found return None
    return None, None


def generalization_error(data, labels, w, b):
    """
    This function checks whether the weights gained together with the bias
    are able to predict the label for a data set given to it
    :param data: a list of lists, mXn size
    :param labels: a list of labels, 1 and -1 in accordance with data
    :param w: a set of weights to be used to predict the sign
    :param b: a bias together with the the weights
    :return: a list of 0's or 1's for right or wrong predictions
    """
    result = [0]*len(data)
    for i in range(len(data)):
        if sign((dot(data[i], w) - b)) != labels[i]:
            result[i] = 1
    return result


def vector_to_matrix(vec):
    """
    This function receives a list and turns it into a list of lists nXn size
    This function assumes the vec given has a whole square number
    :param vec: a list to be turned to
    :return: matrix, list of list, the size of nXn from len(vec)
    """
    matrix = []
    lst_size = int(len(vec) ** 0.5)
    for i in range(0, len(vec), lst_size):
        matrix.append(vec[i:i+lst_size])
    return matrix
 

def classifier_4_7(data, labels):
    """
    This function receives a list of lists and runs the perceptron algorithm
    on them in order to find a classifier for pictures of 4 and 7
    :param data: a list of lists, where the rows are a list to be turned
    into a matrix and the inner parts are floats
    :param labels: the signs for our test suit, negative for 4 and positive
    for a 7
    :return: a tupple with: the perceptron result, either a (weight, bias) if
    found or a (None, None) pair if no classifier can be found
    """
    return perceptron(data, labels)


def test_4_7(train_data, train_labels, test_data, test_labels):
    """
    This function tests the perceptron on a given data set to find a
    classfier, and then uses that classifier on a different data set and
    compares whether there are errors or not.
    :param train_data: training data we will use to make a classifier
    :param train_labels: the labels for that data set
    :param test_data: the data for which our current classifier will be used
    against.
    :param test_labels: the labels for that test data to compare for errors.
    :return: a tuple holding the classifier(list) and bias and a list of
    errors against the labels for the test_data
    """
    result = perceptron(train_data, train_labels)
    if result[0] is None:
        return None, None, None
    else:
        errors = generalization_error(test_data, test_labels,
                                                result[0], result[1])
        return result[0], result[1], errors

