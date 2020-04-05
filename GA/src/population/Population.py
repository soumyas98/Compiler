from member.Member import Member
import constants


class Population:
    def __init__(self):
        self.member = []
        for i in range(constants.POPULATION_SIZE):
            self.member.append(Member())


if __name__ == '__main__':
    population = Population()
    