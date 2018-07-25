# Example Package

There are many things in python programming that is conceptually not very hard, but requires 
practices. This is a simple example package for me to practice those. 
You can check each step of the development by checking out the commits.
Below is the list of the concepts I practiced. I'll update the list as this package grows.
- Distribution of a python package
- Parallelization
- Developing a command line tool
- General python programming
- Developing a python package using git


As the first practice, I used `setuptools` to distribute my package. Now installation can be 
easily done by typing
```
$ git clone https://github.com/yongkuk/example_pkg
$ cd example_pkg
$ pip install .
```


Next, I implemented parallel execution of tasks using the `concurrent.futures` module.
The program tests if the numbers given in `presets/default.cfg`
are prime or not. You can choose between `ThreadPoolExecutor` and `ProcessPoolExecutor` by 
setting the option `--mode` as either `process` or `thread`.
```
$ example_pkg --mode process -p 4 --quiet
Parallel mode : process
112272535095293 is prime: True
112582705942171 is prime: True
112272535095293 is prime: True
115280095190773 is prime: True
115797848077099 is prime: True
1099726899285419 is prime: False
Finished in 1.0011513233184814s
```

