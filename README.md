# Example Package

This is a simple example package for me to practice how to use the setuptools.

Install by typing
```
$ git clone https://github.com/yongkuk/example_pkg
$ cd example_pkg
$ pip install .
```
As the first practice, I implemented parallel execution of tasks using the 
concurrent.futures module. The program tests if the numbers given in `presets/default.cfg`
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

