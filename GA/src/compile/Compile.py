from constants import COMPILE_COMMAND_LIST, CLEAN_COMMAND_LIST
from constants import META_DATA_COMPILE_TIME, META_DATA_EXEC_TIME
from constants import META_DATA_BIN_NAME
from constants import ITERATIONS
from constants import PROGRAM_EXEC_PATH
from constants import O1_TARGET, O1_COMMAND_LIST
from constants import O2_TARGET, O2_COMMAND_LIST
from constants import O3_TARGET, O3_COMMAND_LIST
from constants import NO_OP_TARGET, NO_OP_COMMAND_LIST
import subprocess
import timeit
import uuid


class Compile:
    @staticmethod
    def run(flags):
        meta_data = dict()
        Compile._clean()
        exec_file = str(uuid.uuid4()).replace('-', '')
        meta_data[META_DATA_BIN_NAME] = exec_file
        meta_data[META_DATA_COMPILE_TIME] = Compile._compile(flags, exec_file)
        meta_data[META_DATA_EXEC_TIME] = Compile._execute(exec_file)

        return meta_data
    
    @staticmethod
    def run_benchmarks():
        benchmark = dict()
        Compile._clean()

        benchmark[O1_TARGET] = Compile._get_benchmark_meta_data(O1_TARGET, O1_COMMAND_LIST)
        benchmark[O2_TARGET] = Compile._get_benchmark_meta_data(O2_TARGET, O2_COMMAND_LIST)
        benchmark[O3_TARGET] = Compile._get_benchmark_meta_data(O3_TARGET, O3_COMMAND_LIST)
        benchmark[NO_OP_TARGET] = Compile._get_benchmark_meta_data(NO_OP_TARGET, NO_OP_COMMAND_LIST)
        return benchmark

    @staticmethod
    def _get_benchmark_meta_data(target, cmd_list):
        exec_file = target
        meta_data = dict()
        meta_data[META_DATA_COMPILE_TIME] = Compile._subproccess(cmd_list)
        meta_data[META_DATA_EXEC_TIME] = Compile._execute(exec_file)
        return meta_data


    @staticmethod
    def _subproccess(cmd_list, iterations=1):
        stmt = 'subprocess.run({}, stderr=subprocess.STDOUT,\
        stdout=subprocess.DEVNULL, check=True)'.format(cmd_list)
        return timeit.timeit(stmt=stmt,
                             setup='import subprocess',
                             number=iterations) / iterations

    @staticmethod
    def _compile(flags, exec_file):
        cmd_list = COMPILE_COMMAND_LIST + \
                   ['CFLAGS={}'.format(flags)] + \
                   ['OUTPUT={}'.format(exec_file)]
        print('Compiling...')
        return Compile._subproccess(cmd_list)

    @staticmethod
    def _execute(exec_file):
        exec_file_path = PROGRAM_EXEC_PATH + exec_file + '.exe'
        print('Executing {}'.format(exec_file_path))
        return Compile._subproccess([exec_file_path], iterations=ITERATIONS)

    @staticmethod
    def _clean():
        print('Cleaning up...\n{}'.format(' '.join(CLEAN_COMMAND_LIST)))
        subprocess.run(CLEAN_COMMAND_LIST, stdout=subprocess.DEVNULL,
                       stderr=subprocess.STDOUT)


if __name__ == '__main__':
    # meta_data = Compile.run('-fno-inline-functions -fearly-inlining -ffunction-cse')
    print(Compile.run_benchmarks())
