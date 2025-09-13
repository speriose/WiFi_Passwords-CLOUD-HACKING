# Wi-Fi and System Information Extractor

## Overview
This Python project is a **Windows-based utility** designed to extract Wi-Fi profiles and their associated keys from a system, along with basic system network information, and send the results via email. The tool is intended for **educational purposes** and personal use, such as retrieving your own saved Wi-Fi credentials or monitoring your network setup.

> ⚠️ **Important:** This script accesses sensitive information like Wi-Fi passwords. Only run this on devices you own or have explicit permission to test. Unauthorized access to other networks is illegal and unethical.

---

## Features

- **Retrieve Saved Wi-Fi Profiles**  
  Uses Windows `netsh` commands to list all stored Wi-Fi profiles on the machine.

- **Extract Wi-Fi Keys**  
  Extracts the cleartext Wi-Fi keys for all saved profiles on the system.

- **System Network Information**  
  Captures the output of the `ipconfig` command to provide information about active network interfaces, IP addresses, and subnet masks.

- **Email Notification**  
  Sends all collected information to a specified email address using Gmail’s SMTP server.

---

## How It Works

1. The script runs `netsh wlan show profiles` to identify all Wi-Fi profiles stored on the system.
2. For each profile, it retrieves the Wi-Fi key using `netsh wlan show profile <profile_name> key=clear`.
3. It runs `ipconfig` to collect current network configuration.
4. All the collected information is compiled into a message and sent via SMTP to a specified email address.

---

## Requirements

- Python 3.x
- Windows OS (requires `netsh` command)
- Internet access for sending emails
- Gmail account with an **App Password** (recommended for security instead of using the account password)

---

## Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/wifi-system-info.git
cd wifi-system-info
