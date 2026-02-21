# Simple Python script to practice input and variables
# This is a base for future network automation tools

print("--- Network Analysis Tool ---")

# Getting data from the user
target_name = input("Enter the device name: ")
target_ip = input("Enter the target IP address: ")

# Displaying the summary
print(f"\n[INFO] Target identified: {target_name}")
print(f"[INFO] Scanning IP: {target_ip}...")
print("Status: Success. (Demo mode)")