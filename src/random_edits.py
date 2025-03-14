import os
import random
import datetime
from git import Repo

repo_path = os.getcwd()  
repo = Repo(repo_path)

edit_folder = os.path.join(repo_path, "random_edits")
os.makedirs(edit_folder, exist_ok=True)

files = [f for f in os.listdir(edit_folder) if os.path.isfile(os.path.join(edit_folder, f))]

actions = ["create", "edit", "write", "delete"]
action = random.choice(actions)

if action == "create" or not files:
    filename = f"file_{random.randint(1000, 9999)}.txt"
    file_path = os.path.join(edit_folder, filename)
    with open(file_path, "w") as f:
        f.write(f"File created on {datetime.datetime.now()}\n")
    print(f"Created file: {filename}")

elif action == "edit":
    file_path = os.path.join(edit_folder, random.choice(files))
    with open(file_path, "a") as f:
        f.write(f"Edited on {datetime.datetime.now()}\n")
    print(f"Edited file: {file_path}")

elif action == "write":
    file_path = os.path.join(edit_folder, random.choice(files))
    with open(file_path, "a") as f:
        f.write(f"Random write on {datetime.datetime.now()}\n")
    print(f"Wrote to file: {file_path}")

elif action == "delete" and len(files) > 1:
    file_to_delete = os.path.join(edit_folder, random.choice(files))
    os.remove(file_to_delete)
    print(f"Deleted file: {file_to_delete}")

repo.git.add(edit_folder)
repo.git.commit("-m", f"Automated commit: {datetime.datetime.now()}")
repo.git.push("origin", "main")

print("Changes pushed successfully!")
