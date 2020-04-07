SEED = 0

# GA Factors
GENERATIONS = 10
POPULATION_SIZE = 10
CROSSOVER_RATE = 0.6
MUTATION_RATE = 0.01
ELITE_FACTOR = 0.3

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

# Meta Data names
META_DATA_EXEC_TIME = 'execution-time'
META_DATA_COMPILE_TIME = 'compile-time'
META_DATA_BIN_SIZE = 'bin-size'

# Compilation commands
PROGRAM_PATH = 'C:/Users/I533128/learning/Compiler/GA/programs/basicmath'
TARGET = 'basicmath_small'
BASE_COMMAND_LIST = ['make',  '-C', PROGRAM_PATH]
COMPILE_COMMAND_LIST = BASE_COMMAND_LIST + [TARGET] 
CLEAN_COMMAND_LIST = BASE_COMMAND_LIST + ['clean']
PROGRAM_EXEC_PATH = PROGRAM_PATH + '/output/'
ITERATIONS = 4
