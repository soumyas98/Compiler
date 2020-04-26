from os import listdir
from os.path import isfile, join
import json

mapping = [
    "Number of basic blocks in the method",
    "Number of basic blocks with a single successor",
    "Number of basic blocks with two successors",
    "Number of basic blocks with more then two successors",
    "Number of basic blocks with a single predecessor",
    "Number of basic blocks with two predecessors",
    "Number of basic blocks with more then two predecessors",
    "Number of basic blocks with a single predecessor and a single successor",
    "Number of basic blocks with a single predecessor and two successors",
    "Number of basic blocks with a two predecessors and one successor",
    "Number of basic blocks with two successors and two predecessors",
    "Number of basic blocks with more then two successors and more then two predecessors",
    "Number of basic blocks with number of instructions less then 15",
    "Number of basic blocks with number of instructions in the interval [15, 500]",
    "Number of basic blocks with number of instructions greater then 500",
    "Number of edges in the control flow graph",
    "Number of critical edges in the control flow graph",
    "Number of abnormal edges in the control flow graph",
    "Number of direct calls in the method",
    "Number of conditional branches in the method",
    "Number of assignment instructions in the method",
    "Number of binary integer operations in the method",
    "Number of binary floating point operations in the method",
    "Number of instructions in the method",
    "Average of number of instructions in basic blocks",
    "Average of number of phi-nodes at the beginning of a basic block",
    "Average of arguments for a phi-node",
    "Number of basic blocks with no phi nodes",
    "Number of basic blocks with phi nodes in the interval [0, 3]",
    "Number of basic blocks with more then 3 phi nodes",
    "Number of basic block where total number of arguments for all phi-nodes is in greater then 5",
    "Number of basic block where total number of arguments for all phi-nodes is in the interval [1, 5]",
    "Number of switch instructions in the method",
    "Number of unary operations in the method",
    "Number of instruction that do pointer arithmetic in the method",
    "Number of indirect references via pointers ('*' in C)",
    "Number of times the address of a variables is taken ('\&' in C)",
    "Number of times the address of a function is taken ('\&' in C)",
    "Number of indirect calls (i.e. done via pointers) in the method",
    "Number of assignment instructions with the left operand an integer constant in the method",
    "Number of binary operations with one of the operands an integer constant in the method",
    "Number of calls with pointers as arguments",
    "Number of calls with the number of arguments is greater then 4",
    "Number of calls that return a pointer",
    "Number of calls that return an integer",
    "Number of occurrences of integer constant zero",
    "Number of occurrences of 32-bit integer constants",
    "Number of occurrences of integer constant one",
    "Number of occurrences of 64-bit integer constants",
    "Number of references of a local variables in the method",
    "Number of references (def/use) of static/extern variables in the method",
    "Number of local variables referred in the method",
    "Number of static/extern variables referred in the method",
    "Number of local variables that are pointers in the method",
    "Number of static/extern variables that are pointers in the method",
    "Number of unconditional branches in the method",
    "CYCLOMATIC COMPLEXITY",
    "HALSTEAD's METRICS",
    "Hn2 is number of distinct operands (Halstead n2)",
    "N is num var defs (should be == Halstead n2 or Halstead N2?)",
    "HN1 is total number of operators (Halstead N1) (approx due to abstraction)",
    "Hn1 is number of distinct operators (Halstead n1) (approx due to abstraction)",
    "Approx of Halstead difficulty D == Hn1/2 * (HN2 / Hn2)",
    "Approx of Halstead volume volume == HN *log_2(Hn)",
    "Approx of Halstead effort, which == Difficulty * Volume"
]
FEAT_PATH = 'GA/programs/susan/features'
data = dict()
data['functions'] = list()
for f in [f for f in listdir(FEAT_PATH)
          if isfile(join(FEAT_PATH, f))]:
    with open(join(FEAT_PATH, f), 'r') as fp:
        x = fp.read()
        feats = x.split(',')
        vals = list()
        for i, feat in enumerate(feats):
            feat = feat.strip()
            vals.append({
                'label': mapping[i],
                'value': feat[feat.find('=') + 1:]
            })
        name = f.split('.')[-3]
        val = dict()
        val['name'] = name
        val['features'] = vals
        data['functions'].append(val)
        with open('ui/src/assets/data/4/feature.json', 'w') as fp2:
            json.dump(data, fp2)
