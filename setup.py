from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="odin",
    description='ODIN detector server',
    url='https://github.com/timcnicholls/odin',
    author='Tim Nicholls',
    author_email='tim.nicholls@stfc.ac.uk',
    packages=find_packages(),
    entry_points={
        'console_scripts' : [
            'odin_server = odin.server:main',
        ],
    },
    install_requires=required,
)
