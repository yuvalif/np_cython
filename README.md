# Goal
Demo the performance impact of using [cython on numpy](https://cython.readthedocs.io/en/stable/src/tutorial/numpy.html) code

# Build
```
python setup.py build_ext --inplace 
```

# Run
```
python main.py
```

# Results
```
built in numpy function
0.0043 ± 0.0010 (msec)
modified cython function
0.0211 ± 0.0007 (msec)
python function
4.0440 ± 0.4269 (msec)
unmodified cython function
3.3301 ± 0.0504 (msec)
```
