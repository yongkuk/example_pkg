import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
        name = "example_pkg",
        version = "0.0.1",
        author = "Yongkuk Choi",
        author_email = "ykchoi624@gmail.com",
        description = "A tiny project for python packaging practice",
        long_description = long_description,
        log_description_content_type = "text/markdown",
        url = "https://github.com/yongkuk/example_pkg",
