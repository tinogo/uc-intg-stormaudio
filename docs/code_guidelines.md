# Code Style

- Code line length: 120
- Use double quotes as default (don't mix and match for simple quoting, checked with pylint).
- Configuration:
    - `.pylint.rc` for pylint
    - `setup.cfg` for flake8 and isort

## Tooling

Install all code linting tools:

```shell
uv sync
```

### Verify

The following tests are run as GitHub action for each push on the main branch and for pull requests.
They can also be run anytime on a local developer machine:

```shell
uv run -m pylint uc_intg_stormaudio
uv run -m flake8 uc_intg_stormaudio --count --show-source --statistics
uv run -m isort uc_intg_stormaudio/. --check --verbose
```

Linting integration in PyCharm/IntelliJ IDEA:
1. Install plugin [Pylint](https://plugins.jetbrains.com/plugin/11084-pylint)
2. Open Pylint window and run a scan: `Check Module` or `Check Current File`

### Format Code
```shell
uv format
```

### Sort Imports

```shell
ux rn -m isort uc_intg_stormaudio/. --verbose
```
