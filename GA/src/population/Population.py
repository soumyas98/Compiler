from member.Member import Member


class Population:
    def __init__(self, n):
        self.members = list()
        for i in range(n):
            self.members.append(Member())

    def calculate_fitness(self):
        pass

    def selection(self):
        pass

    def crossover(self):
        pass

    def mutation(self):
        pass


if __name__ == '__main__':
    population = Population()
