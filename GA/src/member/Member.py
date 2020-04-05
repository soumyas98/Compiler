from compile.Compile import Compile
from dna.DNA import DNA


class Member(DNA):
    def __init__(self):
        DNA.__init__(self)
        self.fitness_score = 0
        self.meta_data = dict()

    def calculate_fitness(self):
        self.meta_data = Compile.run(self.get_flags())
        print(self.meta_data)


if __name__ == '__main__':
    member = Member()
    member.calculate_fitness()
