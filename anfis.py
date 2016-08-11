#from __init__ import *
import random
import copy


# example rules
An1 = [[.8, .75, .7, .6, .55, .5, .35, .2, .1, .1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
Ar1 = [[0.1, 0.1, 0.3, 0.4, 0.5, 0.6, 0.7, 0.7, 0.7, 0.9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
An2 = [[1.0, .7, .6, .3, .2, .1, .05, .05, .05, .05], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
Ar2 = [[.1, .1, .5, .6, .65, .7, .7, .8, .8, .1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
An3 = [[1.0, .9, .6, .2, .1, .05, .05, .05, .05, .05], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
Ar3 = [[.1, 0.2, .3, .4, .4, .4, .6, .8, .8, .9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
An4 = [[1.0,1.0,1.0,1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
Ar4 = [[1.0,1.0,1.0,1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
An5 = [[1.0,1.0,1.0,1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
Ar5 = [[1.0,1.0,1.0,1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
An6 = [[1.0,1.0,1.0,1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
Ar6 = [[1.0,1.0,1.0,1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
An7 = [[1.0,1.0,1.0,1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
Ar7 = [[1.0,1.0,1.0,1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
An8 = [[.9, .6, .3, .2, .05, .02, .02, .02, .02, .02], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
Ar8 = [[.3, .3, .4, .5, .6, .6, .7, .8, 1.0, 1.0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
An9 = [[1.0, .7, .6, .4, .35, .15, .05, .05, .02, .01], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
Ar9 = [[.5, .5, .5, .6, .65, .7, .75, .8, .9, 1.0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

reg_n = [An1, An2, An3, An4, An5, An6, An7, An8, An9]
reg_r = [Ar1, Ar2, Ar3, Ar4, Ar5, Ar6, Ar7, Ar8, Ar9]
rules = [reg_n, reg_r]


class Anfis:

    def __init__(self, inputs_len, rules, Tnorm, down_range, up_range):
        """
        Initialization of ANFIS net
        :param inputs_len: nuber of inputs, that we use
        :param rules: list of rules [[fuzzy number, fuzzy number, fuzzy nuber...], [...], ...]
        :param Tnorm: norma T, which we use
        :param down_range: minimal value of p - params (polynomial's factor), it's also the down range of our output
        :param up_range: maximal value of p - params (polynomial's factor), it's also the up range of our output
        """
        self.rules = rules
        self.Tnorm = Tnorm
        self.p_list = make_p(down_range, up_range, inputs_len, len(rules))

    def change_params(self, rules, p_list):
        """
        Change params of ANFIS net
        :param rules: new rules [[fuzzy number, fuzzy number, fuzzy nuber...], [...], ...]
        :param p_list: lists of p - params (polynomial's factor)

        """
        self.rules = rules
        self.p_list = p_list

    def run(self, inputs):
        """
        In self.result we have a result of net's work on input's stimulation.
        :param inputs: list of inputs

        """
        self.inputs = inputs
        self.first_layer_outputs = self.first_layer()
        self.second_layer_outputs = self.second_layer()
        self.third_layer_outputs = self.third_layer()
        self.fourth_layer_outputs = self.fourth_layer()
        self.result = sum(self.fourth_layer_outputs)


    def fourth_layer(self):
        """
        It realizes net's fourth layer (sum of weighted outputs of third layer )
        :return: fourth layer outputs
        """

        fourth_layer_outputs = []
        for p_vector, tau in zip(self.p_list, self.third_layer_outputs):
            y0 = p_vector[0]    # bubel, nie uzywamy tego, ale niech zostanie dla potomnosci
            for x, p in zip(self.inputs, p_vector[1:]):# pojedziemy po dolach
                y0 += x*p
            y0 *= tau
            fourth_layer_outputs.append(y0)
        return fourth_layer_outputs

    def third_layer(self):
        """
        It realizes net's third layer (normalization of second layer's outputs )
        :return: third layer outputs
        """
        third_layer_outputs = []
        t_norm_sum = sum(self.second_layer_outputs[0])
        for number in self.second_layer_outputs[0]:
            third_layer_outputs.append(number/t_norm_sum)
        return third_layer_outputs

    def second_layer(self):
        """
        It realizes net's second layer - sum of T-norm of first layer's outputs
        :return: second layer outputs
        """

        second_up = []
        second_down = []
        for line, p_vector in zip(self.first_layer_outputs, self.p_list):
            second_up.append(min(line[0]))
            y0 = p_vector[0]
            for elem_down, p in zip(line[1], p_vector[1:]):
                y0 += elem_down*p
            second_down.append(y0)
        return [second_up, second_down]

    def first_layer(self):
        """
        It realizes net's first layer - checking input's compatibility with rules
        :return: first layer outputs
        """
        first_layer_outputs = []
        for rule in self.rules:
            rule_result_up = []
            rule_result_down = []
            for (fuzzy_A, i) in zip(rule, self.inputs):
                rule_result_up.append(fuzzy_A[0][i - 1])
                rule_result_down.append(i)
            first_layer_outputs.append([rule_result_up, rule_result_down])
        return first_layer_outputs


def negation(x):
    """
    :param x: param to negation
    :return: negated param
    """
    return 1 - x


def make_p(down_range, up_range, input_num, rules_num):
    """
    It rand p - params (polynomial's factor)
    :param down_range: minimal value of p - params (polynomial's factor), it's also the down range of our output
    :param up_range: maximal value of p - params (polynomial's factor), it's also the up range of our output
    :param input_num: number of inputs
    :param rules_num: number of rules
    :return: list of p - params
    """
    p = []
    for i in range(rules_num - 1):
        pp = []
        for j in range(input_num + 1):
            pp.append(random.uniform(down_range, up_range))
        p.append(pp)
    return p


def make_fuzzy_num(down_range, up_range):
    """
    It rand lists which represents fuzzy number [[x1,x2,x3...xn),[down_range, down_range+1, ... up_range]], 0<xi<1
    :param down_range:  First number over which will be fuzzy number
    :param up_range:    Last number over which will be fuzzy number
    :return: lists which represents fuzzy number [[x1,x2,x3...xn),[down_range, down_range+1, ... up_range]], 0<xi<1
    """
    fuzyy_num_up = []
    fuzyy_num_down = []
    for i in range(down_range, up_range + 1):
        fuzyy_num_up.append(round(random.random(), 3))
        fuzyy_num_down.append(i)
    return [fuzyy_num_up, fuzyy_num_down]


class Genetic:
    def __init__(self, teaching_inputs, anfis_num, start): #dane uczace, liczba anfisow w pokoleniu
        """
        Save in self.best_anfis ANFIS net which give the best answers
        :param teaching_inputs: list of teaching inputs [[[1. input, 2. input...], output], [...]]
        :param anfis_num: Number of ANFIS nets using in genetic teaching
        :param start: starts params of ANIFS net [inputs_len, rules, Tnorm, down_range, up_range]
        """
        self.last_error = 10000000
        self.best_result = 1000000
        self.start = start
        first_anfis_list = []
        self.teaching_inputs = teaching_inputs
        for i in range(anfis_num):
            new_anfis = Anfis(*start)
            first_anfis_list.append(new_anfis)
        self.best_anfis = first_anfis_list[0]
        population = first_anfis_list
        while self.last_error > 19:
            population = self.make_new_population(population)

    def cross_over (self, father, mother):
        """

        :param father: 1. ANFIS net
        :param mother: 2. ANFIS net
        :return: ANFIS net which has mixed features of two others nets: father and mother
        """
        num_one = random.randint(0, len(father.p_list[0]))
        num_two = random.randint(0, len(father.p_list[0]))
        while num_one == num_two:
            num_one = random.randint(0, len(father.p_list[0]))
            num_two = random.randint(0, len(father.p_list[0]))
        index_one = min(num_one, num_two)
        index_two = max(num_one, num_two)
        if num_one > len(father.p_list)/2:
            child = copy.deepcopy(father)
            child.p_list[0][index_one:index_two] = mother.p_list[0][index_one:index_two]
        else:
            child = copy.deepcopy(mother)
            child.p_list[0][index_one:index_two] = father.p_list[0][index_one:index_two]
        return child

    def make_new_population(self, population):
        """
        Makes new set of ANIS net using genetic teaching
        :param population: set of ANFIS nets
        :return: new set of ANIS nets
        """
        ordnung_population = self.sort_population(population)
        new_population = []

        new_population.append(population[0])
        new_population.append(population[1])
        new_population.append(population[2])
        new_population.append(population[3])

        length = len(ordnung_population)
        while not len(new_population) == length:
            lotery = random.randint(0, 10)
            if lotery < 5:
                end_range = int (len(ordnung_population)/2)
                mum = random.randint(0, end_range)
                dad = random.randint(0, end_range)
                new_anfis = self.cross_over(ordnung_population[mum], ordnung_population[dad])
            elif lotery < 8:
                new_anfis = ordnung_population[random.randint(4, len(ordnung_population) - 8)]
                ordnung_population.remove(new_anfis)
            else:
                new_anfis = Anfis(*self.start)

            if random.randint(0, 10) > 5:
                new_anfis = self.mutation(new_anfis)
            new_population.append(new_anfis)
        return new_population

    def mutation(self, anfis):
        """
        Changing random p-params of ANIFS net
        :param anfis: ANFIS net
        :return: CHanged ANFIS net
        """
        how_much = random.randint(0, len(anfis.p_list[0]) - 1)
        for i in range(how_much):
            index = random.randint(0, len(anfis.p_list[0]) - 1)
            anfis.p_list[0][index] = random.randint(-1, 1) * random.random()/10
        return anfis

    def sort_population(self, population):
        """
        Sort population of ANFIS net according to errors
        :param population: population of ANFIS nets
        :return:Sorted population
        """
        anfis_generation = []
        for anfis in population:
            anfis_errors = []
            for teaching_set in self.teaching_inputs:
                anfis.run(teaching_set[0])
                result = anfis.result
                error = (result - teaching_set[1])**2
                anfis_errors.append(error)
            anfis_generation.append([sum(anfis_errors), anfis])
        anfis_generation = self.sort_anfis_list(anfis_generation)
        self.last_error = anfis_generation[0][0]
        self.best_result = anfis_generation[0][1].result
        self.best_anfis = anfis_generation[0][1]
        sorted_population = []
        for pair in anfis_generation:
            sorted_population.append(pair[1])
        return sorted_population

    def sort_anfis_list(self, anfis_list):
        """
        :param anfis_list: List of ANFIS nets and their errors
        :return: sorted list of ANFIS nets and their errors
        """
        less = []
        equal = []
        greater = []
        if len(anfis_list) > 1:
            pivot = anfis_list[0]
            for x in anfis_list:
                if x[0] < pivot[0]:
                    less.append(x)
                if x[0] == pivot[0]:
                    equal.append(x)
                if x[0] > pivot[0]:
                    greater.append(x)
            return self.sort_anfis_list(less) + equal + self.sort_anfis_list(greater)
        else:
            return anfis_list


if __name__ == '__main__':

    import json
    with open('data.json', 'r') as fp:
        data = json.load(fp)
    T = data["rak_lub_nierak"]
    uczenie = Genetic(T, 70, [10, rules, min, 0, 1])
    wyuczony = uczenie.best_anfis

    Testing = data["test"]
    print(Testing[40])
    wyuczony.run(Testing[40][0])
    print("wynik", wyuczony.result, "powinno byc", Testing[40][1])

    dobrze = 0
    zle = 0
    for t in Testing:
        wyuczony.run(t[0])
        if (wyuczony.result < 0.5 and t[1] == 0) or (wyuczony.result > 0.5 and t[1] == 1):
            dobrze += 1
        else:
            zle += 1
    print("dobrze: ", dobrze)
    print("zle: ", zle)
