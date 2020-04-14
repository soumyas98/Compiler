from member.Member import Member
from meta_data.PopulationMD import PopulationMD
from constants import CROSSOVER_RATE
from constants import MUTATION_RATE
from constants import ELITE_FACTOR
from math import ceil
import random


class Population:
    def __init__(self, n):
        self.size = n
        self.members = [Member() for _ in range(n)]
        self.meta_data = PopulationMD()

    def get_fittest(self):
        return self.meta_data.fittest_member

    def calculate_fitness(self):
        for member in self.members:
            member.calculate_fitness()

        self.meta_data.fittest_member = max(self.members,
                                            key=lambda mem: mem.get_fitness())
        self.meta_data.fitness_sum = sum(m.get_fitness()
                                         for m in self.members)
        self.meta_data.avg_fitness = self.meta_data.fitness_sum / self.size
        self.meta_data.crossover_count = 0
        self.meta_data.mutation_count = 0

    def get_data_dump(self):
        data = dict()
        data['members'] = list()
        for member in self.members:
            data['members'].append(member.get_data_dump())
        return data

    def selection(self):
        new_generation = self._get_elites()
        for i in range(len(self.members) - len(new_generation)):
            parent1 = self._select_one()
            parent2 = parent1
            tries = 0
            while parent1 == parent2 and tries < 1000:
                parent2 = self._select_one()
                tries += 1
            child = self._crossover(parent1, parent2)
            new_generation.append(child)
        self.members = new_generation

    def mutation(self):
        for member in self.members:
            if random.uniform(0, 1) < MUTATION_RATE:
                self.meta_data.mutation_count += 1
                member.mutate_DNA()

    def _crossover(self, parent1, parent2):
        parent1_DNA = parent1.get_DNA()
        parent2_DNA = parent2.get_DNA()
        if random.uniform(0, 1) < CROSSOVER_RATE:
            self.meta_data.crossover_count += 1
            mid = len(parent1_DNA) // 2
            new_DNA = parent1_DNA[:mid] + parent2_DNA[mid:]
            return Member(dna=new_DNA)
        if parent1.get_fitness() > parent2.get_fitness():
            return parent1
        return parent2

    def _get_elites(self):
        elite_len = ceil(len(self.members) * ELITE_FACTOR)
        return sorted(self.members,
                      key=lambda mem: mem.get_fitness(),
                      reverse=True)[:elite_len]

    def _select_one(self):
        selected = random.uniform(0, self.meta_data.fitness_sum)
        pre_sum = 0
        for member in self.members:
            pre_sum += member.get_fitness()
            if pre_sum > selected:
                return member


if __name__ == '__main__':
    from constants import SEED
    random.seed(SEED)
    SIZE = 10
    population = Population(SIZE)
    population.calculate_fitness()
