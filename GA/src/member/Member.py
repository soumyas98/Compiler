from compile.Compile import Compile
from dna.DNA import DNA
from constants import META_DATA_EXEC_TIME


class Member(DNA):
    def __init__(self, dna=None):
        DNA.__init__(self, dna=dna)
        self.fitness_score = 0.1
        self.meta_data = dict()

    def calculate_fitness(self):
        self.meta_data = Compile.run(self.get_flags())
        self.fitness_score = self.meta_data[META_DATA_EXEC_TIME]
        print(self.meta_data)

    def get_fitness(self):
        return 1 / self.fitness_score

    def get_DNA(self):
        return self.data

    def set_DNA(self, data):
        self.data = data

    def __repr__(self):
        return 'DNA: {}\nFitness: {}\nMeta Data: {}\nFlags:{}'.format(
            self.data, self.get_fitness(), self.meta_data, self.get_flags())


if __name__ == '__main__':
    member = Member()
    member.calculate_fitness()
    print(member)
