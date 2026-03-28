# Calculator

A simple calculator library with core arithmetic operations.

## Features

- **Addition** — sum two or more numbers
- **Subtraction** — subtract one number from another
- **Multiplication** — multiply two or more numbers
- **Division** — divide one number by another (with zero-division protection)

## Installation

```bash
pip install -e ".[dev]"
```

## Usage

```python
from calculator.engine import Calculator

calc = Calculator()
result = calc.add(2, 3)       # 5
result = calc.subtract(10, 4) # 6
result = calc.multiply(3, 7)  # 21
result = calc.divide(10, 2)   # 5.0
```

## Development

### Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

### Run Tests

```bash
pytest
```

### Linting

```bash
ruff check src/ tests/
```

### Type Checking

```bash
mypy src/
```

## Project Structure

```
calculator/
├── src/
│   └── calculator/
│       ├── __init__.py
│       ├── engine.py       # Core Calculator class
│       └── errors.py       # Custom error types
├── tests/
│   ├── __init__.py
│   ├── test_engine.py
│   └── test_errors.py
├── pyproject.toml
└── README.md
```

## License

MIT
