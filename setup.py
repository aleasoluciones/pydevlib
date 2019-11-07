from setuptools import setup, find_packages

setup(
    name="infdev",
    version="1.0.0",
    author="Bifer Team",
    description="Development tools for Alea Soluciones projects",
    platforms="Linux",
    packages=find_packages(
        exclude=["tests", "specs", "integration_specs", "functional_specs"]
    ),
    install_requires=[
        "six==1.12",
        "mamba==0.10",
        "expects==0.9.0",
        "doublex==1.9.1",
        "doublex-expects==0.7.1",
        "httmock==1.3.0",
        "pyDoubles==1.4",
        "PyHamcrest==1.8.0",
        "fake-factory==0.5.9",
        "deepdiff==3.3.0",
        "coverage==3.7.1",
        "pylint==2.4.3",
        "yapf==0.25.0",
        "black==19.10b0",
    ],
    entry_points={
        "console_scripts": [
            "infdev = infdev.runner:infdev",
            "mambo = infdev.runner:mambo",
            "git_hooks = infdev.runner:git_hooks",
            "linter = infdev.runner:linter",
            "yapf_formatter = infdev.runner:yapf_formatter",
            "black_formatter = infdev.runner:black_formatter",
            "focused_specs = infdev.runner:focused_specs",
            "unit_tests = infdev.runner:unit_tests",
            "integration_tests = infdev.runner:integration_tests",
            "factory_tests = infdev.runner:factory_tests",
            "functional_tests = infdev.runner:functional_tests",
            "acceptance_tests = infdev.runner:acceptance_tests",
            "local_tests = infdev.runner:local_tests",
            "all_tests = infdev.runner:all_tests",
        ]
    },
)
