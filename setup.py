from distutils.core import setup
from pathlib import Path

setup(
    name='devops-test',
    version=Path('version.txt').read_text().strip(),
    packages=[''],
    url='https://soar.name',
    license='GNU GPLv3 ',
    author='Aleksey @soar Smyrnov',
    author_email='i@soar.name',
    description='Test Task for DevOps Interview'
)
