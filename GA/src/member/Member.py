from compile.Compile import Compile
from dna.DNA import DNA
from constants import META_DATA_EXEC_TIME


class Member(DNA):
    def __init__(self):
        DNA.__init__(self)
        self.fitness_score = 0
        self.meta_data = dict()

    def calculate_fitness(self):
        self.meta_data = Compile.run(self.get_flags())
        self.fitness_score = self.meta_data[META_DATA_EXEC_TIME]

    def get_fitness(self):
        return self.fitness_score

    def __repr__(self):
        return 'DNA: {}\nFitness: {}\nMeta Data: {}'.format(self.data,
                                                            self.fitness_score,
                                                            self.meta_data)


if __name__ == '__main__':
    member = Member()
    member.calculate_fitness()
    print(member)
