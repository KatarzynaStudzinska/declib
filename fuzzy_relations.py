from norms import *
from decimal import *
from numpy import matrix
import math

class FuzzyRelations:

    @staticmethod
    def make_relation(X, Y, f):
        """
        :param X: list with n elements i.e. [a, b, c, d]
        :param Y: list with n elements i.e. [x, y, z, t]
        :param f: function
        :return: list with elements which are products of function on pair of elements [f(a,x), f(b,y), f(c,z), f(d,t)]
        """
        tab = []
        for ey in Y:
            line = []
            for ex in X:
                line.append(f(ey, ex))
            tab.append(line)
        return (tab)


    @staticmethod
    def assupT(X, Y, tn):
        """
        It make supremum-T-norm of two relations
        :param X: list with m n-element lists
        :param Y: list with n k-element lists
        :param tn:  T-norm, which we use
        :return: list with m k-element lists
        """
        result = []
        if isinstance(X[0], list):
            for jx in range(len(X)):
                line = []
                for jy in range(len(Y[0])):
                    value = []
                    for i in range(len(Y)):
                        value.append(tn(X[jx][i], Y[i][jy]))
                        pass
                    line.append(max(value))
                result.append(line)
            return result
        else:
            for jy in range(len(Y[0])):
                value = []
                for i in range(len(X)):
                    value.append(tn(X[i], Y[i][jy]))
                result.append(max(value))
            return result

    @staticmethod
    def asinfS(X, Y, sn):
        """
        It make infinium-S-norm of two relations
        :param X: list with m n-element lists
        :param Y: list with n k-element lists
        :param tn:  S-norm, which we use
        :return: list with m k-element lists
        """
        result = []
        if isinstance(X[0], list):
            for jx in range(len(X)):
                line = []
                for jy in range(len(Y[0])):
                    value = []
                    for i in range(len(Y)):
                        value.append(sn(X[jx][i], Y[i][jy]))
                        pass
                    line.append(min(value))
                result.append(line)
            return result
        else:
            for jy in range(len(Y[0])):
                value = []
                for i in range(len(X)):
                    value.append(sn(X[i], Y[i][jy]))
                result.append(min(value))
            return result

if __name__ == "__main__":
    def write_list(list):
        for line in list:
            print(line)

    def fu(x, y):
        return x*y

    X = [[2, 4], [1, 9], [2, 4]]
    Y = [[7, 5], [6, 2]]
    Aprim = [0, 0.5, 0.4, 0.3, 0]
    AimB = [[0.2, 0.5, 0.7, 1, 1], [0.3, 0.5, 0.7, 0.7, 0.7], [0.4, 0.5, 0.6, 0.6, 0.6], [0.5, 0.5, 0.5, 0.5, 0.5], [0.9, 0.9, 0.9, 0.9, 0.9]]
    print(FuzzyRelations.assupT(Aprim, AimB, min))

