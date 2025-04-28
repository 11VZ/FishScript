# FishScript

FishScript is a custom programming language inspired by Java and Python. It is designed for simplicity, readability, and extensibility, and compiles to Python for execution.

---

## Installation

### Windows
1. **Download all FishScript files** (including `install_fishscript.bat`) to a folder of your choice (e.g., `C:\FishScript`).
2. **Run the installer:**
   - Double-click `install_fishscript.bat` **OR** run it from Command Prompt:
     ```
     install_fishscript.bat
     ```
3. **Restart your terminal** (Command Prompt or PowerShell) to update your PATH.
4. You can now run FishScript files from anywhere using:
   ```
   fish myscript.fish
   ```

---

### Mac/Linux
1. **Download all FishScript files** (including `install_fishscript.sh` and the `fish` launcher) to a folder (e.g., `~/FishScript`).
2. **Make the launcher executable:**
   ```bash
   chmod +x fish
   ```
3. **Run the installer:**
   ```bash
   bash install_fishscript.sh
   ```
4. **Restart your terminal** (or run `source ~/.bashrc` or `source ~/.zshrc`) to update your PATH.
5. You can now run FishScript files from anywhere using:
   ```bash
   fish myscript.fish
   ```

---

## Usage
- Write your FishScript code in files ending with `.fish`.
- Run them with the `fish` command as shown above.
- For language features and examples, see `FISHSCRIPT_DOCS.md`.

---

## Troubleshooting
- **Python required:** FishScript requires Python 3 to be installed and available in your PATH.
- **PATH not updated?** If `fish` is not recognized, ensure you restarted your terminal after running the installer.
- **Permission denied (Mac/Linux)?** Make sure the `fish` launcher is executable: `chmod +x fish`.

---

## Uninstallation
- Remove the FishScript directory from your PATH (edit your environment variables or shell config).

---

## More
- For language reference and examples, see `FISHSCRIPT_DOCS.md`.
- For issues or contributions, visit the FishScript repository.
