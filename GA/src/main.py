from constants import SEED, POPULATION_SIZE, GENERATIONS
from population.Population import Population
import random


def main():
    random.seed(SEED)

    population = Population(POPULATION_SIZE)

    for generation in range(GENERATIONS):
        population.calculate_fitness()
        fittest = population.get_fittest()
        print('The fittest in', generation, 'is\n', fittest)
        population.selection()
        population.mutation()


if __name__ == '__main__':
    main()
