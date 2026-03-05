#!/bin/bash

# Створюємо масив заявок
tickets=("Low" "High" "Medium" "High" "Low")

echo "Bash розпочинає перевірку..."

for level in "${tickets[@]}"
do
    if [ "$level" == "High" ]; then
        echo "!!! Терміново: $level"
    else
        echo "Нормально: $level"
    fi
done