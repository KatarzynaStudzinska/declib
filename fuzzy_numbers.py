from norms import *
import math
import matplotlib.pyplot as plt


class FuzzyNumbers():

    def subtraction(self, uA, uB, t_nrm):
        """
        Function realises uA - uB
        :param uA: minued (fuzzy number, for example: [[0.1, 0.2, 0.8], [2, 3, 4]])
        :param uB: subtrahend (fuzzy number, for example: [[0.1, 0.2, 0.8], [2, 3, 4]])
        :param t_nrm: T - norm, which we use
        :return: result of substraction (fuzzy number, for example: [[0.1, 0.2, 0.8], [2, 3, 4]])
        """

        if len(uA[0]) > len(uB[0]):
            uL = uA
            uS = uB
        else:
            uL = uB
            uS = uA

        z = []
        zd = []
        zu = []
        for L in range(len(uL[0])):
            for S in range(len(uS[0])):
                t_norm_s_l = t_nrm(uL[0][L], uS[0][S])
                z.append([t_norm_s_l, uL[1][L] - uS[1][S]])
                zu.append(t_norm_s_l)
                zd.append(uL[1][L] - uS[1][S])

        result = []
        result_dwn = []

        for i in range(len(zu)):
            if not result_dwn.__contains__(zd[i]):
                result.append([zu[i], zd[i]])
                result_dwn.append(zd[i])
            else:
                index = result_dwn.index(zd[i])
                result[index][0] = max(zu[i], result[index][0])
        finald = []
        finalu = []

        for elem in result:
            finalu.append(elem[0])
            finald.append(elem[1])
        final = [finalu, finald]
        return (final)

    def multiplication(self, uA, uB, t_nrm):
        """
        Function realises uA * uB
        :param uA: first multiplier (fuzzy number, for example: [[0.1, 0.2, 0.8], [2, 3, 4]])
        :param uB: second multiplier (fuzzy number, for example: [[0.1, 0.2, 0.8], [2, 3, 4]])
        :param t_nrm: T - norm, which we use
        :return: result of multiplication (fuzzy number, for example: [[0.1, 0.2, 0.8], [2, 3, 4]])
        """
        if len(uA[0]) > len(uB[0]):
            uL = uA
            uS= uB
        else:
            uL= uB
            uS= uA

        z = []
        zd = []
        zu = []
        for L in range(len(uL[0])):
            for S in range(len(uS[0])):
                t_norm_s_l = t_nrm(uL[0][L], uS[0][S])
                z.append([t_norm_s_l, uL[1][L] * uS[1][S]])
                zu.append(t_norm_s_l)
                zd.append(uL[1][L] * uS[1][S])

        result = []
        result_dwn = []

        for i in range(len(zu)):
            if not result_dwn.__contains__(zd[i]):
                result.append([zu[i], zd[i]])
                result_dwn.append(zd[i])
            else:
                index = result_dwn.index(zd[i])
                result[index][0] = max(zu[i], result[index][0])
        finald = []
        finalu = []

        for elem in result:
            finalu.append(elem[0])
            finald.append(elem[1])
        final = [finalu, finald]
        return (final)

    def division(self,uA, uB, t_nrm):
        """
        Function realises uA / uB
        :param uA: divided (fuzzy number, for example: [[0.1, 0.2, 0.8], [2, 3, 4]])
        :param uB: divider (fuzzy number, for example: [[0.1, 0.2, 0.8], [2, 3, 4]])
        :param t_nrm: T - norm, which we use
        :return: result of division (fuzzy number, for example: [[0.1, 0.2, 0.8], [2, 3, 4]])
        """
        if len(uA[0]) > len(uB[0]):
            uL = uA
            uS = uB
        else:
            uL = uB
            uS = uA

        z = []
        zd = []
        zu = []
        for L in range(len(uL[0])):
            for S in range(len(uS[0])):
                t_norm_s_l = t_nrm(uL[0][L], uS[0][S])
                z.append([t_norm_s_l, uL[1][L] / uS[1][S]])
                zu.append(t_norm_s_l)
                zd.append(uL[1][L] / uS[1][S])

        result = []
        result_dwn = []

        for i in range(len(zu)):
            if not result_dwn.__contains__(zd[i]):
                result.append([zu[i], zd[i]])
                result_dwn.append(zd[i])
            else:
                index = result_dwn.index(zd[i])
                result[index][0] = max(zu[i], result[index][0])
        finald = []
        finalu = []

        for elem in result:
            finalu.append(elem[0])
            finald.append(elem[1])
        final = [finalu, finald]
        return (final)

    def addition(self,uA, uB, t_nrm):
        """
        Function realises uA + uB
        :param uA: first addend (fuzzy number, for example: [[0.1, 0.2, 0.8], [2, 3, 4]])
        :param uB: second addend (fuzzy number, for example: [[0.1, 0.2, 0.8], [2, 3, 4]])
        :param t_nrm: T - norm, which we use
        :return: addition's result (fuzzy number, for example: [[0.1, 0.2, 0.8], [2, 3, 4]])
        """
        if len(uA[0]) > len(uB[0]):
            uL = uA
            uS= uB
        else:
            uL= uB
            uS= uA

        z = []
        zd = []
        zu = []
        for L in range(len(uL[0])):
            for S in range(len(uS[0])):
                t_norm_s_l = t_nrm(uL[0][L], uS[0][S])
                z.append([t_norm_s_l, uL[1][L] + uS[1][S]])
                zu.append(t_norm_s_l)
                zd.append(uL[1][L] + uS[1][S])

        result = []
        result_dwn = []

        for i in range(len(zu)):
            if not result_dwn.__contains__(zd[i]):
                result.append([zu[i], zd[i]])
                result_dwn.append(zd[i])
            else:
                index = result_dwn.index(zd[i])
                result[index][0] = max(zu[i], result[index][0])
        finald = []
        finalu = []

        for elem in result:
            finalu.append(elem[0])
            finald.append(elem[1])
        final = [finalu, finald]
        return (final)

    def alfa_addition(self, A, B, uA, uB, alfa):
        alfaAB = [A[0] + B[0], A[1] + B[1]]
        return [uA[0] + uB[0] + alfaAB[0]*alfa,uA[-1] + uB[-1] + alfaAB[-1]*alfa]


    def alfa_subtraction(self, A, B, uA, uB, alfa):
        alfaAB = [max(A[0] + B[0], A[1] + B[1]), min(A[0] - B[0], A[1] + B[1])]
        print(max(uA[0], uB[0]), min(uA[0], uB[0]))
        first = (max(uA[0], uB[0]) - min(uA[0], uB[0])) + alfaAB[0]*alfa
        last = (max(uA[1], uB[1]) - min(uA[1], uB[1])) + alfaAB[1]*alfa
        return [first,  last]

    def alfa_multiplication(self, A, B, uA, uB, alfa):
        alfaAB0 = max(A[0] * B[0], A[1] * B[1],A[1] * B[0], A[1] * B[0])
        alfaAB1 = min(A[0] * B[0], A[1] * B[1],A[1] * B[0], A[1] * B[0])
        return [uA[0] * uB[0] + alfaAB0*alfa, uA[-1] * uB[-1] + alfaAB1*alfa]

    def alfa_division(self, A, B, uA, uB, alfa):
        print(A[0] / B[0], A[1] / B[1],A[1] / B[0], A[1] / B[0])
        alfaAB0 = max(A[0] / B[0], A[1] / B[1],A[1] / B[0], A[1] / B[0])
        alfaAB1 = min(A[0] / B[0], A[1] / B[1],A[1] / B[0], A[1] / B[0])
        print(alfaAB0, alfaAB1)
        return [uA[0] / uB[0] + alfaAB0*alfa, uA[-1] / uB[-1] + alfaAB1*alfa]

    def one_dimension_enlarg(self, uA, snorm, g):
        uBd = []
        for elem in uA[1]:
            uBd.append(g(elem))
        return [uA[0], uBd]

if __name__ == "__main__":

    """A = [1, -2]
    uA = [3, 4, 6]
    B = [2, -1]
    uB = [6, 8, 10]
    alfa = 0
    print(alfa_division(A, B, uA, uB, alfa))"""

    # uB = [[0, 1, 0.7, 0.3, 0], [0.5, 1, 1.5, 2, 3]]
    # uA = [[0, 1, 0.5, 0], [4, 5, 6, 7]]
    # cos = subtraction(uA, uB, T_zadeh)
    # print(cos)
    # plt.plot(cos[1], cos[0], 'x')
    # plt.show()
    # uA = [[0, 1, 0.5, 0], [4, 5, 6, 7]]
    # print(one_dimension_enlarg(uA, S_fodor, math.sqrt))



