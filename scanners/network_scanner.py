import os

# Створюємо список IP-адрес (це твої "таргети")
servers = ["8.8.8.8", "1.1.1.1", "127.0.0.1"]

print(f"--- Starting scan of {len(servers)} servers ---")

# Цикл for перебирає кожну адресу в списку
for ip in servers:
    print(f"Checking {ip}...")
    
    # Виконуємо команду ping. 
    # -c 1 (один пакет), > /dev/null (приховати технічний вивід)
    exit_code = os.system(f"ping -c 1 {ip} > /dev/null")
    
    if exit_code == 0:
        print(f"  [+] Server {ip} is ACTIVE")
    else:
        print(f"  [-] Server {ip} is DOWN")

print("--- Scan finished ---")