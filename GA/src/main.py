from constants import SEED, POPULATION_SIZE, GENERATIONS
from population.Population import Population
import random
import copy


def main():
    random.seed(SEED)

    population = Population(POPULATION_SIZE)
    fittest_members = list()

    bdr_len = 20
    for generation in range(GENERATIONS):
        print('#' * bdr_len, 'Generation', generation, '#' * bdr_len)

        print('----------> Fitness Calculation')
        population.calculate_fitness()

        fittest = population.get_fittest()
        print('\nThe fittest member of this generation is\n{}'.format(fittest))
        fittest_members.append(copy.deepcopy(fittest))

        print('\n----------> Selecting population for next generation')
        population.selection()

        print('\n----------> Mutating population')
        population.mutation()
        print()

    print('#' * bdr_len, 'Search completed', '#' * bdr_len)
    print()

    for i, member in enumerate(fittest_members):
        print('#' * bdr_len, 'Generation', i, '#' * bdr_len)
        print('Data', member.get_meta_data(), '\n')
        print('Flags', member.get_flags())
        print()


if __name__ == '__main__':
    main()
