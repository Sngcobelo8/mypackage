from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='recursion functions and sorting functions package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Sngcobelo8/mypackage',
    author='Sonwabo Ngcobelo',
    author_email='sngcobelo@gmail.com'
)
