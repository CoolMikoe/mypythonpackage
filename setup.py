from setuptools import setup, find_packages

setup(
    name='mypythonpackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<coolmikoe>/<mypythonpackage>',
    author='<Your Name>',
    author_email='<mykerhun@gmail.com>'
)