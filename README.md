# uv template

This repository provides a template for managing Python environments and dependencies using [uv](https://docs.astral.sh/uv/getting-started/installation/).

## Setup

### Installing [uv](https://docs.astral.sh/uv/getting-started/installation/)

```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Checking Available Python Versions with uv

```shell
uv python list --all-versions
```

### Specifying a Python Version (refer to `.python-version`)

```shell
uv python pin x.x.x
```

### Installing Python and Dependencies

```shell
uv sync
```

### Running a Python File

```shell
uv run src/sample/main.py
```

### Starting a REPL

```shell
python3
```

### Adding Dependencies

```shell
uv add <package>
uv add --dev <package>
```
