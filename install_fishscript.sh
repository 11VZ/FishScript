set -e
FISH_HOME="$(cd "$(dirname "$0")" && pwd)"

if ! echo "$PATH" | grep -q "$FISH_HOME"; then
  SHELL_RC="$HOME/.bashrc"
  [ -n "$ZSH_VERSION" ] && SHELL_RC="$HOME/.zshrc"
  echo "export PATH=\"$PATH:$FISH_HOME\"" >> "$SHELL_RC"
  echo "FishScript installed! Restart your terminal or run: source $SHELL_RC"
else
  echo "FishScript is already in your PATH!"
fi
