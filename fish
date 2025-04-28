if [ $# -eq 0 ]; then
  echo "Usage: fish <file.fish>"
  exit 1
fi

FISH_FILE="$1"
EXT="${FISH_FILE##*.}"
if [ "$EXT" != "fish" ]; then
  echo "Please provide a .fish file to run."
  exit 1
fi

PYTHON_BIN=""
if command -v python3 >/dev/null 2>&1; then
  PYTHON_BIN="python3"
elif command -v python >/dev/null 2>&1; then
  PYTHON_BIN="python"
else
  echo "Python is required but not found. Please install Python 3."
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
"$PYTHON_BIN" "$SCRIPT_DIR/fishscript_transpiler.py" "$FISH_FILE" > /dev/null 2>&1
PY_FILE="${FISH_FILE%.fish}.py"
"$PYTHON_BIN" "$PY_FILE"
rm -f "$PY_FILE"