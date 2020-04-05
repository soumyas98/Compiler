import constants
import random


class DNA:
    def __init__(self):
        self.data = ''
        temp = []
        for i in range(len(constants.FLAGS)):
            x = random.uniform(0, 1)
            y = round(x)
            temp.append(str(y))
        self.data = ''.join(temp)
        
    def get_flags(self):
        flags = list()
        for i in range(len(self.data) - 1):
            if self.data[i] == '1':
                flags.append('-f' + constants.FLAGS[i])
            else:
                flags.append('-fno' + constants.FLAGS[i])
        if self.data[-1] == '0':
            flags.append('-f' + constants.FLAGS[-1])
        else:
            flags.append('-fno-' + constants.FLAGS[-1])
        return ' '.join(flags)


if __name__ == '__main__':
    dna = DNA()
    print(dna.get_flags())
