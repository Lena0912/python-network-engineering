servers = [
    {"name": "Web-Portal", "status": "UP"},
    {"name": "Database", "status": "UP"},
    {"name": "Auth-Service", "status": "DOWN"},
    {"name": "Payment-Gateway", "status": "DOWN"},
    {"name": "Storage", "status": "UP"}
]

total_servers = len(servers) # Рахуємо загальну кількість
up_count = 0

for s in servers:
    if s["status"] == "UP":
        up_count += 1

# Рахуємо відсоток
uptime_percent = (up_count / total_servers) * 100

print(f"Загальна кількість серверів: {total_servers}")
print(f"Працює: {up_count}")
print(f"Uptime інфраструктури: {uptime_percent}%")

if uptime_percent < 80:
    print("!!! КРИТИЧНО: Рівень доступності нижче норми!")

report_message = f"""
--- INFRASTRUCTURE REPORT ---
Date: 2026-03-07
Total Servers: {total_servers}
Working: {up_count}
Uptime: {uptime_percent}%
Status: {"CRITICAL" if uptime_percent < 80 else "STABLE"}
-----------------------------
"""

# Записуємо у файл
with open("infrastructure_report.txt", "w") as f:
    f.write(report_message)

print("Звіт згенеровано у файл infrastructure_report.txt")