# Author: Katarzyna Studzinska & Piotr Kopa Ostrowski

"""A package for fuzzy numbers and sets operations. It can also shows monkeys."""

__version__ = '1.0.0'


def fuzzy_subtraction( uA, uB, t_nrm):
    """
    :param uA: list, which represents first fuzzy number: [[values], [arguments]]
    :param uB: list, which represents second fuzzy number: [[values], [arguments]]
    :param t_nrm: norm, which we want to use
    :return: list, which represents result fuzzy number: [[values], [arguments]]
    """
    from fuzzy_numbers import FuzzyNumbers
    return FuzzyNumbers.subtraction(uA, uB, t_nrm)


def make_ralation(X, Y, f):
    """
    :param X: list, which represents first fuzzy number: [[values], [arguments]]
    :param Y: list, which represents second fuzzy number:[[values], [arguments]]
    :param f: function, which we use to make relation
    :return: relation between two numbers
    """
    from fuzzy_relations import FuzzyRelations
    return FuzzyRelations.make_relation(X, Y, f)


def assupT(X, Y, tn):
    """
    :param X: list, which represents first fuzzy number: [[values], [arguments]]
    :param Y: list, which represents second fuzzy number:[[values], [arguments]]
    :param tn: T-norm, which is used to create assumption supremum
    :return: T-norm assumption
    """
    from fuzzy_relations import FuzzyRelations
    return FuzzyRelations.assupT(X, Y, tn)


def asinfS(X, Y, sn):
    """
    :param X: list, which represents first fuzzy number: [[values], [arguments]]
    :param Y: list, which represents second fuzzy number: [[values], [arguments]]
    :param sn: T-norm, which is used to create infimum assumption
    :return: S-norm assumption
    """
    from fuzzy_relations import FuzzyRelations
    return FuzzyRelations.assupT(X, Y, sn)


def T_fodor(x, y):
    """
    :param x: first number
    :param y: second number
    :return: normalized number
    """
    from norms import Norms
    return Norms.T_fodor(x, y)


def implication(A, B, ns, nt, neg):
    """
    :param A: antecedent, list, which represents fuzzy number: [[values], [arguments]]
    :param B: consequent, list, which represents fuzzy number: [[values], [arguments]]
    :param ns: S-norm
    :param nt: T-norm
    :param neg: negation
    :return: implication of A and B; list, which represents fuzzy number: [[values], [arguments]]
    """
    from logic_inference import LogicInference
    return LogicInference.implication(A, B, ns, nt, neg)


def modus_tollens(A, B, Bprim, ns, nt, neg):
    """

    :param A: antecedent of rule, list, which represents fuzzy number: [[values], [arguments]]
    :param B: consequent of rule, list, which represents fuzzy number: [[values], [arguments]]

    :param Bprim: factual consequent, list, which represents fuzzy number: [[values], [arguments]]
    :param ns: S - norm
    :param nt: T - norm
    :param neg: negation
    :return: factual antecedent, Aprim; list, which represents fuzzy number: [[values], [arguments]]
    """
    from logic_inference import LogicInference
    return LogicInference.modus_tollens(A, B, Bprim, ns, nt, neg)


def modus_pones(A, B, Aprim, ns, nt, neg):
    """

    :param A: antecedent of rule, list, which represents fuzzy number: [[values], [arguments]]
    :param B: consequent of rule, list, which represents fuzzy number: [[values], [arguments]]

    :param Aprim: factual antecedent, list, which represents fuzzy number: [[values], [arguments]]
    :param ns: S - norm
    :param nt: T - norm
    :param neg: negation
    :return: factual consequent, Bprim; list, which represents fuzzy number: [[values], [arguments]]
    """
    from logic_inference import LogicInference
    return LogicInference.modus_pones(A, B, Aprim, ns, nt, neg)


def generalized_syllogizm(A, B, C, Bprim, ns, nt, neg):
    """

    :param A: antecedent of first rule, list, which represents fuzzy number: [[values], [arguments]]
    :param B: consequent of first rule and antecedent of second rule, list, which represents fuzzy number: [[values], [arguments]]
    :param C: consequent of second rule, list, which represents fuzzy number: [[values], [arguments]]

    :param Bprim: factual antecedent of second rule, list, which represents fuzzy number: [[values], [arguments]]
    :param ns: S - norm
    :param nt: T - norm
    :param neg: negation
    :return: factual consequent, Cprim; list, which represents fuzzy number: [[values], [arguments]]
    """
    from logic_inference import LogicInference
    return LogicInference.generalized_syllogizm(A, B, C, Bprim, ns, nt, neg)


def FATI(implication_list, Aprim):
    """

    :param implication_list: list of rules: [[A, B, T-norm, S-norm, negation]]
    :param Aprim: factual antecedent, list, which represents fuzzy number: [[values], [arguments]]
    :return: factual consequent of agregated rules
    """
    from logic_inference import LogicInference
    return LogicInference.FATI(implication_list, Aprim)


