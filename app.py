import os

def creat_file(file_name):
    try:
        with open(file_name, "x") as fs:
            print(f"{file_name} file was created successfully") 
    except FileExistsError:
        print("File already exists!")
    except Exception as err:
        print(f"An error occurred: {err}")

def view_all_file():
    files = os.listdir()
    if not files:
        print("No files found!")
    else:
        print("---- Available files in folder -------")
        for file in files:
            print(file)

def delet_file(file_name):
    try:
        os.remove(file_name)
        print(f"{file_name} deleted successfully!")
    except FileNotFoundError:
        print("File not found!")
    except Exception as err:
        print(f"An error occurred: {err}")

def read_file(file_name):
    try:
        with open(file_name, "r") as fs:
            content = fs.read()
            print("------ File Content ----")
            print(content)
    except FileNotFoundError:
        print("File not found!")
    except Exception as err:
        print(f"An error occurred: {err}")

def edit_file(file_name):
    try:
        with open(file_name, "a") as fs:
            content = input("Enter your content: ")
            fs.write(content + "\n")
            print(f"Content added to {file_name} successfully!")
    except FileNotFoundError:
        print("File not found!")
    except Exception as err:
        print(f"An error occurred: {err}")

print("1. View file")
print("2. Create file")
print("3. Read file")
print("4. Edit file")
print("5. Delete file")

choise = input("Tell me your work (1-5): ")

if choise == "1":
    view_all_file()
elif choise == "2":
    file_name = input("Enter a file name: ")
    creat_file(file_name)
elif choise == "3":
    file_name = input("Enter a file name: ")
    read_file(file_name)
elif choise == "4":
    file_name = input("Enter a file name: ")
    edit_file(file_name)
elif choise == "5":
    file_name = input("Enter a file name: ")
    delet_file(file_name)
else:
    print("Something went wrong! Please choose between 1-5.")
