# pydevlib

Alea Soluciones development utils & scripts meant to be used in Python projects


## Requirements

You'll need bash as your shell and it works on Python 3.7+


## Install

Simply run on your virtualenv:

```pip install -e git+https://github.com/aleasoluciones/pydevlib.git#egg=pydevlib```

or add to your requirements-dev.txt (recommended)

```-e git+https://github.com/aleasoluciones/pydevlib.git#egg=pydevlib```


## Usage

Once the module is installed, you can simply run

`pydevlib`

to list available commands. Actually, the commands list is:

```
mambo -> Alias for mamba -f documentation
git_hooks -> Install pre-commit and pre-push git hooks
linter -> Run pylint for production and specs code
type_checker -> Run MyPY for production and specs code to perform static type checking
yapf_formatter -> Run YAPF to format python code
focused_specs -> Search for focused specs across the code
unit_tests -> Run unit tests
factory_tests -> Run factory tests
integration_tests -> Run integration tests
functional_tests -> Run functional tests
acceptance_tests -> Run acceptance tests
regression_tests -> Run regression tests
fast_tests -> Run all fast tests (unit, factory and integration tests)
all_tests -> Run all tests but acceptance tests (unit, factory, integration and functional tests)
```

The way you can use the commands is simply like this:

`git_hooks`

For scripts that may accept arguments, you can do:

`linter staged`
`yapf_formatter your_file another_file`
`unit_tests doc`


## Development

Simply clone this repository and run

```dev/setup_venv.sh```


### TODO

- Document virtualenv path to be searched is the default repository name
- Document special script cases
- Unify functional test across projects
- Add a command to list the installed python development libraries with a link to documentation
