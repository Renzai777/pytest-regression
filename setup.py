# setup.py
from setuptools import setup, find_packages

setup(
    name="pytest-regression",
    version="0.1.0",
    description="A pytest plugin to repeat the entire test suite in batches.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/your-username/pytest-regression",
    packages=find_packages(),
    entry_points={
        "pytest11": [
            "pytest_regression = pytest_regression.plugin",
        ]
    },
    install_requires=["pytest>=6.0.0"],
    classifiers=[
        "Framework :: Pytest",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