def FITA(implication_list, Aprim):
    """

    :param implication_list: list of rules: [[A, B, T-norm, S-norm, negation]]
    :param Aprim: factual antecedent, list, which represents fuzzy number: [[values], [arguments]]
    :return: agregated factual consequents
    """
    from logic_inference import LogicInference
    return LogicInference.FITA(implication_list, Aprim)


def create_learned_anfis (teaching_data, anfis_num, start):
    """

    :param teaching_data: list of lists of inputs and output which are used to teach [[[int0, in1, in2, in3 ...], out ], ... ]
    :param anfis_num: number of anfis systems in generation
    :param start: start parameters [number of inputs, rules used in ANFIS system, Tnorm, down range of inputs, up range of inputs]
    :return: learned ANFIS system which give the best result
    """
    from anfis import Genetic
    return Genetic(teaching_data, anfis_num, start).best_anfis


def use_anfis (our_anfis, inputs):
    """

    :param our_anfis: object of class Anfis
    :param inputs: list of inputs which we use[int0, in1, in2, in3 ...]
    :return: output
    """
    our_anfis.run(inputs)
    return our_anfis.result


def show_first_monkey (*args):
    """

    :param args: you can type whatever you want
    """
    from monkey import Monkey
    Monkey.monkey1(*args)


def show_second_monkey (*args):
    """

    :param args: you can type whatever you want
    """
    from monkey import Monkey
    Monkey.monkey2(*args)


def show_extra_monkey (*args):
    """

    :param args: you can type whatever you want
    """
    from monkey import Monkey
    Monkey.monkey_extra(*args)

if __name__ == '__main__':

    Aprzyklad = [[1.0,1.0,1.0,1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    An1 = [[.8, .75, .7, .6, .55, .5, .35, .2, .1, .1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    Ar1 = [[0.1, 0.1, 0.3, 0.4, 0.5, 0.6, 0.7, 0.7, 0.7, 0.9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    An2 = [[1.0, .7, .6, .3, .2, .1, .05, .05, .05, .05], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    Ar2 = [[.1, .1, .5, .6, .65, .7, .7, .8, .8, .1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    An3 = [[1.0, .9, .6, .2, .1, .05, .05, .05, .05, .05], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    Ar3 = [[.1, 0.2, .3, .4, .4, .4, .6, .8, .8, .9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    An4 = [[0.9,0.5,0.3,0.1, 0.1, 0.05, 0.03, 0.02, 0.01, 0.01], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    Ar4 = [[0.3,0.4,0.45,0.7, 0.7, 0.8, 0.4, 0.7, 0.8, 0.9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    An5 = [[.2,.95,.5,.12, .04, .04, .04, .04, .04, .04], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    Ar5 = [[.1,.4,.4,.6, .6, .7, .9, .9, .9, .9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

    An6 = [[1.0,1.0,1.0,1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    Ar6 = [[1.0,1.0,1.0,1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    An7 = [[1.0,1.0,1.0,1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    Ar7 = [[1.0,1.0,1.0,1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    An8 = [[.9, .6, .3, .2, .05, .02, .02, .02, .02, .02], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    Ar8 = [[.3, .3, .4, .5, .6, .6, .7, .8, 1.0, 1.0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    An9 = [[1.0, .7, .6, .4, .35, .15, .05, .05, .02, .01], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    Ar9 = [[.5, .5, .5, .6, .65, .7, .75, .8, .9, 1.0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    An4 = Aprzyklad
    Ar4 = Aprzyklad
    An5 = Aprzyklad
    Ar5 = Aprzyklad
    # An8 = Aprzyklad
    # Ar8 = Aprzyklad
    #Aprzyklad = [[.0,.0,.0,.0, .0, .0, .0, .0, .0, .0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    reg_n = [An1, An2, An3, An4, An5, An6, An7, An8, An9]
    reg_r = [Ar1, Ar2, Ar3, Ar4, Ar5, Ar6, Ar7, Ar8, Ar9]
    rules = [reg_n, reg_r]
    import json
    with open('data.json', 'r') as fp:
        data = json.load(fp)
    T = data["rak_lub_nierak"]
    wyuczony = create_learned_anfis(T, 70, [10, rules, min, 0, 1])

    Testing = data["test"]
    print(Testing[30])
    use_anfis(wyuczony,Testing[30][0])
    print("wynik", wyuczony.result, "powinno byc", Testing[30][1])
    dobrze = 0
    zle = 0
    for t in Testing:
        use_anfis(wyuczony,t[0])
        if (wyuczony.result < 0.5 and t[1] == 0) or (wyuczony.result > 0.5 and t[1] == 1):
            dobrze += 1
        else:
            zle += 1
    print("dobrze: ", dobrze)
    print("zle: ", zle)
    print ("dobre wyniki", round(100*dobrze/(dobrze+zle),1) ,"%")
