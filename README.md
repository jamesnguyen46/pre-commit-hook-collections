# Pre-commit hook config

The objective of this repository is to manage pre-commit hook version centrally. This repository is implemented from [example](https://github.com/pre-commit/pre-commit/issues/731#issuecomment-376945745).

## Usage

```yaml
repos:
  - repo: https://github.com/jamesnguyen46/pre-commit-hook-config
    rev: v0.1.0
    hooks:
      - id: common-hkgrp
      - id: python-hkgrp
      - ...
```
## Config

### `common-hkgrp`

Include the below steps:

- `file - check size` : only allow to add file size < 1MB
- `file - fix newline` : makes sure files end in a newline and only a newline.
- `content - detect private key` : checks for the existence of private keys.
- `content - trimp space` : trims trailing whitespace.

### `python-hkgrp`

Include the below steps:

- `python - check file name` : check whether python file path is valid or not. File path is valid when only includes lower characters and not contains `space` character and `hyphen` symbol.
- `python - format code` : using [black](https://github.com/psf/black) to format code.
- `python - check lint` : using [pylint](https://github.com/pycqa/pylint) to analysis source code to helps enforcing a coding standard, sniffs for code smells and offers simple refactoring suggestions. 

