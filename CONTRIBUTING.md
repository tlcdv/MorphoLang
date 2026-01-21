# Contributing to MorphoLang

We welcome contributions from the bioelectricity research community! MorphoLang aims to be a comprehensive, standardized toolkit for bioelectric morphogenesis.

## How to Contribute

### 1. Reporting Bugs or Issues
- Use the GitHub Issues tab to report bugs
- Provide detailed information about the issue
- Include steps to reproduce the problem

### 2. Suggesting New Features
- Open an issue with the "Feature Request" label
- Describe the feature and its use case
- Explain how it aligns with MorphoLang's mission

### 3. Contributing New Bioelectric Subroutines

This is the most valuable contribution! If you have discovered a bioelectric intervention that produces a reproducible morphological outcome:

#### Step 1: Prepare Your Data
Ensure you have:
- **Peer-reviewed publication** or preprint with experimental validation
- **Target Vmem range** (membrane potential in mV)
- **Spatial domain** where the intervention must be applied
- **Duration** of the bioelectric state
- **Hardware drivers** (ion channels, drugs, etc.) that produce this state

#### Step 2: Create the Subroutine File
1. Fork this repository
2. Create a new JSON file in `/subroutines` following this naming convention:
   ```
   {species}_{organ}_{action}_{version}.json
   ```
   Example: `xenopus_eye_induce_v1.json`

3. Follow the schema defined in `subroutine_schema.json`:
   ```json
   {
     "id": "unique_identifier_v1",
     "metadata": {
       "author": "FirstAuthor et al.",
       "description": "Brief description of the morphological outcome",
       "version": "1.0",
       "references": [
         "DOI or citation"
       ]
     },
     "target_morphology": {
       "organ": "eye",
       "species": "Xenopus laevis",
       "action": "induce"
     },
     "bioelectric_state": {
       "target_vmem_range": [-50, -30],
       "spatial_domain": "ventral_ectoderm",
       "duration_hours": 24,
       "notes": "Additional context"
     },
     "hardware_drivers": [
       {
         "type": "ion_channel_mRNA",
         "name": "Kv1.5",
         "mechanism_of_action": "Voltage-gated Potassium efflux",
         "dosage": "See reference"
       }
     ]
   }
   ```

4. Validate your JSON:
   ```bash
   python -m json.tool subroutines/your_file.json
   ```

#### Step 3: Update the Database
Add your subroutine to `database/database_seed.json` by appending it to the array.

#### Step 4: Submit a Pull Request
- Create a descriptive PR title (e.g., "Add limb regeneration subroutine for Axolotl")
- Include a summary of the biological phenomenon
- Reference the primary literature
- Await review from maintainers

### 4. Code Contributions

If you want to improve the compiler, verification tools, or add new features:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Write clean, documented code
4. Test your changes
5. Commit with clear messages
6. Push to your fork
7. Open a Pull Request

#### Code Style
- Follow PEP 8 for Python code
- Use docstrings for all functions and classes
- Add type hints where possible
- Keep functions focused and modular

### 5. Documentation

Help us improve documentation:
- Fix typos or unclear explanations
- Add examples or tutorials
- Improve code comments
- Translate documentation to other languages

## Code of Conduct

### Our Standards
- Be respectful and inclusive
- Focus on constructive feedback
- Acknowledge contributions from others
- Prioritize scientific rigor and reproducibility

### Unacceptable Behavior
- Harassment or discriminatory language
- Submitting false or unvalidated data
- Plagiarism or misrepresentation of sources

## Questions?

Open an issue with the "Question" label or contact the maintainers.

## Attribution

All contributors will be acknowledged in the project documentation. By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for helping advance bioelectric research!
