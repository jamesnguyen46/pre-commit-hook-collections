# Pre-commit hook config

The objective of this repository is to manage pre-commit hook version centrally. This repository is implemented from [example](https://github.com/pre-commit/pre-commit/issues/731#issuecomment-376945745).

## Usage

```yaml
repos:
  - repo: https://github.com/jamesnguyen46/pre-commit-hook-config
    rev: v0.1.0
    hooks:
      - id: common-hook
      - id: python-hook
      - ...
```
## Config

### `common-hook`

Includes the below steps:

- `file - check size` : only allow to add file size < 1MB
- `file - fix newline` : makes sure files end in a newline and only a newline.
- `content - detect private key` : checks for the existence of private keys.
- `content - trim space` : trims trailing whitespace.

### `json-hook`

- `json - check syntax`
- `json - auto format`

### `yaml-hook`

- `yaml - check syntax`
- `yaml - auto format`

### `python-hook`

- `python - check file name` : check whether python file path is valid or not. File path is valid when only includes lower characters and not contains `space` character and `hyphen` symbol.
- `python - format code` : using [black](https://github.com/psf/black) to format code.
- `python - check lint` : using [pylint](https://github.com/pycqa/pylint) to analysis source code to helps enforcing a coding standard, sniffs for code smells and offers simple refactoring suggestions.
Default : set max line length 120 and disable some rules such as

  ```yaml
  # missing-module-docstring
  C0114,
  # missing-class-docstring
  C0115,
  # missing-function-docstring
  C0116,
  # too-few-public-methods
  R0903,
  # broad-except
  W0703,
  # no-self-use
  R0201,
  # import-error
  E0401,
  # no-member
  E1101,
  # duplicate-code
  R0801
  ```
