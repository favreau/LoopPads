"""setup.py"""
import os
import pathlib
import pkg_resources
from setuptools import find_packages, setup

BASEDIR = os.path.dirname(os.path.abspath(__file__))

def parse_reqs(reqs_file):
    ''' parse the requirements '''
    install_reqs = list()
    with pathlib.Path(reqs_file).open() as requirements_txt:
        install_reqs = [str(requirement)
                        for requirement
                        in pkg_resources.parse_requirements(requirements_txt)]
    return install_reqs


REQS = parse_reqs(os.path.join(BASEDIR, "requirements.txt"))

# read the contents of README.md
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    packages=find_packages(),
    install_requires=REQS,
    name='looppads',
    description='LoopPads for all',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/favreau/LoopPads.git',
    author='Cyrille Favreau',
    license='LGPLv3',
    project_urls={
            "Documentation": "",
            "Source": "https://github.com/favreau/LoopPads",
    }
)
