from setuptools import setup, find_packages

setup(
    name="pydevlib",
    version="1.0.3",
    author="Bifer Team",
    description="Development tools for Alea Soluciones projects",
    platforms="Linux",
    packages=find_packages(exclude=["tests", "specs", "integration_specs", "functional_specs", "acceptance_specs"]),
    install_requires=[
        "mamba==0.11.2",
        "expects==0.9.0",
        "doublex",
        "doublex-expects==0.7.1",
        "httmock==1.4.0",
        "pyDoubles==1.8.1",
        "PyHamcrest==2.0.3",
        "Faker==11.3.0",
        "deepdiff==5.7.0",
        "coverage==6.3",
        "pylint==2.14.4",
        "black==22.1.0",
        "mypy==0.931",
        "ipython==7.31.1",
        "ropevim==0.8.1",
    ],
    dependency_links = ['git+https://github.com/davidvilla/python-doublex@0ccbe65c8574169d8b723c1ef29bcbe3f2e98c20#egg=doublex'],
    entry_points={
        "console_scripts": [
            "pydevlib = pydevlib.runner:pydevlib",
            "mambo = pydevlib.runner:mambo",
            "git_hooks = pydevlib.runner:git_hooks",
            "linter = pydevlib.runner:linter",
            "type_checker = pydevlib.runner:type_checker",
            "formatter = pydevlib.runner:formatter",
            "focused_specs = pydevlib.runner:focused_specs",
            "unit_tests = pydevlib.runner:unit_tests",
            "integration_tests = pydevlib.runner:integration_tests",
            "regression_tests = pydevlib.runner:regression_tests",
            "factory_tests = pydevlib.runner:factory_tests",
            "functional_tests = pydevlib.runner:functional_tests",
            "acceptance_tests = pydevlib.runner:acceptance_tests",
            "fast_tests = pydevlib.runner:fast_tests",
            "all_tests = pydevlib.runner:all_tests",
        ]
    },
)
