# Read existing folders from folderList.txt
input("Make sure that you inserted the folder into the right directory. \n Make sure you named the file you want to show up as thumbnail '1.jpg'.\n Press Enter to proceed")
existing_folders = set()
with open('folderList.txt', 'r') as file:
    existing_folders = set(file.read().splitlines())

# Scan folders in the same directory as the script
import os
current_folders = {folder for folder in os.listdir() if os.path.isdir(folder)}

# Compare and print missing folders
missing_folders = current_folders - existing_folders

# Generate JS code for missing folder and files
js_code = ""
for folder in missing_folders:
    js_code += f'//folder title\n"{folder}"\n: [\n//folder content\n'
    folder_content = os.listdir(folder)
    for file in folder_content:
        js_code += f'"{folder}/{file}",\n'
    js_code += '],\n'

# Generate HTML code for the missing folders
html_code = ""
for folder in missing_folders:
    html_code += f"<li class=\"album-tile\">\n"
    html_code += f"<img class=\"album-thumbnail\" src=\"{folder}/1.jpg\" alt=\"{folder}\">\n"
    html_code += f"<div class=\"album-title\">{folder}</div>\n"
    html_code += f"</li>\n"

# Read the contents of script.js
with open('script.js', 'r') as js_file:
    js_contents = js_file.readlines()

# Insert JS code at line 8
js_contents.insert(7, js_code)

# Write the modified JS contents back to script.js
with open('script.js', 'w') as js_file:
    js_file.writelines(js_contents)

# Read the contents of index.html
with open('index.html', 'r') as html_file:
    html_contents = html_file.readlines()

# Insert HTML code at line 22
html_contents.insert(21, html_code)

# Write the modified HTML contents back to index.html
with open('index.html', 'w') as html_file:
    html_file.writelines(html_contents)

# Append missing folder names to folderList.txt
with open('folderList.txt', 'a') as folder_list_file:
    for folder in missing_folders:
        folder_list_file.write(f"{folder}\n")

# Wait for user input before exiting
input("Done. Press Enter to exit")
