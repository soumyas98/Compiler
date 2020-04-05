import constants


class DNA:
    def __init__(self):
        self.data = '10010010010010010010010010010010010010010010010010010010'

    def get_flags(self):
        flags = list()
        for x in self.data:
            if self.data[56] == '0':
                flags.append('-f' + constants.FLAGS[56])
            if self.data[56] == '1':
                flags.append('-fno' + constants.FLAGS[56])
            elif x == '1':
                flags.append('-f' + constants.FLAGS[x])
            else:
                flags.append('-fno' + constants.FLAGS[x])
        return ' '.join(flags)


if __name__ == '__main__':
    dna = DNA()
    print(dna.get_flags())
