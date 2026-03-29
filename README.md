# pi-calc

A small Python package for approximating and exploring the value of π.

## Features

- **Leibniz approximation** – compute π iteratively with configurable precision
- **Digit extraction** – retrieve the first *n* decimal digits of π
- **CLI interface** – run calculations directly from the terminal

## Requirements

- Python 3.10+

## Installation

```bash
# Clone the repository
git clone https://github.com/black0rpheus/pi-swarm-test.git
cd pi-swarm-test

# Create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# Install in editable mode with dev dependencies
pip install -e ".[dev]"
```

## Usage

### Command Line

```bash
# Default: 1,000,000 iterations
pi-calc

# Custom iteration count
pi-calc -n 5000000
```

### Python API

```python
from pi_calc.pi import compute_pi, pi_digits

# Approximate pi
result = compute_pi(iterations=1_000_000)
print(f"Pi ≈ {result}")

# Get the first 10 decimal digits
digits = pi_digits(10)
print(digits)  # [1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
```

## Development

```bash
# Run tests
pytest

# Lint and format
ruff check .
ruff format .
```

## License

MIT
