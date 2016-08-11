from norms import *
import math
import numpy as np
import matplotlib.pyplot as plt

def product(uA, uB, f):
    """
    Function implements realization of some function (for example norm) between two fuzzy numbers.
    :param uA: fuzzy number, for example: [[0.1, 0.2, 0.8], [2, 3, 4]]
    :param uB: fuzzy number, for example: [[0.1, 0.2, 0.8], [2, 3, 4]]
    :param f: definition of function, which we want to implement
    :return: result of function between two fuzzy numbers
    """
    result = []
    result_d = []
    for i in range(max(len(uA[0]), len(uB[0]))):
        for j in range(i, min(len(uA[0]), len(uB[0]))):
            if (uA[1][i] == uB[1][j]):
                    result.append(f(uA[1][i], uB[1][j]))
                    result_d.append(uA[1][i])
        return ([result, result_d])



def sum_fs(uA, uB, f):
    """
    Function implements sum of two fuzzy number
    :param uA: first fuzzy number, for example: [[0.1, 0.2, 0.8], [2, 3, 4]]
    :param uB: second fuzzy number, for example: [[0.1, 0.2, 0.8], [2, 3, 4]]
    :param f: function, which is used to create sum's result
    :return: sum's result
    """
    result = []
    result_d = []
    for i in range(max(len(uA[0]), len(uB[0]))):
            for j in range(i, min(len(uA[0]), len(uB[0]))):
                if (uA[1][i] == uB[1][j]):
                    result.append(f(uA[1][i], uB[1][j]))
                    result_d.append(uA[1][i])
    return ([result, result_d])


def standard(x):
    return 1 - x

def negation(uA, f):
    """
    Function implements fuzzy number's negation. It's necessary to define negation's function.
    :param uA: fuzzy number, for example: [[0.1, 0.2, 0.8], [2, 3, 4]]
    :param f: negation's function
    :return: negated fuzzy number
    """
    result = []
    for xA in uA[0]:
        result.append(f(xA))
    return ([result, uA[1]])


def concentration(uA):
    """
    Function implements concentration of fuzzy number.
    :param uA: fuzzy number, for example: [[0.1, 0.2, 0.8], [2, 3, 4]], which we want to concentrate.
    :return: concentated fuzzy number
    """
    return [list(np.array(uA[0])**2), uA[1]]


def extension(uA):
    """
    Function implements extension of fuzzy number.
    :param uA: fuzzy number, for example: [[0.1, 0.2, 0.8], [2, 3, 4]], which we want to extend.
    :return: extended fuzzy number
    """
    return [list(np.array(uA[0])**(1/2)), uA[1]]
    pass


def contrast_intensification(uA, a):
    """
    Function implements fuzzy number's contrast intensification
    :param uA: fuzzy number, for example: [[0.1, 0.2, 0.8], [2, 3, 4]]
    :param a: intensification's param (scalar)
    :return: fuzzy number after contrast intensification
    """
    result = []
    for elem in uA[0]:
        if elem < 0.5:
            result.append(2**(a - 1)*elem**a)
        else:
            result.append(1 - 2**(a-1)*(1 - elem)**a)
    return [result, uA[1]]


def contrast_reduction(uA, a):
    """
    Function implements fuzzy number's contrast reduction
    :param uA: fuzzy number, for example: [[0.1, 0.2, 0.8], [2, 3, 4]]
    :param a: intensification's param (scalar)
    :return: fuzzy number after contrast reduction
    """
    result = []
    for elem in uA[0]:
        if elem < 0.5:
            expon = float(1/a)
            result.append((elem/2**(a - 1))**(expon))
        else:
            expon = float(1/a)
            result.append(1 - ((1 - elem)/2**(a - 1))**(expon))
    return [result, uA[1]]
    pass
