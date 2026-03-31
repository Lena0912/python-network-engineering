#!/bin/bash

echo "=== SYSTEM SECURITY AUDIT START ==="
date

# 1. Перевірка: Хто зараз у системі? (Who is logged in)
echo -e "\n[1] Currently logged in users:"
who

# 2. Перевірка: Відкриті порти (Network Analysis)
echo -e "\n[2] Listening network ports:"
ss -tulpn | grep LISTEN

# 3. Перевірка: Останні невдалі входи (Failed Logins)
echo -e "\n[3] Recent failed login attempts:"
# На багатьох системах це файл /var/log/auth.log або через journalctl
journalctl -t sshd --since "24 hours ago" | grep -i "failed" | tail -n 5

echo -e "\n=== AUDIT COMPLETE ==="
