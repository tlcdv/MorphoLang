# MorphoLang: A Bioelectric Compiler for Morphogenesis (v0.4)

**MorphoLang** is an open source toolkit that operationalizes the "Bioelectric Code." It treats biological pattern formation as a computational process, allowing researchers to compile high level anatomical goals (e.g., "Build an Eye") into low level molecular interventions.

> "If bioelectric dynamics... can be treated as a kind of software, the next revolution in biology could be... driven by the realization that we do not have to manipulate living systems at the level of their 'machine code' (affecting specific molecules), but at the level of information.". 
> *Levin & Martyniuk, 2017*

**Status:** 🧬 **BETA v0.4 - Genetic Interface** (Research Use Only)

---

## 🆕 What's New in v0.4

### **The Genetic Interface**
Bioelectricity is the trigger; genetics is the machinery. v0.4 connects them:
- 🧬 **Downstream Biomarkers**: Protocols now verify that voltage changes successfully trigger specific genes (e.g., *Rx1*, *Msx1*, *Notch*).
- ⏱️ **Temporal Profiles**: Models oscillating vs. constant signals ("pulsatile" vs "steady-state").

### **The "Inverse" Problem (Decoding)**
New tool to read voltage patterns and predict morphology:
- 🔮 **`predict_morphology.py`**: Input a voltage map, output a predicted organ.
  - *Example:* "Warning: -40mV pattern in ventral ectoderm matches Ectopic Eye."

---

## 🧬 Core Philosophy

Traditional regenerative medicine attempts to micromanage individual cell fates. **MorphoLang** takes a top down **pattern homeostasis** approach:

* **Hardware:** Ion channels and gap junctions
* **Software:** Spatio-temporal Vmem patterns  
* **Control Loop:** Closed loop feedback to maintain target states
* **Interface:** Coupling bioelectric triggers to transcriptional networks

---

## 🚀 Quick Start

### 1. Installation
```bash
git clone https://github.com/tlcdv/MorphoLang.git
cd MorphoLang
pip install -r requirements.txt
```

### 2. Compile a Protocol (Forward Engineering)

```python
from compiler.experiment_gen import BioCompiler

compiler = BioCompiler()
protocol = compiler.find_subroutine(organ="eye", species="Xenopus laevis")

print(compiler.generate_protocol(protocol))
```

**Output includes:**
```
[PHASE 4: HOMEOSTATIC MAINTENANCE]
  Monitoring Schedule: Every 6 hours
  Feedback Decision Tree: IF Vmem > -25mV → Apply booster

[PHASE 5: SAFETY & VERIFICATION]
  (!) VERIFICATION METHOD: Ratiometric Voltage Imaging
  
  SECONDARY VERIFICATION (Genetic Markers):
  > Gene:      Rx1 (Retinal Homeobox)
    Expected:  UPREGULATED
    Timing:    Stage 12.5
```

### 3. Decode a Pattern (Reverse Engineering)

You observe a hyperpolarized patch (-40mV) in the ventral ectoderm. What is the tissue building?

```python
from compiler.predict_morphology import BioDecoder

decoder = BioDecoder()
prediction = decoder.predict(vmem=-40.0, spatial_domain="ventral_ectoderm")

print(decoder.generate_report(prediction))
```

**Output:**
```
PREDICTION #1: INDUCE EYE
  Mechanism:  Hyperpolarized domain mimicking Anterior Neural Field
  Confidence: High
  Verifiers:  Check for expression of Rx1, Pax6
```

---

## 📚 Standard Library

| **Subroutine** | **Target** | **Mechanism** | **Biomarkers** |
|---|---|---|---|
| `xenopus_eye_v1` | Induce Eye | Kv1.5 (1-2 ng) | *Rx1*, *Pax6* |
| `xenopus_tail_v1` | Regenerate Tail | H+ Pump (500 pg) | *Notch*, *Msx1* |
| `planaria_head_v1` | Remodel Head | Octanol (127 μM) | *ndk*, *smed-prep* |
| `xenopus_limb_v1` | Regenerate Limb | Monensin (10 mM) | *Msx1* |

---

## 🤝 Contributing

We welcome bioelectric subroutines! To contribute:

1. Fork the repo
2. Create a JSON file in `/subroutines` following `subroutine_schema.json`
3. Include:
   - `downstream_biomarkers` (gene targets)
   - `control_loop` parameters
   - `temporal_profile` (constant/oscillating)
4. Submit a Pull Request.

---

## ⚠️ Safety & Ethics

- **Research Use Only**: Protocols are for controlled laboratory environments
- **Animal Ethics**: IACUC approval required for all animal work
- **Tumor Risk**: Stop conditions prevent indefinite interventions

---

## 📄 License

MIT License - See `LICENSE` for details

---

**Based on the research of Dr. Michael Levin (Tufts University) and the principles of bioelectric pattern homeostasis.**
