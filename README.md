# Linux & Bash Automation Journey 🚀

This repository contains my practical work and scripts developed while learning Linux system administration and Bash scripting as part of my **Cloud Support Engineer** training.

## 🛠 Project: System Health Check Script
The core of this repository is a Bash script (`health_check.sh`) designed to automate routine server monitoring tasks.

### Features:
* **Disk Usage Monitoring**: Tracks available space on the root partition.
* **Memory Analysis**: Reports real-time RAM usage in Megabytes.
* **Network Connectivity**: Automatically pings external services (Google) to verify internet access.
* **Timestamping**: Every report is generated with a precise system date and time.
* Automated Backup & Retention: A dedicated script (backup.sh) that creates compressed archives and automatically deletes files older than 7 days to manage disk space.
* Error Handling & Validation: Scripts now include logic to verify directory existence and handle potential execution errors using if/else statements. 

## 🧠 Skills Acquired
During this module, I have mastered the following concepts:
* **File System Navigation**: Managing directories and files via CLI (`cd`, `ls`, `cp`, `mv`).
* **Permissions & Security**: Implementing the principle of least privilege using `chmod` (e.g., `600` for secrets, `+x` for execution).
* **Data Processing**: Using pipes (`|`) and filters (`grep`, `wc`) to analyze logs and system outputs.
* **Resource Troubleshooting**: Monitoring system health with `df -h`, `free -m`, and `neofetch`.
* **Networking Basics**: Diagnosing connectivity using `ifconfig` and `ping`.
* **Version Control**: Managing code lifecycle with Git and GitHub.
* Scripting Logic: Implementing conditional statements (if/then/else) and exit codes for robust automation.
* Data Lifecycle Management: Using the find utility with -mtime parameters to implement data retention policies.
* Advanced Git Workflow: Managing remote synchronization, resolving merge conflicts, and maintaining a clean commit history.


  🕒 Automation & Backup Systems
Cron Scheduling: Mastered the crontab syntax (m h dom mon dow command) to schedule recurring system tasks.

Bash Scripting: Developed a robust backup script utilizing variables and command substitution.

Data Compression: Integrated the tar utility with gzip compression (-czf) to optimize storage and manage backups efficiently.

## 🛠 Project: Advanced System Scan & Disk Cleanup
A second script (`system_check.sh`) focused on deep diagnostic and storage optimization.

### Features:
* **Deep Disk Scan:** Analyzes mounted Windows drives (`/mnt/c`, `/mnt/d`) in WSL to find storage bottlenecks.
* **Top 10 Directory Analysis:** Automatically identifies the largest folders to suggest cleanup candidates.
* **Memory-Intensive Processes:** Uses `ps` with custom sorting to find the top 5 "RAM eaters".
* **Automated Reporting:** Generates a structured `report.txt` for incident analysis.

### Skills Demonstrated:
* **Storage Analysis:** Advanced use of `du`, `sort -hr`, and `head`.
* **Process Management:** Monitoring system load via `htop` and `ps`.
* **WSL Interoperability:** Handling file system differences between Linux and Windows.

## 📊 SQL Skills & Data Analysis
I use SQL to investigate system incidents and generate operational reports.
* **Complex Joins:** Connecting user data with incident logs.
* **Filtering & Aggregation:** Analyzing service uptime and priority distributions.
* **Practice:** Check my [SQL Practice Folder](./sql-practice/) for code examples.
