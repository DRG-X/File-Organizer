# 🗂️ File Organizer with Undo Feature

A Python-based file management tool that automatically sorts your messy files into organized folders — by **extension** or by **last modified time**.  
It also includes an **Undo** feature so you can easily restore files back to their original location if needed.

---

## ✨ Features
- 📁 **Sort by Extension** → Groups files by type (e.g., `.jpg`, `.pdf`, `.mp4`).  
- ⏰ **Sort by Last Modified Date** → Organizes files into Year/Month folders.  
- 🔄 **Undo Functionality** → Restores all moved files with a single command.  
- 📝 **Logging** → All operations are logged in `file_manager.log` for debugging.  
- 💾 **JSON-based History** → Tracks every move for safe undos.  

---

## 🚀 Usage
1. Clone this repo:
   ```bash
   git clone https://github.com/DRG-X/File-Organizer.git
2. Navigate to the folder: cd File-Organizer
3. Run the script: python main.py
4. Enter the folder path you want to clean.

Choose a method:

e → Sort by Extension
t → Sort by Date/Time
u → Undo all moves

📂 Example
Before:
Downloads/
  - img1.jpg
  - doc1.pdf
  - movie.mp4

After (Sort by Extension):
Downloads/Organized_Files/
  ├── jpg/
  │   └── img1.jpg
  ├── pdf/
  │   └── doc1.pdf
  └── mp4/
      └── movie.mp4


⚡ Requirements
Python 3.8+

Standard library only (no external dependencies).


Future Improvements
1. GUI for non-technical users
2. Custom rules (e.g., size-based sorting)
3. Scheduled auto-cleaning


🧑‍💻 Author
Made with ⚡ and too much coffee by Deepansh Raj Goel






