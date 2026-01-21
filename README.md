# MorphoLang: A Bioelectric Compiler for Morphogenesis (v0.3)

<img width="1200" height="798" alt="planarian-flatworm-heads-l" src="https://github.com/user-attachments/assets/a4b5431a-54f2-4677-9509-ed727692c715" />

**MorphoLang** is an open-source toolkit that operationalizes the "Bioelectric Code" with **closed-loop homeostatic control**. It treats biological pattern formation as a computational process, allowing researchers to compile high-level anatomical goals (e.g., "Build an Eye") into low-level molecular interventions with feedback mechanisms.

> "If bioelectric dynamics... can be treated as a kind of software, the next revolution in biology could be... driven by the realization that we do not have to manipulate living systems at the level of their 'machine code' (affecting specific molecules), but at the level of information."  
> — *Levin & Martyniuk, 2017*

**Status:** 🧪 **BETA v0.3 - Homeostatic Control** (Research Use Only)

---

## 🆕 What's New in v0.3

### **Closed-Loop Homeostatic Control**
MorphoLang now models bioelectricity as a **feedback system**, not a simple trigger:
- ⏱️ **Monitoring Schedules**: Time-based checkpoints for measuring Vmem drift
- 🔁 **Feedback Mechanisms**: Decision trees for corrective actions when tissues fight back
- 🛑 **Termination Criteria**: Stop conditions to prevent overgrowth/tumors
- 📍 **Spatial Delivery Analysis**: Warnings for local vs. systemic mismatches

### **Enhanced Database**
- Precise dosages (127 μM Octanol, 1-2 ng mRNA)
- Developmental staging (NF Stage 3, Stage 24, etc.)
- Control loop parameters for each subroutine
- Delivery method specifications

---

## 🧬 Core Philosophy

Traditional regenerative medicine attempts to micromanage individual cell fates. **MorphoLang** takes a top-down **pattern homeostasis** approach:

* **Hardware:** Ion channels and gap junctions
* **Software:** Spatio-temporal Vmem patterns  
* **Control Loop:** Closed-loop feedback to maintain target states
* **Subroutines:** Modular anatomical triggers

---

## 🚀 Quick Start

### 1. Installation
```bash
git clone https://github.com/tlcdv/MorphoLang.git
cd MorphoLang
pip install -r requirements.txt
```

### 2. Compile a Homeostatic Protocol

```python
from compiler.experiment_gen import BioCompiler

compiler = BioCompiler()
protocol = compiler.find_subroutine(organ="eye", species="Xenopus laevis")

print(compiler.generate_protocol(protocol))
```

**Output includes:**
```
[PHASE 0: DEVELOPMENTAL CONTEXT]
  Intervention Window: NF Stage 3 → Stage 24

[PHASE 1: TARGET STATE DEFINITION]
  Target Vmem: [-50, -30] mV

[PHASE 2: HARDWARE SELECTION]
  Kv1.5 mRNA: 1-2 ng per blastomere

[PHASE 3: DELIVERY & SPATIAL CONSTRAINTS]
  Method: microinjection (local)
  
[PHASE 4: HOMEOSTATIC MAINTENANCE] ← NEW!
  Monitoring Schedule: Every 6 hours
  
  Feedback Decision Tree:
    IF Vmem > -25mV → Apply booster dose
    ELSE IF Vmem < -55mV → Allow stabilization
    ELSE → Continue monitoring
  
  STOP CONDITIONS:
    1. Optic cup formation (Stage 24)
    2. Vmem normalizes to -40mV
    3. Safety cutoff: 48 hours max

[PHASE 5: SAFETY & VERIFICATION]
  Use Ratiometric Imaging at each checkpoint
```

---

## 📚 Standard Library

| **Subroutine** | **Target** | **Mechanism** | **Control Loop** |
|---|---|---|---|
| `xenopus_eye_v1` | Induce Eye | Kv1.5 (1-2 ng) | Every 6h, 48h max |
| `xenopus_tail_v1` | Regenerate Tail | H+ Pump (500 pg) | Every 4h, 72h max |
| `planaria_head_v1` | Remodel Head | Octanol (127 μM) | Every 12h, 48h max |
| `xenopus_limb_v1` | Regenerate Limb | Monensin (10 mM) | Every 8h, 168h max |

---

## 🔬 Verification (Ratiometric Imaging)

```python
from verification.dye_decode import BioStateValidator

validator = BioStateValidator()

# Analyze Donor (CC2-DMPE) and Acceptor (DiBAC4) channels
vmem_map = validator.analyze_ratiometric(
    donor_path='data/t+12h_cc2.tif',
    acceptor_path='data/t+12h_dibac.tif'
)

success, msg = validator.verify_state(vmem_map, protocol['bioelectric_state'])
print(msg)  # "SUCCESS: Target state MAINTAINED"
```

---

## 🤝 Contributing

We welcome bioelectric subroutines! To contribute:

1. Fork the repo
2. Create a JSON file in `/subroutines` following `subroutine_schema.json`
3. Include:
   - `control_loop` with monitoring frequency and feedback rules
   - `delivery_method` with spatial restriction details
   - `developmental_context` with staging information
4. Ensure data is from peer-reviewed sources
5. Submit a Pull Request

---

## ⚠️ Safety & Ethics

- **Research Use Only**: Protocols are for controlled laboratory environments
- **Animal Ethics**: IACUC approval required for all animal work
- **Tumor Risk**: Stop conditions prevent indefinite interventions
- **Equipment Safety**: High voltage systems require proper training

---

## 📖 Documentation

- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
- [Second Review](sketches/Second%20review.md) - Scientific rationale for v0.3
- [Examples](examples/) - Working code samples

---

## 📄 License

MIT License - See `LICENSE` for details

---

**Based on the research of Dr. Michael Levin (Tufts University) and the principles of bioelectric pattern homeostasis.**

*Version 0.3 implements closed-loop control as described in the "Pattern Homeostasis" model.*
