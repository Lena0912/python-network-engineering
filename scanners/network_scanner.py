import os
from datetime import datetime

servers = ["8.8.8.8", "1.1.1.1", "127.0.0.1"]

# Створюємо файл для запису звіту ('w' - write mode)
with open("scan_report.txt", "w") as file:
    file.write(f"Network Scan Report - {datetime.now()}\n")
    file.write("-" * 30 + "\n")

    for ip in servers:
        print(f"Checking {ip}...")
        exit_code = os.system(f"ping -c 1 {ip} > /dev/null")
        
        if exit_code == 0:
            status = "UP"
        else:
            status = "DOWN"
        
        # Записуємо результат у файл
        file.write(f"Server {ip} is {status}\n")

print("\n[DONE] Results saved to scan_report.txt")