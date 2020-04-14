from constants import SEED, POPULATION_SIZE, GENERATIONS, JSON_FILE
from constants import O1, O2, O3, O0
from constants import CROSSOVER_RATE, MUTATION_RATE, ELITE_FACTOR
from population.Population import Population
from compile.Compile import Compile
import random
import copy
import json


def pretty_print(meta_data):
    print('Execution time', meta_data.exec_time, 's')
    print('Compile time', meta_data.compile_time, 's')
    print()


def main():
    random.seed(SEED)

    population = Population(POPULATION_SIZE)
    fittest_members = list()

    bdr_len = 20
    data = dict()
    data['generation-count'] = GENERATIONS
    data['population'] = POPULATION_SIZE
    data['crossover-rate'] = CROSSOVER_RATE
    data['mutation-rate'] = MUTATION_RATE
    data['elite-factor'] = ELITE_FACTOR

    data['generations'] = list()
    for generation in range(GENERATIONS):
        print('#' * bdr_len, 'Generation', generation, '#' * bdr_len)
        gen_data = dict()
        print('----------> Fitness Calculation')
        population.calculate_fitness()
        gen_data = population.get_data_dump()

        fittest = population.get_fittest()
        print('\nThe fittest member of this generation is\n{}'.format(fittest))
        fittest_members.append(copy.deepcopy(fittest))

        print('\n----------> Selecting population for next generation')
        population.selection()

        print('\n----------> Mutating population')
        population.mutation()
        gen_data.update(population.meta_data.get_dict())
        data['generations'].append(gen_data)
        print()

    print('#' * bdr_len, 'Final Generation', '#' * bdr_len)

    population.calculate_fitness()

    gen_data = population.get_data_dump()
    gen_data.update(population.meta_data.get_dict())
    data['generations'].append(gen_data)

    fittest = population.get_fittest()
    fittest_members.append(copy.deepcopy(fittest))

    print('#' * bdr_len, 'Search completed', '#' * bdr_len)
    print()

    for i, member in enumerate(fittest_members):
        print('#' * bdr_len, 'Generation', i, '#' * bdr_len)
        print('Data', member.get_meta_data(), '\n')
        print('Flags', member.get_flags())
        print()

    benchmarks = Compile.run_benchmarks()
    bm_dict = dict()
    bm_dict[O1] = benchmarks[O1].get_dict()
    bm_dict[O2] = benchmarks[O2].get_dict()
    bm_dict[O3] = benchmarks[O3].get_dict()
    bm_dict[O0] = benchmarks[O0].get_dict()
    data['benchmark'] = bm_dict

    print('#' * bdr_len, 'Benchmarks', '#' * bdr_len)
    print('----------> O1 Optimization')
    pretty_print(benchmarks[O1])
    print('----------> O2 Optimization')
    pretty_print(benchmarks[O2])
    print('----------> O3 Optimization')
    pretty_print(benchmarks[O3])
    print('----------> No Optimization')
    pretty_print(benchmarks[O0])
    print('----------> GA found Optimization')
    pretty_print(fittest_members[-1].get_meta_data())

    with open(JSON_FILE, 'w') as fp:
        json.dump(data, fp, indent=2)
    print('\nData written to {} file'.format(JSON_FILE))


if __name__ == '__main__':
    main()
