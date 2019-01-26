from distutils.core import setup
from pathlib import Path

from helpers.version import get_project_version

setup(
    name='devops-test',
    version=get_project_version(),
    packages=[''],
    url='https://soar.name',
    license='GNU GPLv3 ',
    author='Aleksey @soar Smyrnov',
    author_email='i@soar.name',
    description='Test Task for DevOps Interview'
)
