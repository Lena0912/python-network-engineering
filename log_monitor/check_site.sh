#!/bin/bash

# 1. Визначаємо адресу сайту та назву лог-файлу
URL="https://google.com"
LOG_FILE="site_report.txt"

# 2. Робимо запит до сайту (curl)
# -s (silent), -o (output to null), -w (write out status code)
STATUS=$(curl -L -s -o /dev/null -w "%{http_code}" $URL)

# 3. Умова: якщо статус 200, сайт працює. Якщо інший — є проблема.
if [ $STATUS -eq 200 ]; then
    RESULT="$(date): SUCCESS - Сайт $URL доступний (Статус $STATUS)"
else
    RESULT="$(date): ERROR - Сайт $URL недоступний (Статус $STATUS)"
fi

# 4. Виводимо результат на екран
echo $RESULT

# 5. Записуємо результат у файл (>> додає запис у кінець файлу)
echo $RESULT >> $LOG_FILE

