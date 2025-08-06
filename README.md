# RISC-V YAML ↔ C Header ↔ YAML Roundtrip Converter

This project demonstrates how to take YAML files from the RISC-V Unified Database, convert them into a C header file using Python, and then use a C program to convert that header back into YAML. The point of this exercise was to make sure that information is preserved across formats, and that the converted YAML matches the structure of the input.

## What This Does

- Reads a YAML file (e.g., `andn.yaml`) from the `spec/std/isa/inst/` directory in the [riscv-unified-db](https://github.com/riscv-software-src/riscv-unified-db) repo.
- Converts it to a `.h` file (`inst_data.h`) that defines each field as a C constant.
- Then uses a C program to print out the contents of that `.h` file in YAML format.
- Finally, it supports doing the same process again using the generated YAML file, and the result will match exactly.

---

## Files

| File | Description |
|------|-------------|
| `yaml_to_header.py` | Python script to convert YAML to C header |
| `inst_data.h` | Generated C header file from the YAML |
| `header_to_yaml.c` | C file that includes the header and prints YAML |
| `generated.yaml` | YAML file generated from the C program |
| `test.yaml` | Example RISC-V YAML input file |

---

## 🔧 How to Run

### 1. Clone the Unified DB repo and choose a YAML file

```bash
git clone https://github.com/riscv-software-src/riscv-unified-db
cd riscv-unified-db/spec/std/isa/inst
```
Pick any instruction YAML, like andn.yaml.
### 2. Convert YAML to C header using Python
Install dependencies:
```bash
pip install pyyaml
```
Run the converter:
```bash
python3 yaml_to_header.py andn.yaml
```
This creates inst_data.h.
### 3. Compile and run the C program
```bash
gcc header_to_yaml.c -o header_to_yaml
./header_to_yaml > generated.yaml
```
You’ll now have a new generated.yaml file.
### 4. Roundtrip test
Try feeding generated.yaml back into the Python script:
```bash
python3 yaml_to_header.py generated.yaml
```
Re-run the C program again:
```bash
./header_to_yaml > regenerated.yaml
```
You’ll see that generated.yaml and regenerated.yaml match — proving that the data structure is preserved.
```bash
./header_to_yaml > generated.yaml
```
