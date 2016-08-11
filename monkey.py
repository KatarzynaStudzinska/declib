from PIL import Image

class Monkey:
    def monkey_extra(*args):
        """
        This method show monkey
        :param args: You can put here whatever you want
        """
        monkey = Image.open("extramonkey.jpg")
        monkey.show()


    def monkey1(*args):
        """
        This method show monkey
        :param args: You can put here whatever you want
        """
        monkey = Image.open("fs_monkey.jpg")
        monkey.show()


    def monkey2(*args):
        """
        This method show monkey
        :param args: You can put here whatever you want
        """
        monkey = Image.open("gtmonkey.jpg")
        monkey.show()
