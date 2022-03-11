from time import perf_counter
import numpy as np
import compute_type_cy
import compute_py
import compute_cy

iter_count = 1000

# setup
m1 = np.random.uniform(0, 1000, size=(100, 100))
m2 = np.random.uniform(0, 1000, size=(100, 100))

print('built in numpy function')
times = []
for i in range(iter_count):
    tic = perf_counter()
    m12 = m1*m2
    toc = perf_counter()
    times.append(toc - tic)
print("%.4f %c %.4f (msec)" % (1000*np.mean(times),  chr(177), 1000*np.std(times)))

print('modified cython function')
times = []
for i in range(iter_count):
    tic = perf_counter()
    m12 = compute_type_cy.compute(m1, m2)
    toc = perf_counter()
    times.append(toc - tic)
print("%.4f %c %.4f (msec)" % (1000*np.mean(times),  chr(177), 1000*np.std(times)))

print('python function')
times = []
for i in range(iter_count):
    tic = perf_counter()
    m12 = compute_py.compute(m1, m2)
    toc = perf_counter()
    times.append(toc - tic)
print("%.4f %c %.4f (msec)" % (1000*np.mean(times),  chr(177), 1000*np.std(times)))

print('unmodified cython function')
times = []
for i in range(iter_count):
    tic = perf_counter()
    m12 = compute_cy.compute(m1, m2)
    toc = perf_counter()
    times.append(toc - tic)
print("%.4f %c %.4f (msec)" % (1000*np.mean(times),  chr(177), 1000*np.std(times)))

