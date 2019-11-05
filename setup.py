from setuptools import setup, find_packages

setup(
    name="infdev",
    version="0.0.1",
    author="Bifer Team",
    description="Development tools for Alea Soluciones projects",
    platforms="Linux",
    packages=find_packages(exclude=["tests", "specs", "integration_specs", "functional_specs"]),
    install_requires=[
        'mamba==0.10',
        'expects==0.9.0',
        'doublex==1.9.1',
        'doublex-expects==0.7.1',
        'httmock==1.3.0',
        'pyDoubles==1.4',
        'PyHamcrest==1.8.0',
        'fake-factory==0.5.9',
        'deepdiff==3.3.0',
        'coverage==3.7.1',
        'pylint==2.4.3',
        'yapf==0.25.0',
        'black==19.10b0',
    ],
    entry_points={
        'console_scripts': ['dev = infdev.runner:main'],
    })
