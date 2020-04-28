from path import PROGRAM_PATH
import time

SEED = time.time()

# GA Factors
GENERATIONS = 1
POPULATION_SIZE = 1
CROSSOVER_RATE = 0.6
MUTATION_RATE = 0.01
ELITE_FACTOR = 0.1

# Flags
FLAGS = [
    "early-inlining", "function-cse", "keep-static-consts",
    "peephole", "split-ivs-in-unroller", "tree-vect-loop-version",
    "cprop-registers", "defer-pop", "guess-branch-probability",
    "if-conversion", "if-conversion2", "ipa-pure-const",
    "ipa-reference", "loop-optimize", "merge-constants",
    "tree-ccp", "tree-ch", "tree-copy-prop", "tree-copyrename",
    "tree-dce", "tree-dominator-opts", "tree-dse", "tree-fre",
    "tree-lrs", "tree-salias", "tree-sink", "tree-sra",
    "tree-ter", "unit-at-a-time", "align-functions",
    "align-jumps", "align-labels", "align-loops",
    "caller-saves", "crossjumping", "cse-follow-jumps",
    "cse-skip-blocks", "delete-null-pointer-checks", "expensive-optimizations",
    "gcse", "optimize-sibling-calls", "peephole2",
    "regmove", "reorder-blocks", "reorder-functions",
    "rerun-cse-after-loop", "rerun-loop-opt", "schedule-insns2",
    "strength-reduce", "strict-aliasing", "thread-jumps", "tree-pre",
    "tree-store-ccp", "tree-store-copy-prop", "tree-vrp", "gcse-after-reload",
    "gcse-after-reload", "unswitch-loops",
    "reorder-blocks-and-partition"
]

# Named Constants
O1 = "O1"
O2 = "O2"
O3 = "O3"
O0 = "O0"
GAOPT = "GAOPT"

# Compilation commands

# Basic Math
"""
DIR_PATH = PROGRAM_PATH + 'basicmath'
TARGET = 'basicmath_small'
O1_TARGET = 'basicmath_O1_small'
O2_TARGET = 'basicmath_O2_small'
O3_TARGET = 'basicmath_O3_small'
NO_OP_TARGET = 'basicmath_NO_OP_small'
NAME = 'small'
EXEC_PARAMS = ''
"""

# Bit Count
"""
DIR_PATH = PROGRAM_PATH + 'bitcount'
TARGET = 'bitcnts'
O1_TARGET = 'bitcnts_O1'
O2_TARGET = 'bitcnts_O2'
O3_TARGET = 'bitcnts_O3'
NO_OP_TARGET = 'bitcnts_O0'
NAME = 'small'
EXEC_PARAMS = '75000'  # '1125000'
"""

# Quick Sort
"""
DIR_PATH = PROGRAM_PATH + 'qsort'
TARGET = 'qsort_large'
O1_TARGET = 'qsort_large_O1'
O2_TARGET = 'qsort_large_O2'
O3_TARGET = 'qsort_large_O3'
NO_OP_TARGET = 'qsort_large_O0'
NAME = 'large'
EXEC_PARAMS = DIR_PATH + '/input_large.dat'  # DIR_PATH + '/input_large.dat'
"""

# Susan
DIR_PATH = PROGRAM_PATH + 'susan'
TARGET = 'susan'
O1_TARGET = 'susan_O1'
O2_TARGET = 'susan_O2'
O3_TARGET = 'susan_O3'
NO_OP_TARGET = 'susan_O0'
NAME = 'small'
EXEC_PARAMS = DIR_PATH + '/input_small.pgm output.susan.smoothing -s'  # DIR_PATH + '/input_large.pgm'

###### COMPILATION COMMANDS #########
BASE_COMMAND_LIST = ['make',  '-C', DIR_PATH]
COMPILE_COMMAND_LIST = BASE_COMMAND_LIST + [TARGET]
O1_COMMAND_LIST = BASE_COMMAND_LIST + [O1_TARGET]
O2_COMMAND_LIST = BASE_COMMAND_LIST + [O2_TARGET]
O3_COMMAND_LIST = BASE_COMMAND_LIST + [O3_TARGET]
NO_OP_COMMAND_LIST = BASE_COMMAND_LIST + [NO_OP_TARGET]
CLEAN_COMMAND_LIST = BASE_COMMAND_LIST + ['clean']
PROGRAM_EXEC_PATH = DIR_PATH + '/output/'
ITERATIONS = 4
JSON_FILE = 'data/{}-{}.json'.format(TARGET, NAME)
