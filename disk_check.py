import shutil

# Шлях до диска (у WSL диски Windows знаходяться в /mnt/)
disk_path = "/mnt/d"

# Отримуємо статистику (total, used, free)
total, used, free = shutil.disk_usage(disk_path)

# Переводимо байти в Гігабайти для зручності
gb = 1024**3 # 1 GB = 1024 * 1024 * 1024 байт

print(f"--- Python Disk Monitor ---")
print(f"Directory: {disk_path}")
print(f"Total space: {total // gb} GB")
print(f"Used space: {used // gb} GB")
print(f"Free space: {free // gb} GB")

# Додаємо логіку "Попередження"
percent_used = (used / total) * 100
if percent_used > 80:
    print("⚠️ WARNING: Disk usage is high!")
else:
    print("✅ Disk space is okay.")
