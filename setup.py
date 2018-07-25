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
    long_description_content_type = "text/markdown",
    include_package_data=True,
    url = "https://github.com/yongkuk/example_pkg",
    packages = setuptools.find_packages(),
    classifiers = (
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux",
    ),
    install_requires=[
        'PyYAML >= 3.0',
        'numpy >= 1.14',
        'pandas >= 0.22.0',
    ],
    entry_points = {
        "console_scripts": ["example_pkg=example_pkg.command_line:__main__"],
    }
)

