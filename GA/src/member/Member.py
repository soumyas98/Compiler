from dna import DNA
from compile import Compile
import constants


class Member(DNA):
    def __init__(self):
        self.dna = dna.DNA()
        self.fitness_score = 0
        self.meta_data = {
            constants.META_DATA_EXEC_TIME: 0,
            constants.META_DATA_COMPILE_TIME: 0,
            constants.META_DATA_BIN_SIZE: 0
        }

    def calculate_fitness(self):
        pass
