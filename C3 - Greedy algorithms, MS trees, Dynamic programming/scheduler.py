import numpy as np
import functools

if __name__ == '__main__':
    file_name = 'jobs.txt'
    # file_name = 'jobsTest2.txt'
    criteria = 'diff' # diff, ratio

    inc_scheduler = {
        'diff' : lambda x: (x[0]-x[1], x[0]),
        'ratio' : lambda x: x[0]/x[1],
    }
    with open(file_name, 'r') as f:
        num_jobs = f.readline()
        jobs = [ list(map(int, line.split())) for line in f.readlines() ]

    print('1 Jobs are loaded from file...')
    # print(jobs)
    jobs.sort(key=inc_scheduler.get(criteria), reverse=True)
    # print(jobs)
    print('2 Jobs are sorted as per criteria...')

    jobs = list(zip(*jobs))
    weights = np.array(jobs[0], dtype=np.uint64)
    comp_times = np.cumsum(jobs[1], dtype=np.uint64)
    print(f'3 calculating cumsum for {criteria} criteria... {np.dot(weights, comp_times)}')
