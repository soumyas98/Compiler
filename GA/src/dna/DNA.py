from constants import FLAGS
from random import randint


class DNA:
    def __init__(self, dna=None):
        if dna is None:
            self.data = self._get_random_bin_str()
        else:
            self.data = dna

    def get_DNA(self):
        return self.data

    def set_DNA(self, data):
        self.data = data

    def _get_random_bin_str(self):
        return ''.join([str(randint(0, 1)) for _ in range(len(FLAGS))])

    def get_flags(self):
        flags = list()
        for i in range(len(self.data)):
            if self.data[i] == '1':
                flags.append('-f' + FLAGS[i])
            else:
                flags.append('-fno-' + FLAGS[i])
        return ' '.join(flags)

    def __repr__(self):
        return 'DNA: {}\nFlags:\n{}'.format(self.data, self.get_flags())


if __name__ == '__main__':
    import random
    from constants import SEED
    random.seed(SEED)
    dna = DNA()
    print(dna)
    dna = DNA('123')
    print(dna)
