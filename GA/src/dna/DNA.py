from constants import FLAGS, SEED
import random


class DNA:
    def __init__(self):
        self.data = self._get_random_bin_str()

    def _get_random_bin_str(self):
        temp = []
        for i in range(len(FLAGS)):
            x = random.randint(0, 1)
            temp.append(str(x))
        return ''.join(temp)

    def get_flags(self):
        flags = list()
        for i in range(len(self.data) - 1):
            if self.data[i] == '1':
                flags.append('-f' + FLAGS[i])
            else:
                flags.append('-fno-' + FLAGS[i])
        return ' '.join(flags)


    def __repr__(self):
        return 'data: {}\nflags:\n{}'.format(self.data, self.get_flags())


if __name__ == '__main__':
    random.seed(SEED)
    dna = DNA()
    print(dna)
