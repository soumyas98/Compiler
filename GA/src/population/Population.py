from member.Member import Member
from constants import POPULATION_SIZE


class Population:
    def __init__(self):
        self.members = list()
        for i in range(POPULATION_SIZE):
            self.members.append(Member())


if __name__ == '__main__':
    population = Population()
    