# GA Factors
GENERATIONS = 50
POPULATION_SIZE = 10
CROSSOVER_RATE = 0.6
MUTATION_RATE = 0.01

# Flags
FLAGS = [
    "early-inlining", "function-cse", "keep-static-consts",
    "peephole", "split-ivn-in-unroller", "tree-vect-loop-version",
    "cprop-registers", "defer-pop", "guess-branch-probability",
    "if-conversion", "if-conversion2", "ipa-pure-const",
    "ipa-reference", "loop-optimize", "merge-constants",
    "tree-ccp", "tree-ch", "tree-copy-prop", "tree-copyrename",
    "tree-dce", "tree-dominator-opts", "tree-dse", "tree-fre",
    "tree-lrs", "tree-salias", "tree-sink", "tree-sra",
    "tree-ter", "unit-at-a-time", "align-functions=0",
    "align-jumps=0", "align-labels=0", "align-loops=0",
    "caller-saves", "crossjumping", "cse-follow-jumps",
    "cse-skip-blocks", "delete-null-pointer-checks", "expensive-optimizations",
    "gcse", "ipa-type-escape", "optimize-sibling-calls", "peephole2",
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
TARGET = 'basicmath_large'
BASE_COMMAND_LIST = ['make',  '-C', PROGRAM_PATH]
COMPILE_COMMAND_LIST = BASE_COMMAND_LIST + [TARGET] 
CLEAN_COMMAND_LIST = BASE_COMMAND_LIST + ['clean']
EXECUTABLE_FILE = PROGRAM_PATH + '/' + TARGET + '.exe'
ITERATIONS = 4
