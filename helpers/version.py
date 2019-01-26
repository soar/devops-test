import pathlib


def get_project_version():
    return pathlib.Path('version.txt').read_text().strip()
