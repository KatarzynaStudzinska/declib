
class Norms:
    @staticmethod
    def T_fodor(x, y):
        """

        :param x: 1. number  0<=x<=1
        :param y: 2. number 0<=y<=1
        :return:  Fodor T norm of x and y witch is >=0 and <=1
        """
        if x + y >1:
            return min(x, y)
        else:
            return 0

    @staticmethod
    def T_drastic(x, y):
        """
        :param x: 1. number  0<=x<=1
        :param y: 2. number 0<=y<=1
        :return: Drastic T norm of x and y witch is >=0 and <=1
        """
        if max(x, y) == 1:
            return min(x, y)
        else:
            return 0

    @staticmethod
    def T_zadeh(x, y):
        """
        :param x: 1. number  0<=x<=1
        :param y: 2. number 0<=y<=1
        :return: Zadeh T norm of x and y witch is >=0 and <=1
        """
        return min(x, y)

    @staticmethod
    def T_lukasiewicz(x, y):
        """
        :param x: 1. number  0<=x<=1
        :param y: 2. number 0<=y<=1
        :return: Lukasiewicz T norm of x and y witch is >=0 and <=1
        """
        return max(x+y -1, 0)

    @staticmethod
    def T_algebraic(x, y):
        """
        :param x: 1. number  0<=x<=1
        :param y: 2. number 0<=y<=1
        :return: Algebraic T norm of x and y witch is >=0 and <=1
        """
        return x*y

    @staticmethod
    def T_einstein(x, y):
        """
        :param x: 1. number  0<=x<=1
        :param y: 2. number 0<=y<=1
        :return: Einstein T norm of x and y witch is >=0 and <=1
        """
        return x*y/(2 - (x + y - x*y))

    @staticmethod
    def S_fodor (x, y):
        """
        :param x: 1. number  0<=x<=1
        :param y: 2. number 0<=y<=1
        :return: Fodor S norm of x and y witch is >=0 and <=1
        """
        if (x + y < 1):
            return max(x, y)
        else:
            return 1

    @staticmethod
    def S_drastic(x, y):
        """
        :param x: 1. number  0<=x<=1
        :param y: 2. number 0<=y<=1
        :return: Drastic S norm of x and y witch is >=0 and <=1
        """
        if (min(x,y) == 1):
            return min(x, y)
        else:
            return 1

    @staticmethod
    def S_zadeh(x, y):
        """
        :param x: 1. number  0<=x<=1
        :param y: 2. number 0<=y<=1
        :return: Zadeh S norm of x and y witch is >=0 and <=1
        """
        return max(x, y)

    @staticmethod
    def S_lukasiewicz(x, y):
        """
       :param x: 1. number  0<=x<=1
        :param y: 2. number 0<=y<=1
        :return: Lukasiewicz S norm of x and y witch is >=0 and <=1
        """
        return min(x + y, 1)

    @staticmethod
    def S_algebraic(x, y):
        """
       :param x: 1. number  0<=x<=1
        :param y: 2. number 0<=y<=1
        :return: Algebraic S norm of x and y witch is >=0 and <=1
        """
        return x + y - x*y

    @staticmethod
    def S_einstein (x,y):
        """
        :param x: 1. number  0<=x<=1
        :param y: 2. number 0<=y<=1
        :return: Einstein S norm of x and y witch is >=0 and <=1
        """
        return (x + y)/(1 + y*x)

