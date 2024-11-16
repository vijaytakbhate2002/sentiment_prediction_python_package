import io
import os
from pathlib import Path
from setuptools import find_packages, setup

# Metadata of package
NAME = 'sentiment_prediction'
DESCRIPTION = 'An end-to-end machine learning project for Twitter sentiment classification'
URL = 'https://github.com/vijaytakbhate2002/Twitter-Post-Sentiment-Prediction--NLP-.git'
EMAIL = 'vijaytakbhate20@gmail.com'
AUTHOR = 'Vijay Dipak Takbhate'
REQUIRES_PYTHON = '>=3.7'

pwd = os.path.abspath(os.path.dirname(__file__))

# Get the list of packages to be installed
def list_reqs(fname='requirements.txt'):
    try:
        with io.open(os.path.join(pwd, fname), encoding='utf-16') as f:
            return f.read().splitlines()
    except FileNotFoundError:
        pass

try:
    with io.open(os.path.join(pwd, 'README.md'), encoding='utf-16') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / NAME

setup(
    name=NAME,
    version="1.0.0",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    package_data={NAME: ['VERSION']},
    install_requires=list_reqs(),
    extras_require={},
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
