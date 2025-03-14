import os
import random
import datetime

directory = "random_files"
os.makedirs(directory, exist_ok=True)

files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

operations = ["create", "modify", "delete"]
weights = [0.6, 0.3, 0.1]
operation = random.choices(operations, weights=weights, k=1)[0]

timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if operation == "create" or not files:
    new_filename = f"file_{random.randint(1000, 9999)}.txt"
    file_path = os.path.join(directory, new_filename)
    
    with open(file_path, "w") as f:
        f.write(f"File created at {timestamp}\n")
        f.write(f"Content ID: {random.randint(10000, 99999)}\n")
    
    print(f"Created new file: {new_filename}")

elif operation == "modify" and files:
    filename = random.choice(files)
    file_path = os.path.join(directory, filename)
    
    with open(file_path, "a") as f:
        f.write(f"\nFile modified at {timestamp}\n")
        f.write(f"Modification ID: {random.randint(10000, 99999)}\n")
    
    print(f"Modified file: {filename}")

elif operation == "delete" and len(files) > 2:
    filename = random.choice(files)
    file_path = os.path.join(directory, filename)
    
    os.remove(file_path)
    print(f"Deleted file: {filename}")

else:
    new_filename = f"file_{random.randint(1000, 9999)}.txt"
    file_path = os.path.join(directory, new_filename)
    
    with open(file_path, "w") as f:
        f.write(f"Fallback file created at {timestamp}\n")
        f.write(f"Content ID: {random.randint(10000, 99999)}\n")
    
    print(f"Created fallback file: {new_filename}")

print("Operation completed successfully")