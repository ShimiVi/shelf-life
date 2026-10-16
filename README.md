# Shelf Life

A small web app for tracking food in your kitchen and what expires soon.

Status: in development.

## Requirements

- Python 3.13+

## Development setup

```bash
git clone https://github.com/ShimiVi/shelf-life.git
cd shelf-life
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

## Running the tests

```bash
pytest
```

## Code style

This project uses [Ruff](https://docs.astral.sh/ruff/) for formatting and linting.

```bash
ruff format .
ruff check .
```
