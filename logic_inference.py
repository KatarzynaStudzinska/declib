from __init__ import assupT

class LogicInference:
    @staticmethod
    def ziplist(A):
        """
        :param A: list of lists with 2 elements i.e. [[a1,b1],[a2,b2],[a3,b3],[a4,b4]]
        :return:  list with 2 lists i.e. [[a1,a2,a3,a4],[b1,b2,b3,b4]]
        """
        Aup = []
        Adown = []
        for elem in A:
            Adown.append(elem[1])
            Aup.append(elem[0])
        return [Aup, Adown]

    @staticmethod
    def unziplist(A):
        """
        :param A: list with 2 lists i.e. [[a1,a2,a3,a4],[b1,b2,b3,b4]]
        :return: list of lists with 2 elements i.e. [[a1,b1],[a2,b2],[a3,b3],[a4,b4]]
        """
        Aup, Adown = A
        result = []
        for u, d in zip(Aup, Adown):
            result.append([u, d])
        return result

    @staticmethod
    def negation(x):
        """
        :param x: number
        :return: 1-x
        """
        return 1 - x

    @staticmethod
    def adjust_Vprim(B, Bprim):
        """
        It's adjust fuzzy number Bprim to fuzzy number B. For every number where B is described and Bprim isn't is added
        pair 0 over this number. For example: B =[[0.5, 1, 0.5][1, 2, 3]], Bprim = [[0.5, 0.5],[2, 3]},
        return = [[0,0.5,0.5],[1, 2, 3]]
        :param B: list of 2 lists with the same number of elements [[x1,x2,x3,...xn][y1,y2,y3,...yn]]  0<=xi<=1
        :param Bprim: list of 2 lists with the same number of elements [[x1,x2,x3,...xm][y1,y2,y3,...ym]]  0<=xi<=1, m<=n
        :return: list of 2 lists, with the same sizes as B
        """
        if not(len(B[0]) == len(Bprim[0])):
            Bprim_up = []
            Bprim_down = []
            ii = 0
            for i in range(len(B[0])):
                if Bprim[1].__contains__(B[1][i]):
                    Bprim_up.append(Bprim[0][ii])
                    Bprim_down.append(Bprim[1][ii])
                    ii +=1
                else:
                    Bprim_up.append(0)
                    Bprim_down.append(B[1][i])

            Bprim = [Bprim_up, Bprim_down]
        return Bprim

    @staticmethod
    def adjust_postimplication_matrix(B, Bprim, post_impmatrix):
        """
        :param B: list of 2 lists with the same number of elements [[x1,x2,x3,...xn][y1,y2,y3,...yn]]  0<=xi<=1
        :param Bprim: list of 2 lists with the same number of elements [[x1,x2,x3,...xm][y1,y2,y3,...ym]]  0<=xi<=1, m<=n
        :param post_impmatrix: list of k-element list
        :return: list of k-element lists
        """
        if not(len(B[0]) == len(Bprim[0])):
            post_impmatrix_changed = []
            ii = 0
            for i in range(len(B[0])):
                if Bprim[1].__contains__(B[1][i]):
                    post_impmatrix_changed.append(post_impmatrix[ii])
                    ii +=1
                else:
                    post_impmatrix_changed.append([1]*len(post_impmatrix[0]))
            return post_impmatrix_changed
        return post_impmatrix
        pass

    @staticmethod
    def transposition(A):
        """
        :param A: List of n elements (i.e. [a,b,c]) of list of k lists with m elements [[a,b],[c,d],[e,f]]
        :return: In first case of A: list of n lists with one element (i.e. [[a],[b],[c]])
                 in  second case of A: list of m lists with k elements [[a,c,e],[b,d,f]]
        """
        result = []

        if isinstance(A[0], list):
            for elem in A:
                result.append(elem[0])
            return result
        if len(A)> 1:
            for elem in A:
                result.append([elem])
            return result

    @staticmethod
    def implication(A, B, ns, nt, neg):
        """
        :param A: 1.fact, list of 2 n-element lists
        :param B: 2. fact, list of 2 k-element lists
        :param ns: S norm witch you want use
        :param nt: T norm witch you want use
        :param neg: Negation witch you want use
        :return: list of k n-element lists
        """
        AsB = []
        for au in A[0]:
            asb = []
            for bu in B[0]:
                atb = nt(au, bu)
                na = neg(au)
                asb.append(ns(atb, na))
            AsB.append(asb)
        return AsB

    @staticmethod
    def modus_tollens(A, B, Bprim, ns, nt, neg):# [[gora], [dol]]
        """
        Modus tollens
        :param A: 1. fact, list of 2 n-element lists
        :param B: 2. fact,list of 2 k-element lists
        :param Bprim: premise list of 2 m-element lists, numbers in second of them must be also in second list in B
        :param ns: S norm witch you want use
        :param nt: T norm witch you want use
        :param neg: Negation witch you want use
        :return: list of 2 n-element lists
        """
        AsB = LogicInference.implication(A, B, ns, nt, neg)
        Bprim = LogicInference.adjust_Vprim(B, Bprim)
        Bprimup = LogicInference.transposition(Bprim[0])
        Aprim = [LogicInference.transposition(assupT(AsB, Bprimup, min)), A[1]]
        return Aprim

    @staticmethod
    def modus_pones(A, B, Aprim, ns, nt, neg):# [[gora], [dol]]
        """
        Modus pones
        :param A: 1.fact, list of 2 n-element lists
        :param B: 2.fact, list of 2 k-element lists
        :param Aprim: premise, list of 2 m-element lists, numbers in second of them must be also in second list in A
        :param ns: S norm witch you want use
        :param nt: T norm witch you want use
        :param neg: Negation witch you want use
        :return: list of 2 k-element lists
        """
        AimpB = LogicInference.implication(A, B, ns, nt, neg)
        Aprim = LogicInference.adjust_Vprim(A, Aprim)
        Bprim = [(assupT(Aprim[0], AimpB,  min)), B[1]]
        return Bprim

    @staticmethod
    def generalized_syllogizm(A, B, C, Bprim, ns, nt, neg):
        """
        Generalized syllogizm of 3 facts (A, B, C) and 1 premise (Bprim)
        :param A: 1.fact, list of 2 n-element lists
        :param B: 1.fact, list of 2 k-element lists
        :param C: 2.fact, list of 2 m-element lists
        :param Bprim: premise, list of 2 m-element lists, numbers in second of them must be also in second list in B
        :param ns: S norm witch you want use
        :param nt: T norm witch you want use
        :param neg: Negation witch you want use
        :return: list of 2 max m-element lists, numbers in second of them must be also in second list in C
        """
        AimpB = LogicInference.implication(A, B, ns, nt, neg)
        Bprim_imp_C = LogicInference.implication(Bprim, C, ns, nt, neg)
        Bprim_imp_C = LogicInference.adjust_postimplication_matrix(B, Bprim, Bprim_imp_C)
        Cprim = assupT(AimpB, Bprim_imp_C, nt)
        Cprim_up = []
        for c_column_number in range(len(Cprim[0])):
            C_buffor = []
            for c_poem_number in range(len(Cprim)):
                C_buffor.append(Cprim[c_poem_number][c_column_number])
            Cprim_up.append(min(C_buffor))

        Cprim = [Cprim_up, C[1]]

        return Cprim


    @staticmethod
    def agregation_FATI(implication_list):
        """
        :param implication_list: list of result of implication. Each result is list of n-element lists. in each basic
        basic list are n numbers >=0 and <=1
        :return: Agregated result, list of n-element lists. in each basic basic list are n numbers >=0 and <=1
        """
        result = []
        first_imp = implication_list[0]
        lines_number = len(first_imp)
        columns_number = len(first_imp[0])

        for i in range(lines_number):
            line = []
            for j in range(columns_number):
                buffor = []
                for imp in implication_list:
                    buffor.append(imp[i][j])
                line.append(max(buffor))
            result.append(line)
        return result

    @staticmethod
    def agregation_FITA(asum_list):
        """
        For every n it take nth element in lists of asum_list and make one list with these elements
        :param asum_list: list of n-element list
        :return: n-element list with numbers >=0 and <=1
        """
        result = []
        for i in range(len(asum_list[0])):
            buffor = []
            for asum in asum_list:
                buffor.append(asum[i])
            result.append(max(buffor))
        return result

    @staticmethod
    def adjust_fuzzy_numbers(Alist):
        """
        It modify every fuzzy number in list. Fuzzy number is write as [[a1,a2,...an],[b1,b2,...bn]]. After modification
        sets of b are the same. For every new bi is added new a1 = 0
        :param Alist: list with fuzzy numbers.
        :return: Modified list with fuzzy numbers
        """
        down_list = []
        for A in Alist:
            for i in A[1]:
                if not down_list.__contains__(i):
                    down_list.append(i)

        down_list.sort()

        new_A_list = []
        for A in Alist:
            A_up = []

            ii = 0
            for i in down_list:
                if A[1].__contains__(i):
                    A_up.append(A[0][ii])
                    ii += 1
                else:
                    A_up.append(0)
            new_A_list.append([A_up, down_list])
        return new_A_list

    @staticmethod
    def adjust_rules(rules_list):
        """
        Rule is saved as list [A, B, S-norm, T-norm, negation]. Then lists of 'A's and 'B's are modihy in
        adjust_fuzzy_numbers method, and save to lists
        :param rules_list: list of rules: [[A, B, S-norm, T-norm, negation],[A2, B2, S-norm, T-norm, negation],...]
        :return: Adjusted list of rules: [[A', B', S-norm, T-norm, negation],[A2', B2', S-norm, T-norm, negation],...]
        """
        A_list = []
        B_list = []

        for rules in rules_list:
            A, B, ns, nt, neg = rules
            A_list.append(A)
            B_list.append(B)
        A_list = LogicInference.adjust_fuzzy_numbers(A_list)
        B_list = LogicInference.adjust_fuzzy_numbers(B_list)

        for rules, A, B in zip(rules_list, A_list, B_list):
            rules[0] = A
            rules[1] = B

        return rules_list

    @staticmethod
    def FATI(rules_list, Aprim):
        """
        :param rules_list: list of rules: [[A, B, S-norm, T-norm, negation],[A2, B2, S-norm, T-norm, negation],...]
        A and B are fuzzy numbers, writen as list of 2 list with the same length
        :param Aprim: Fuzzy number saved as list of two lines with the same length
        :return: Fuzzy number saved as list of two lines with the same length
        """
        imp = []
        rules_list = LogicInference.adjust_rules(rules_list)

        for rules in rules_list:
            imp.append(LogicInference.implication(*rules))

        agregated_rules = LogicInference.agregation_FATI(imp)

        first_A_down  = rules_list[0][0]

        Aprim = LogicInference.adjust_fuzzy_numbers([Aprim, first_A_down])[0]  #pCz - jak adjustować?

        output = assupT(Aprim[0], agregated_rules,  min)

        output = [output, rules_list[0][1][1]]
        return output

    @staticmethod
    def FITA (rules_list, Aprim):
        """
        :param rules_list: list of rules: [[A, B, S-norm, T-norm, negation],[A2, B2, S-norm, T-norm, negation],...]
        A and B are fuzzy numbers, writen as list of 2 list with the same length
        :param Aprim: Fuzzy number saved as list of two lines with the same length
        :return: Fuzzy number saved as list of two lines with the same length
        """
        Bprim_list = []
        rules_list = LogicInference.adjust_rules(rules_list)
        first_A_down  = rules_list[0][0]

        for rules in rules_list:
            R = LogicInference.implication(*rules)
            Aprim = LogicInference.adjust_fuzzy_numbers([Aprim, first_A_down])[0]
            Bprim = assupT(Aprim[0], R, min)
            Bprim_list.append(Bprim)
        Bprim_up = LogicInference.agregation_FITA(Bprim_list)
        Bprim = [Bprim_up, rules_list[0][1][1]]
        return Bprim

if __name__ == "__main__":

    A = [[0.3, 0.7, 0.2, 0.3, 0.1], [ 1.5,  2, 3, 4, 5]]
    B = [[0.2, 0.3, 0.7, 0.1, 1], [3, 4, 5, 6, 8]]
    A1 = [[1, 0.7, 0.1, 0.2, 0.1], [0, 1, 1.5,  2, 3]]
    B1 = [[0.2, 0.5, 0.4, 1, 1], [3, 4, 5, 6, 7]]
    A2 = [[1, 0.1, 0.9, 0.1], [0, 1,  2, 3]]
    B2 = [[1, 0.7], [0, 1]]
    Aprim = [[0.7, 0.2, 0.3], [1, 1.5, 2]]

    ru1 = [A, B, min, max, LogicInference.negation]
    ru2 = [A1, B1, min, max, LogicInference.negation]
    ru3 = [A, B1, min, max, LogicInference.negation]
    ru4 = [A2, B2, min, max, LogicInference.negation]
    rules_list = [ru1, ru2, ru3, ru4]


