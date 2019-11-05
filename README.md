# infdev

Alea Soluciones development utils & scripts meant to be used in Python projects


## Requirements

Works on Python 3.7+

## Install

TODO

## Usage

Once the module is installed (it's recommended to be put on a requirements-dev.txt inside your project), you can simply run

`dev -l`

to list available commands. Actually, the commands list is:

```
git_hooks
linter
yapf_formatter
black_formatter
focused_specs
unit_tests
factory_tests
integration_tests
functional_tests
acceptance_tests
local_tests
all_tests
```

The way you can use the commands is simply like this:

`dev git_hooks`

For scripts that may accept arguments, you can do:

`dev yapf_formatter your_file`
`dev unit_tests doc`



### TODO

- Improve documentation
- Document special script cases
- Autocomplete commands
