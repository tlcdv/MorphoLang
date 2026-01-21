# MorphoLang Project Structure

## Directory Tree

```
MorphoLang/
├── .github/                          # GitHub-specific files
│   ├── ISSUE_TEMPLATE/               # Issue templates
│   │   ├── bug_report.md
│   │   ├── feature_request.md
│   │   └── subroutine_contribution.md
│   ├── pull_request_template.md
│   └── FUNDING.yml
│
├── compiler/                         # The Bioelectric Compiler
│   ├── __init__.py
│   └── experiment_gen.py             # Main compiler logic
│
├── database/                         # Validated bioelectric subroutines
│   └── database_seed.json            # Seed database (4 subroutines)
│
├── docs/                             # Research papers (gitignored)
│   └── [PDF files...]
│
├── examples/                         # Usage examples
│   ├── README.md
│   ├── induce_eye_example.py
│   └── regenerate_tail_example.py
│
├── hardware_drivers/                 # Low-level actuator specs
│   └── README.md
│
├── sketches/                         # Development notes (gitignored)
│   └── [Guide files...]
│
├── subroutines/                      # Individual subroutine files
│   ├── xenopus_ectopic_eye_induction_v1.json
│   ├── xenopus_tail_regeneration_rescue_v1.json
│   ├── planaria_head_species_remodeling_v1.json
│   └── xenopus_limb_regeneration_induction_v1.json
│
├── tests/                            # Unit tests
│   ├── __init__.py
│   ├── README.md
│   ├── test_compiler.py
│   └── test_database.py
│
├── verification/                     # Voltage dye analysis tools
│   ├── __init__.py
│   └── dye_decode.py
│
├── .gitignore                        # Git ignore rules
├── CONTRIBUTING.md                   # Contribution guidelines
├── LICENSE                           # MIT License
├── README.md                         # Main documentation
├── requirements.txt                  # Python dependencies
└── subroutine_schema.json           # JSON schema for subroutines
```

## File Count

- **Total Python files**: 8
- **Total JSON files**: 6
- **Total Markdown files**: 11
- **Test coverage**: 12 unit tests

## Key Components

### 1. Core Modules
- `compiler/experiment_gen.py`: Translates anatomical goals into lab protocols
- `verification/dye_decode.py`: Validates bioelectric states from imaging data

### 2. Data Layer
- `subroutine_schema.json`: Defines the standard format
- `database/database_seed.json`: Central knowledge base
- `subroutines/*.json`: Individual validated interventions

### 3. Community Infrastructure
- GitHub issue templates for bugs, features, and contributions
- Pull request template
- Comprehensive CONTRIBUTING.md
- Example scripts for onboarding

### 4. Quality Assurance
- Unit tests for compiler logic
- Database integrity validation tests
- All 12 tests passing

## Next Steps

1. Initialize git repository
2. Create GitHub repository at https://github.com/tlcdv/MorphoLang
3. Push code to remote
4. Set up repository description and topics
5. Announce to bioelectricity research community
