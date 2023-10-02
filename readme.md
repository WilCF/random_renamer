# File Renaming Script

This script renames all files in the directory where the script is located, following a specific naming convention: a capital letter followed by a two-digit number, while preserving the original file extensions. The renamed files are then placed in a new folder named "new".

## Usage

1. Place the script (`rename_files.py` or whatever you've named it) in the folder containing the files you want to rename.
2. Run the script using Python:
   ```bash
   python rename_files.py
   ```
3. The script will create a new folder named "new" in the same directory. All the renamed files will be copied to this new folder, preserving the original files in their original state.

## Naming Convention

Files are renamed following this pattern: 
- A single uppercase letter (A-Z)
- Followed by a two-digit number (00-99)

For example: `A01.txt`, `B35.jpg`, `Z99.docx`, etc.

## Notes

- The script will skip renaming itself to avoid any conflicts.
- If the "new" folder already exists, the script will simply add the renamed files to it. If not, it will create the folder.
- Ensure you have the necessary permissions to read and write in the directory where the script is placed.

---
