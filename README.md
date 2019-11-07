# infdev

Alea Soluciones development utils & scripts meant to be used in Python projects


## Requirements

You'll need bash as your shell and it works on Python 3.7+


## Install

TODO

## Usage

Once the module is installed (it's recommended to be put on a requirements-dev.txt inside your project), you can simply run

`infdev`

to list available commands. Actually, the commands list is:

```
mambo -> Alias for mamba -f documentation
git_hooks -> Install pre-commit and pre-push git hooks
linter -> Run pylint for production and specs code
yapf_formatter -> Run YAPF to format python code
black_formatter -> Run Black to format python code
focused_specs -> Search focused specs across the code
unit_tests -> Run unit tests
factory_tests -> Run factory tests
integration_tests -> Run integration tests
functional_tests -> Run functional tests
acceptance_tests -> Run acceptance tests
local_tests -> Run all local tests (unit, factory and integration tests)
all_tests -> Run all tests but acceptance tests (unit, factory, integration and functional tests
```

The way you can use the commands is simply like this:

`git_hooks`

For scripts that may accept arguments, you can do:

`yapf_formatter your_file another_file`
`unit_tests doc`



### TODO

- Document special script cases
