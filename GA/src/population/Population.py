from member.Member import Member
import constants


class Population:
    def __init__(self):
        self.members = list()
        for i in range(constants.POPULATION_SIZE):
            self.members.append(Member())


if __name__ == '__main__':
    population = Population()
    