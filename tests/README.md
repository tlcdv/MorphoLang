# MorphoLang Test Suite

This directory contains unit tests for the MorphoLang project.

## Running Tests

Run all tests:
```bash
python -m unittest discover tests
```

Run a specific test file:
```bash
python -m unittest tests.test_compiler
```

Run with verbose output:
```bash
python -m unittest discover tests -v
```

## Test Coverage

- `test_compiler.py`: Tests for the BioCompiler module
- `test_database.py`: Validation tests for the database integrity

## Adding New Tests

When adding new functionality, please add corresponding tests. Follow the existing pattern:

```python
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from your_module import YourClass

class TestYourClass(unittest.TestCase):
    def test_something(self):
        # Your test code
        self.assertEqual(expected, actual)
```
