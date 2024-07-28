from setuptools import setup, find_packages

setup(
    name='ml2024-summer-sofia',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        # Add dependencies here
    ],
    entry_points={
        'console_scripts': [
            'find_number=ML2024-SUMMER-SOFIA.main:main',
        ],
    },
    author='Siddharth Santhanakrishnan',
    author_email='siddharth.san.work@gmail.com',
    description='A project to find the index of a number in a list.',
    url='https://github.com/sidkrish03/ml2024-summer-sofia',
)
