from constants import COMPILE_COMMAND_LIST, CLEAN_COMMAND_LIST
from constants import ITERATIONS
from constants import PROGRAM_EXEC_PATH
from constants import O1_TARGET, O1_COMMAND_LIST
from constants import O2_TARGET, O2_COMMAND_LIST
from constants import O3_TARGET, O3_COMMAND_LIST
from constants import NO_OP_TARGET, NO_OP_COMMAND_LIST
from meta_data.MemberMD import MemberMD
import subprocess
import timeit
import uuid


class Compile:
    @staticmethod
    def run(flags):
        Compile._clean()

        exec_file = str(uuid.uuid4()).replace('-', '')
        cmp_time = Compile._compile(flags, exec_file)
        exec_time = Compile._execute(exec_file)

        meta_data = MemberMD(exec_time, cmp_time, exec_file)
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
    def _get_benchmark_meta_data(exec_file, cmd_list):
        cmp_time = Compile._subproccess(cmd_list)
        exec_time = Compile._execute(exec_file)
        return MemberMD(exec_time, cmp_time, exec_file)

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
    meta_data = Compile.run('-fno-inline-functions -fearly-inlining -ffunction-cse')
    bm_md = Compile.run_benchmarks()
    print(meta_data)
    print(bm_md)
