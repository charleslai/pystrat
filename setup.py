from distutils.core import setup

setup(
    name='PyStrat',
    version='0.0.1',
    author='Charles J. Lai',
    author_email='cjl223@cornell.edu',
    packages=['pystrat', 'pystrat.test'],
    scripts=[],
    url='',
    license='LICENSE.txt',
    description='A python trading strategy backtesting system.',
    long_description=open('README.txt').read(),
    install_requires=[
    ],
)