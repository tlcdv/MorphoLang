# Hardware Drivers

This directory is intended to house the low-level specifications for biological actuators.

## Structure
- `ion_channels.db`: Database of ion channels (e.g., Kv1.5, Kir4.1) and their Vmem effects.
- `pharmacology.db`: Database of drugs (e.g., Ivermectin, Monensin) and their targets.

## Usage
These files will be referenced by the compiler to resolve generic driver requests (e.g. "Hyperpolarizing Channel") to specific implementable parts (e.g. "Kv1.5 mRNA sequence").
