from constants import COMPILE_COMMAND_LIST
from constants import EXECUTABLE_FILE
from constants import ITERATIONS
from constants import CLEAN_COMMAND_LIST
from constants import META_DATA_COMPILE_TIME
from constants import META_DATA_EXEC_TIME
import subprocess
import timeit


class Compile:
    @staticmethod
    def run(flags):
        meta_data = dict()
        Compile._clean()
        meta_data[META_DATA_COMPILE_TIME] = Compile._compile(flags)
        meta_data[META_DATA_EXEC_TIME] = Compile._execute()

        return meta_data

    @staticmethod
    def _compile(flags):
        cmd_list = COMPILE_COMMAND_LIST + ['CFLAGS={}'.format(flags)]
        print('Compiling using...\n{}'.format(' '.join(cmd_list)))
        stmt = 'subprocess.run({}, stderr=subprocess.STDOUT,\
        check=True)'.format(cmd_list)

        return timeit.timeit(stmt=stmt, setup='import subprocess', number=1)

    @staticmethod
    def _execute():
        print('Executing {}'.format(EXECUTABLE_FILE))
        stmt = 'subprocess.run({}, stderr=subprocess.STDOUT,\
        stdout=subprocess.DEVNULL, check=True)'.format([EXECUTABLE_FILE])

        return timeit.timeit(stmt=stmt, setup='import subprocess',
                             number=ITERATIONS) / ITERATIONS

    @staticmethod
    def _clean():
        print('Cleaning up...\n{}'.format(' '.join(CLEAN_COMMAND_LIST)))
        subprocess.run(CLEAN_COMMAND_LIST, stderr=subprocess.STDOUT,
                       stdout=subprocess.DEVNULL)


if __name__ == '__main__':
    Compile.run('-finline-functions -fearly-inlining -ffunction-cse')
