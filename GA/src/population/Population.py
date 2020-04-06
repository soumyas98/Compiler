from member.Member import Member
import constants
import random


class Population:
    def __init__(self, n):
        self.members = list()
        for i in range(n):
            self.members.append(Member())

    def calculate_fitness(self):
        pass

    def selection(self):
        fitness_sum = sum(m.get_fitness() for m in self.members)
        return self.select_one(fitness_sum)
        

    def crossover(self):
        pass

    def mutation(self):
        count = 0
        for member in self.members:
            if random.uniform(0, 1) < constants.MUTATION_RATE:
                mutated_DNA = self.mutate_DNA(member)
                if member.get_DNA() != mutated_DNA:
                    count += 1
                member.set_DNA(mutated_DNA)
        print(count)

    def select_one(self, fitness_sum):
        selected = random.uniform(0, fitness_sum)
        current = 0
        for i, member in enumerate(self.members):
            current += member.get_fitness()
            if current > selected:
                return i
    
    def mutate_DNA(self, member):
        dna = member.get_DNA().split()
        mutate_point = random.randint(0, len(dna) - 1)
        if dna[mutate_point] == '0':
            dna[mutate_point] = '1'
        else:
            dna[mutate_point] = '0'
        return ''.join(dna)


def check_selection():
    lst = [0] * 10
    for i in range(0, 10000):
        i = population.selection()
        lst[i] += 1
    for i in range(1, 10):
        print(lst[i], population.members[i].fitness_score)


if __name__ == '__main__':
    population = Population(10)
    population.mutation()

    
    