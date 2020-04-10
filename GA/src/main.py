from constants import SEED, POPULATION_SIZE, GENERATIONS, JSON_FILE
from constants import O1_TARGET, O2_TARGET, O3_TARGET, NO_OP_TARGET
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
    data['generations'] = list()
    for generation in range(GENERATIONS):
        print('#' * bdr_len, 'Generation', generation, '#' * bdr_len)

        print('----------> Fitness Calculation')
        population.calculate_fitness()
        data['generations'].append(population.get_data_dump())

        fittest = population.get_fittest()
        print('\nThe fittest member of this generation is\n{}'.format(fittest))
        fittest_members.append(copy.deepcopy(fittest))

        print('\n----------> Selecting population for next generation')
        population.selection()

        print('\n----------> Mutating population')
        population.mutation()
        print()

    print('#' * bdr_len, 'Final Generation', '#' * bdr_len)
    population.calculate_fitness()
    data['generations'].append(population.get_data_dump())
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
    bm_dict[O1_TARGET] = benchmarks[O1_TARGET].get_dict()
    bm_dict[O2_TARGET] = benchmarks[O2_TARGET].get_dict()
    bm_dict[O3_TARGET] = benchmarks[O3_TARGET].get_dict()
    bm_dict[NO_OP_TARGET] = benchmarks[NO_OP_TARGET].get_dict()
    data.update(bm_dict)

    print('#' * bdr_len, 'Benchmarks', '#' * bdr_len)
    print('----------> O1 Optimization')
    pretty_print(benchmarks[O1_TARGET])
    print('----------> O2 Optimization')
    pretty_print(benchmarks[O2_TARGET])
    print('----------> O3 Optimization')
    pretty_print(benchmarks[O3_TARGET])
    print('----------> No Optimization')
    pretty_print(benchmarks[NO_OP_TARGET])
    print('----------> GA found Optimization')
    pretty_print(fittest_members[-1].get_meta_data())

    with open(JSON_FILE, 'w') as fp:
        json.dump(data, fp, indent=2)
    print('\nData written to {} file'.format(JSON_FILE))


if __name__ == '__main__':
    main()
