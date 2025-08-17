from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ANIME-RECOMMENDER",
    version="0.1",
    author="Sudhanshu",
    packages=find_packages(), #automatically finds all Python packages (folders with __init__.py) in your project.
    install_requires = requirements, #Uses the requirements list from earlier, ensuring all libraries listed in requirements.txt are installed when someone installs your package.
)