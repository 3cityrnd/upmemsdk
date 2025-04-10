from setuptools import setup, find_packages
import os

pkgdir='upmemsdk'

def package_files(directory):
    paths = []
    for (path, _, filenames) in os.walk(directory):
        for filename in filenames:
            full_path = os.path.join(path, filename)
            paths.append(os.path.relpath(full_path, pkgdir))
    return paths

extra_files = package_files(pkgdir)

setup(
    name=f'{pkgdir}',
    version='0.1.0',
    packages=find_packages(),
    package_data={'': extra_files},
    include_package_data=True,
    description='UPMEM package SDK (debian, ubuntu , rocky)',
)

