from constants import FLAGS, SEED
import random


class DNA:
    def __init__(self):
        self.data = self._get_random_bin_str()

    def _get_random_bin_str(self):
        return ''.join([str(random.randint(0, 1)) for _ in range(len(FLAGS))])

    def get_flags(self):
        flags = list()
        for i, x in enumerate(self.data):
            flags.append('{}{}'.format('-f' if x == '1' else '-fno-',
                                       FLAGS[i]))
        return ' '.join(flags)

    def __repr__(self):
        return 'data: {}\nflags:\n{}'.format(self.data, self.get_flags())


if __name__ == '__main__':
    random.seed(SEED)
    dna = DNA()
    print(dna)
