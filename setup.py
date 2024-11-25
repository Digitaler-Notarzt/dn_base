from setuptools import setup, find_packages


def read_requirements(file):
    with open(file) as f:
        return f.read().splitlines()


def read_file(file):
   with open(file) as f:
        return f.read()


long_description = read_file("README.md")
requirements = read_requirements("requirements.txt")

setup(
    name = 'dn_base',
    version = '0.1',
    author = 'Markus Stuppnig',
    author_email = 'markus@stuppnig.net',
    description = 'Core dependencies for dino diploma thesis backend',
    long_description_content_type = "text/markdown",
    long_description = long_description,
    packages = find_packages(exclude=["test"]),  # Don't include test directory in binary distribution
    install_requires = requirements,
)
