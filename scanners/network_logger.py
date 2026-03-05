import os
from datetime import datetime

addresses = ["23.1.35.132", "184.31.10.133", "8.8.8.8"]

# Відкриваємо файл для запису логів (режим 'a' - append, додавання в кінець)
with open("network_test.log", "a") as log_file:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file.write(f"\n--- Перевірка за {current_time} ---\n")
    
    for ip in addresses:
        response = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")
        if response == 0:
            status = "UP"
        else:
            status = "DOWN"
        
        log_entry = f"IP: {ip} | Status: {status}\n"
        print(log_entry.strip()) # Виводимо на екран
        log_file.write(log_entry) # Записуємо у файл