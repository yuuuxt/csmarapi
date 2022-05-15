from setuptools import find_packages, setup

setup(
    name="csmarapi",
    version='0.0.1',

    author='csmar',

    packages=find_packages(where='src'),
    package_dir={'': 'src'}
)
