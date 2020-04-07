from member.Member import Member
from constants import CROSSOVER_RATE
from constants import MUTATION_RATE
from constants import ELITE_FACTOR
import random
import copy

class Population:
    def __init__(self, n):
        self.members = list()
        for i in range(n):
            self.members.append(Member())

    def get_fittest(self):
        return max(self.members, key=lambda mem: mem.get_fitness())

    def calculate_fitness(self):
        for member in self.members:
            member.calculate_fitness()

    def selection(self):
        new_generation = self._get_elites()
        fitness_sum = sum(m.get_fitness() for m in self.members)
        for i in range(len(self.members) - len(new_generation)):
            parent1 = self._select_one(fitness_sum)
            parent2 = parent1
            tries = 0
            while parent1 == parent2 and tries < 1000:
                parent2 = self._select_one(fitness_sum)
                tries += 1
            child = self.crossover(parent1, parent2)
            new_generation.append(child)
        self.members = new_generation

    def crossover(self, parent1, parent2):
        parent1_DNA = parent1.get_DNA()
        parent2_DNA = parent2.get_DNA()
        if random.uniform(0, 1) < CROSSOVER_RATE:
            mid = len(parent1_DNA) // 2
            new_DNA = parent1_DNA[:mid] + parent2_DNA[mid:]
            return Member(dna=new_DNA)
        if parent1.get_fitness() > parent2.get_fitness():
            return parent1
        return parent2

    def mutation(self):
        for member in self.members:
            if random.uniform(0, 1) < MUTATION_RATE:
                mutated_DNA = self._mutate_DNA(member)
                member.set_DNA(mutated_DNA)

    def _get_elites(self):
        elite_len = int(len(self.members) * ELITE_FACTOR)
        return copy.deepcopy(sorted(self.members,
                      key=lambda mem: mem.get_fitness(),
                      reverse=True)[:elite_len])

    def _select_one(self, fitness_sum):
        selected = random.uniform(0, fitness_sum)
        current = 0
        for i, member in enumerate(self.members):
            current += member.get_fitness()
            if current > selected:
                return member

    def _mutate_DNA(self, member):
        dna = member.get_DNA().split()
        mutate_pnt = random.randint(0, len(dna) - 1)
        dna[mutate_pnt] = '0' if dna[mutate_pnt] == '1' else '0'
        return ''.join(dna)


def check_selection(SIZE):
    lst = [0] * SIZE
    for i in range(0, 10000):
        i = population.selection()
        lst[i] += 1
    for i in range(1, SIZE):
        print(lst[i], population.members[i].fitness_score)


if __name__ == '__main__':
    SIZE = 10
    population = Population(SIZE)
    # population.mutation()
    # check_selection(SIZE)
    