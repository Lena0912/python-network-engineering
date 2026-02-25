#!/bin/bash
echo "--- Запуск повної перевірки системи ---"
./check_site.sh
grep "ERROR" server.log > errors_only.txt
python3 analyzer.py
echo "--- Перевірка завершена! Результати у final_report.txt ---"
