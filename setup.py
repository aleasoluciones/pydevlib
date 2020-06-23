from setuptools import setup, find_packages

setup(
    name="pydevlib",
    version="1.0.0",
    author="Bifer Team",
    description="Development tools for Alea Soluciones projects",
    platforms="Linux",
    packages=find_packages(exclude=["tests", "specs", "integration_specs", "functional_specs"]),
    install_requires=[
        "six==1.15",
        "mamba==0.11",
        "expects==0.9.0",
        "doublex==1.9.2",
        "doublex-expects==0.7.1",
        "httmock==1.3.0",
        "pyDoubles==1.8.1",
        "PyHamcrest==2.0.2",
        "Faker==4.1.1",
        "deepdiff==5.0.0",
        "coverage==5.1",
        "pylint==2.5.3",
        "yapf==0.30.0",
    ],
    entry_points={
        "console_scripts": [
            "pydevlib = pydevlib.runner:pydevlib",
            "mambo = pydevlib.runner:mambo",
            "git_hooks = pydevlib.runner:git_hooks",
            "linter = pydevlib.runner:linter",
            "yapf_formatter = pydevlib.runner:yapf_formatter",
            "focused_specs = pydevlib.runner:focused_specs",
            "unit_tests = pydevlib.runner:unit_tests",
            "integration_tests = pydevlib.runner:integration_tests",
            "factory_tests = pydevlib.runner:factory_tests",
            "functional_tests = pydevlib.runner:functional_tests",
            "acceptance_tests = pydevlib.runner:acceptance_tests",
            "fast_tests = pydevlib.runner:fast_tests",
            "all_tests = pydevlib.runner:all_tests",
        ]
    },
)
