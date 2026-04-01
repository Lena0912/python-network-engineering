import os

def analyze():
    file_path = 'sample.log'
    if not os.path.exists(file_path):
        print("Log file not found!")
        return

    print(f"--- Searching for Issues in {file_path} ---")
    with open(file_path, 'r') as file:
        for line in file:
            if "ERROR" in line or "CRITICAL" in line:
                print(f"FOUND: {line.strip()}")

analyze()
