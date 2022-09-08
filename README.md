# Parallelization in Python

### Summary

This repository consists of a template for parallelizing tasks in Python. This template can be easily modified for your application. All methods are based on the multiprocessing module.

### How to parallelize tasks in Python

Using the multiprocessing module it is possible to parallelize tasks in python by 

```python
from multiprocessing import Pool

with Pool() as pool:
        output = pool.map(run_subtask, arguments)
```

and for tasks with multiple input arguments you can use
```python
output = pool.starmap(run_subtask, arguments)
```
instead.

There also exist different alternatives to `pool.map` method, such as `pool.map_async`, `pool.imap`, `pool.imap_unordered`, which might be more suitable in terms of speed and memory allocation depending on your application. For more details about these methods see [this stackoverflow post](https://stackoverflow.com/a/26521507) or multiprocessing [documentation](https://docs.python.org/3/library/multiprocessing.html).

### Warning - Shared databases or data structures
When parallelizing tasks one has to be especially careful with subtasks that need access to same data structures (e.g. tasks that write to the same databases). In this case it might be necessary to further adjust these methods to avoid their collisions during the parallelized process. For more information see multiprocessing [documentation](https://docs.python.org/3/library/multiprocessing.html). However, if you are parallelizing subtasks that do not need access to shared data structures (e.g. Monte Carlo simulations) you can simply use the methods above to speed up your computations.