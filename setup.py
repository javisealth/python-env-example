# -*- coding: utf-8 -*-

from src import killer_app
from setuptools import setup, find_packages

# Package dependencies
install_requires = [

]

# Trove classifiers
classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.5',
]


setup(
    # Package info
    name=killer_app.name,
    version=killer_app.version,
    description=killer_app.description,
    author=killer_app.author,
    author_email=killer_app.author_email,
    url='',
    long_description=killer_app.description,

    # Package classifiers
    classifiers=classifiers,

    # Package structure
    packages=find_packages('src', exclude=['ez_setup', '*.tests', '*.tests.*', 'tests.*', 'tests']),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,

    # Dependencies
    install_requires=install_requires,

    # Entry points
    entry_points={
        'console_scripts': [
            'killer_app = killer_app.main:main',
        ],
    }
)
