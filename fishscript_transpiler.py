import os
import re
import sys

def transpile_fishscript_file(filename, imported_modules=None):
    if imported_modules is None:
        imported_modules = set()
    
    with open(filename, 'r') as f:
        lines = f.readlines()

    output = []
    indent_level = 0
    indent = lambda: '    ' * indent_level
    
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith('//') or stripped.startswith('#'):
            continue
        m = re.match(r'import (\w+);', stripped)
        if m:
            mod = m.group(1)
            if mod not in imported_modules:
                imported_modules.add(mod)
                mod_file = os.path.join(os.path.dirname(filename), f"{mod}.fish")
                output.append(f"# Importing {mod}.fish")
                mod_code = transpile_fishscript_file(mod_file, imported_modules)
                output.append(mod_code)
            continue
        m = re.match(r'(public|private)?\s*(int|float|string|boolean)\s+(\w+)\s*=\s*(.+);', stripped)
        if m:
            var_type = m.group(2)
            var_name = m.group(3)
            var_value = m.group(4)
            output.append(f"{indent()}{var_name} = {var_value}")
            continue
        m = re.match(r'while (.+) {', stripped)
        if m:
            cond = m.group(1)
            output.append(f"{indent()}while {cond}:")
            indent_level += 1
            continue
        m = re.match(r'(public|private)?\s*(\w+)\(([^)]*)\) {', stripped)
        if m:
            func_name = m.group(2)
            params = m.group(3)
            py_params = ', '.join([p.split()[-1] for p in params.split(',') if p.strip()])
            output.append(f"{indent()}def {func_name}({py_params}):")
            indent_level += 1
            continue
        m = re.match(r'if\s+!(.+) {', stripped)
        if m:
            cond = m.group(1).strip()
            output.append(f"{indent()}if not {cond}:")
            indent_level += 1
            continue
        m = re.match(r'if (.+) {', stripped)
        if m:
            cond = m.group(1)
            output.append(f"{indent()}if {cond}:")
            indent_level += 1
            continue
        m = re.match(r'else if (.+) {', stripped)
        if m:
            cond = m.group(1)
            output.append(f"{indent()}elif {cond}:")
            indent_level += 1
            continue
        m = re.match(r'else {', stripped)
        if m:
            output.append(f"{indent()}else:")
            indent_level += 1
            continue
        if stripped == '}':
            indent_level = max(0, indent_level - 1)
            continue
        m = re.match(r'print\((.*)\);', stripped)
        if m:
            output.append(f"{indent()}print({m.group(1)})")
            continue
        m = re.match(r'return (.+);', stripped)
        if m:
            output.append(f"{indent()}return {m.group(1)}")
            continue
        m = re.match(r'(\w+) = ([\w\.]+)\((.*)\);', stripped)
        if m:
            var = m.group(1)
            func_call = m.group(2)
            args = m.group(3)
            if '.' in func_call:
                func_call = func_call.split('.')[-1]
            output.append(f"{indent()}{var} = {func_call}({args})")
            continue
        output.append(f"{indent()}# [unparsed] {stripped}")
    return '\n'.join(output)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: fish <file.fish>")
        sys.exit(1)
    fs_file = sys.argv[1]
    py_code = transpile_fishscript_file(fs_file)
    out_file = os.path.splitext(fs_file)[0] + '.py'
    with open(out_file, 'w') as f:
        f.write(py_code)
