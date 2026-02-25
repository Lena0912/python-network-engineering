from datetime import datetime  # Імпортуємо модуль для роботи з часом

# Отримуємо поточну дату та час у гарному форматі
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

try:
    with open('errors_only.txt', 'r') as file:
        errors = file.readlines()
        count = len(errors)

    # Формуємо текст звіту
    status = "КРИТИЧНИЙ 🔴" if count > 2 else "ОК 🟢"
    report_content = (
        f"=== ЗВІТ МОНІТОРИНГУ ===\n"
        f"Час перевірки: {current_time}\n"
        f"Знайдено помилок: {count}\n"
        f"Статус системи: {status}\n"
        f"========================\n"
    )

    # 1. Виводимо в консоль для нас
    print(report_content)

    # 2. Записуємо у файл для менеджера
    with open('final_report.txt', 'a') as report_file: # 'a' означає append (додавати в кінець)
        report_file.write(report_content + "\n")
    
    print("✅ Звіт збережено у файл final_report.txt")

except FileNotFoundError:
    print("❌ Помилка: файл errors_only.txt не знайдено.")
