# MorphoLang Examples

This directory contains example scripts demonstrating how to use MorphoLang for various bioelectric interventions.

## Available Examples

### 1. Eye Induction (`induce_eye_example.py`)
Demonstrates how to generate a protocol for inducing ectopic eye formation in *Xenopus laevis* using the bioelectric compiler.

**Run it:**
```bash
python examples/induce_eye_example.py
```

### 2. Tail Regeneration (`regenerate_tail_example.py`)
Shows how to compile a protocol for rescuing tail regeneration in non-regenerative contexts.

**Run it:**
```bash
python examples/regenerate_tail_example.py
```

## Creating Your Own Experiments

To create a custom experiment:

```python
from compiler.experiment_gen import BioCompiler

# Initialize compiler
compiler = BioCompiler()

# Find a subroutine
subroutine = compiler.find_subroutine(
    organ="your_target_organ",
    species="Target Species Name"
)

# Generate protocol
if subroutine:
    protocol = compiler.generate_protocol(subroutine)
    print(protocol)
```

## Adding New Examples

We welcome example contributions! If you have a particularly interesting use case, please submit a pull request with:
- A well-commented Python script
- A brief description in this README
- Expected output or results
