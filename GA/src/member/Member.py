from compile.Compile import Compile
from dna.DNA import DNA
from constants import META_DATA_EXEC_TIME


class Member(DNA):
    def __init__(self, dna=None):
        DNA.__init__(self, dna=dna)
        self.meta_data = dict()

    def calculate_fitness(self):
        print('DNA', self.get_DNA())
        new_meta_data = Compile.run(self.get_flags())
        if META_DATA_EXEC_TIME not in self.meta_data:
            self.fitness_score = 1 / new_meta_data[META_DATA_EXEC_TIME]
        elif new_meta_data[META_DATA_EXEC_TIME] < \
                self.meta_data[META_DATA_EXEC_TIME]:
            self.fitness_score = 1 / new_meta_data[META_DATA_EXEC_TIME]
        print(self.fitness_score, self.meta_data)
        print()

    def get_fitness(self):
        return self.fitness_score

    def get_DNA(self):
        return self.data

    def set_DNA(self, data):
        self.data = data

    def get_meta_data(self):
        return self.meta_data

    def __repr__(self):
        return 'DNA: {}\nFitness: {}\nMeta Data: {}\nFlags:{}'.format(
            self.data, self.get_fitness(), self.meta_data, self.get_flags())


if __name__ == '__main__':
    member = Member()
    member.calculate_fitness()
    print(member)
