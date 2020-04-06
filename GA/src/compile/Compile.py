from constants import COMPILE_COMMAND_LIST
from constants import ITERATIONS
from constants import CLEAN_COMMAND_LIST
from constants import META_DATA_COMPILE_TIME
from constants import META_DATA_EXEC_TIME
from constants import PROGRAM_EXEC_PATH
import subprocess
import timeit
import uuid


class Compile:
    @staticmethod
    def run(flags):
        meta_data = dict()
        Compile._clean()
        exec_file = str(uuid.uuid4()).replace('-', '')
        meta_data[META_DATA_COMPILE_TIME] = Compile._compile(flags, exec_file)
        meta_data[META_DATA_EXEC_TIME] = Compile._execute(exec_file)

        return meta_data

    @staticmethod
    def _compile(flags, exec_file):
        cmd_list = COMPILE_COMMAND_LIST + \
                   ['CFLAGS={}'.format(flags)] + \
                   ['OUTPUT={}'.format(exec_file)]
        print('Compiling...')
        stmt = 'subprocess.run({}, stderr=subprocess.STDOUT,\
        stdout=subprocess.DEVNULL, check=True)'.format(cmd_list)

        return timeit.timeit(stmt=stmt, setup='import subprocess', number=1)

    @staticmethod
    def _execute(exec_file):
        exec_file_path = PROGRAM_EXEC_PATH + exec_file + '.exe'
        print('Executing {}'.format(exec_file_path))
        stmt = 'subprocess.run({}, stderr=subprocess.STDOUT,\
        stdout=subprocess.DEVNULL, check=True)'.format([exec_file_path])

        return timeit.timeit(stmt=stmt, setup='import subprocess',
                             number=ITERATIONS) / ITERATIONS

    @staticmethod
    def _clean():
        print('Cleaning up...\n{}'.format(' '.join(CLEAN_COMMAND_LIST)))
        subprocess.run(CLEAN_COMMAND_LIST, stdout=subprocess.DEVNULL,
                       stderr=subprocess.STDOUT)


if __name__ == '__main__':
    meta_data = Compile.run('-fno-inline-functions -fearly-inlining -ffunction-cse')
    print(meta_data)
