from member.Member import Member
import constants
import random


class Population:
    def __init__(self, n):
        self.members = list()
        for i in range(n):
            self.members.append(Member())

    def calculate_fitness(self):
        for member in self.members:
            member.calculate_fitness()

    def selection(self):
        fitness_sum = sum(m.get_fitness() for m in self.members)
        return self._select_one(fitness_sum)

    def crossover(self):
        pass

    def mutation(self):
        count = 0
        for member in self.members:
            if random.uniform(0, 1) < constants.MUTATION_RATE:
                mutated_DNA = self._mutate_DNA(member)
                if mutated_DNA != member.get_DNA():
                    count += 1
                member.set_DNA(mutated_DNA)
        print(count)

    def _select_one(self, fitness_sum):
        selected = random.uniform(0, fitness_sum)
        current = 0
        for i, member in enumerate(self.members):
            current += member.get_fitness()
            if current > selected:
                return i

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
    SIZE = 100
    population = Population(SIZE)
    population.mutation()
    check_selection(SIZE)
    