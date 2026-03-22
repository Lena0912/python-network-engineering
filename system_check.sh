#!/bin/bash
echo "---SYSTEM CHECK REPORT ---" > report.txt
echo "Date and Time: $(date)" > report.txt
echo -e "\n--- DISK SPACE ---" >> report.txt
df -h >> report.txt
echo -e "\n--- TOP 5 MEMORY PROCESSES ---" >> report.txt
ps -aux --sort=-%mem | head -n 6 >> report.txt
echo "The report is ready! Check the file report.txt"
echo -e "\n--- TOP 10 LARGEST DIRECTORIES ON D: ---" >> report.txt
du -h /mnt/d --max-depth=1 2>/dev/null | sort -hr | head -n 10 >> report.txt
echo -e "\n--- TOP 10 LARGEST DIRECTORIES ON C: ---" >> report.txt
du -h /mnt/c --max-depth=1 2>/dev/null | sort -hr | head -n 10 >> report.txt
