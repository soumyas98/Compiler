from compile.Compile import Compile
from dna.DNA import DNA
import random


class Member(DNA):
    def __init__(self, dna=None):
        DNA.__init__(self, dna=dna)
        self.meta_data = None
        self.fitness_score = random.uniform(0, 10)  # randomness for testing

    def calculate_fitness(self):
        md = Compile.run(self.get_flags())
        if self.meta_data is None:
            self.meta_data = md
        elif md.exec_time < self.meta_data.exec_time:
            self.meta_data = md
        self.meta_data.exec_file = md.exec_file

        self.fitness_score = 1 / self.meta_data.exec_time

    def mutate_DNA(self):
        dna = list(self.data)
        mutate_pnt = random.randint(0, len(dna) - 1)
        dna[mutate_pnt] = '0' if dna[mutate_pnt] == '1' else '1'
        self.set_DNA(''.join(dna))

    def get_meta_data(self):
        return self.meta_data

    def get_fitness(self):
        return self.fitness_score

    def get_data_dump(self):
        return self.meta_data.get_dict()

    def __repr__(self):
        return 'DNA: {}\nFitness: {}\nMeta Data: {}\nFlags:{}'.format(
            self.data, self.get_fitness(), self.meta_data, self.get_flags())


if __name__ == '__main__':
    mem = Member()
    mem.calculate_fitness() 
    mem.calculate_fitness()
