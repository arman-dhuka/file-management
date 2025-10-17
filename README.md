# File Management Utility

A simple Python-based file management tool that helps you create, view, read, edit, and delete files directly from the command line.

---

## 📁 Repository Structure

.
├── app.py
└── sample.txt

yaml
Copy code

- `app.py` — the main Python script that contains all file management functions  
- `sample.txt` — a sample file (used for testing or demonstration)  

---

## 🔧 Features

- Create new files  
- View all files in the current folder  
- Read the content of a file  
- Append new content to a file  
- Delete a file  

---

## 🚀 Usage

1. Clone or download the repository:  
   ```bash
   git clone https://github.com/arman-dhuka/file-management.git
   cd file-management
Run the Python script:

bash
Copy code
python app.py
(If you are using Python 3, use python3 app.py instead)

Choose an option from the menu (1–5) and follow the on-screen instructions to enter file names or content as required.

⚙️ Function Overview (from app.py)
Function	Description
creat_file(file_name)	Creates a new file if it doesn’t already exist
view_all_file()	Displays all files in the current directory
read_file(file_name)	Prints the contents of a specified file
edit_file(file_name)	Appends new content to the specified file
delet_file(file_name)	Deletes the specified file

🛠️ Error Handling / Edge Cases
Displays a clear message if you try to create a file that already exists

Handles “file not found” errors when trying to read, edit, or delete a missing file

General exceptions are caught to prevent program crashes

📝 Suggestions / Future Improvements
Add directory path support (manage files inside subfolders)

Add an overwrite option (not just append)

Confirmation prompt before deleting files

Improve error messages for better user experience

Add logging for actions and errors

Create a GUI front-end (Tkinter or web-based)

Write unit tests for better reliability

👤 Author
Arman Dhuka
