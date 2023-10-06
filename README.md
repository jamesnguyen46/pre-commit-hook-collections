# pre-commit hook group

[![License](https://img.shields.io/badge/license-Apache-orange?label=License&logo=apache&logoColor=white)](https://github.com/jamesnguyen46/pre-commit-hook-group/blob/main/LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/jamesnguyen46/pre-commit-hook-group?label=Last%20Commit&logo=github&logoColor=white&color=yellow)](https://github.com/jamesnguyen46/pre-commit-hook-group/commits/main)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/jamesnguyen46/pre-commit-hook-group/Pre-commit?label=GitHub%20Workflow&logo=githubactions&logoColor=white)

The objective of this repository is to manage pre-commit hook version centrally. It is implemented from [example](https://github.com/pre-commit/pre-commit/issues/731#issuecomment-376945745).

## Usage

```yaml
repos:
  - repo: https://github.com/jamesnguyen46/pre-commit-hook-group
    rev: {lastest_version}
    hooks:
      - id: common-group
      - id: python-group
      - ...
```

## Groups

### `common-group`

Includes the below steps:

- `file - check size` : only allow to add file size < 1MB
- `file - fix newline` : makes sure files end in a newline and only a newline.
- `content - detect private key` : checks for the existence of private keys.
- `content - trim space` : trims trailing whitespace.

### `json-group`

- `json - check syntax`
- `json - auto format`

### `yaml-group`

- `yaml - check syntax`
- `yaml - auto format`

### `markdown-group`

- `markdown - check lint` : using [markdownlint](https://github.com/markdownlint/markdownlint) to check markdown files according ro some [rules](https://github.com/markdownlint/markdownlint/blob/master/docs/RULES.md). Default has disabled some rules as

  ```
  MD002 - First header should be a top level header
  MD013 - Line length
  MD024 - Multiple headers with the same content
  MD033 - Inline HTML
  ```

### `python-group`

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

### `golang-group`

- `golang - check lint` : using [golangci-lint](https://github.com/golangci/golangci-lint)
