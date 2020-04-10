class PopulationMD:
    def __init__(self):
        self.avg_fitness = None
        self.fitness_sum = None
        self.fittest_member = None
        self.mutation_count = None
        self.crossover_count = None

    def get_dict(self):
        d = dict()
        d['avg-fit'] = self.avg_fitness
        d['fittest'] = self.fittest_member.get_data_dump()
        d['mutation-count'] = self.mutation_count
        d['crossover-count'] = self.crossover_count
        return d

    def __repr__(self):
        return 'Avg: {}, Sum: {}, Fittest: {}, MC: {}, CC: {}'.format(
            self.avg_fitness, self.fitness_sum,
            self.fittest_member.get_fitness(),
            self.mutation_count, self.crossover_count
        )
