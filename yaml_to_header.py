import yaml
import sys
import re

def sanitize_key(key):
    return re.sub(r'\W|^(?=\d)', '_', key)

def format_string(s):
    s = s.replace('\\', '\\\\')
    s = s.replace('"', '\\"')
    s = s.replace('\n', '\\n"\n"')
    return f'"{s}"'

def yaml_to_header(yaml_file, header_file):
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)

    with open(header_file, 'w') as f:
        f.write("// Auto-generated header file\n")
        f.write("#ifndef RISCV_INST_DATA_H\n#define RISCV_INST_DATA_H\n\n")
        f.write("#include <stdint.h>\n\n")

        for key, value in data.items():
            c_key = sanitize_key(key)
            if isinstance(value, str):
                f.write(f'const char* {c_key} = {format_string(value)};\n')
            elif isinstance(value, bool):
                f.write(f'const int {c_key} = {1 if value else 0};\n')
            elif isinstance(value, int):
                f.write(f'const int {c_key} = {value};\n')
            elif isinstance(value, list):
                items = ', '.join(format_string(str(item)) for item in value)
                f.write(f'const char* {c_key}[] = {{ {items}, "" }};\n')
            elif isinstance(value, dict):
                for subkey, subvalue in value.items():
                    full_key = sanitize_key(f"{key}_{subkey}")
                    if isinstance(subvalue, str):
                        f.write(f'const char* {full_key} = {format_string(subvalue)};\n')
                    elif isinstance(subvalue, bool):
                        f.write(f'const int {full_key} = {1 if subvalue else 0};\n')
                    elif isinstance(subvalue, int):
                        f.write(f'const int {full_key} = {subvalue};\n')
        f.write("\n#endif\n")

if __name__ == "__main__":
    yaml_file = sys.argv[1] if len(sys.argv) > 1 else "generated.yaml"
    header_file = "inst_data.h"
    yaml_to_header(yaml_file, header_file)
