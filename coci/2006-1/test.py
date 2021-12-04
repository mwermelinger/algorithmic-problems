import glob
import subprocess
from timeit import default_timer as timer

def test(problem, limit=1):
    """Test the given problem with all input files.

    limit is the number of seconds per test
    """
    for infile in sorted(glob.iglob(f'{problem}/*.in.*')):
        outfile = infile.replace('in', 'out')
        command = f'python {problem}.py < {infile} | diff -w - {outfile}'
        start = timer()
        differences = subprocess.run(command, shell=True, text=True,
                                     stdout=subprocess.PIPE)
        runtime = timer() - start
        print('Processed', infile, 'in', f'{runtime:.6}', 'seconds')
        if differences.stdout:
            print(differences.stdout)
        elif runtime > limit:
            print('Time limit possibly exceeded')
