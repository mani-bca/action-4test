from setuptools import setup, find_packages

setup(
    name="todo-app",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'pytest>=7.4.0',
    ],
)