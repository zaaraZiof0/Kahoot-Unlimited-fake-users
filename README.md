# Kahoot Bot Army

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](#license)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](#)

A scalable, human-like Kahoot bot army built with Selenium and Python. Automate joining Kahoot games for educational or testing purposes.

---

## Table of Contents

- [📖 Overview](#-overview)  
- [🚀 Features](#-features)  
- [⚙️ Prerequisites](#️-prerequisites)  
- [💾 Installation](#-installation)  
- [📝 Configuration](#-configuration)  
- [🚀 Usage](#-usage)  
- [👥 Contributing](#-contributing)  
- [⚖️ License](#️-license)  
- [❗ Disclaimer](#-disclaimer)  

---

## 📖 Overview

This repository contains a multi-threaded Python script that uses Selenium to simulate multiple players joining a Kahoot game. Each bot exhibits human-like typing and random delays, helping you test Kahoot quizzes at scale.

## 🚀 Features

- **Human-like Behavior**: Random delays and typing patterns to mimic real users.  
- **Threaded Execution**: Launch 1–50 bots concurrently.  
- **Headless Mode**: Option to run Chrome in headless mode for CI integration.  
- **Anti-Detection**: Custom user-agents and Chrome options to minimize Selenium detection.  
- **Configurable**: Easily adjust pin, bot count, base name, and headless mode.

## ⚙️ Prerequisites

- **Python 3.8+**  
- **Google Chrome** installed  
- **pip** package manager

## 💾 Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/<your-username>/kahoot-bot-army.git
   cd kahoot-bot-army
   ```

2. **Create and activate a virtual environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate   # Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

## 📝 Configuration

- **Kahoot PIN**: Six-digit game PIN.  
- **Number of Bots**: Choose between 1 and 50 (default 20 if not confirmed).  
- **Base Name**: Prefix for bot names (e.g., `Student 1`, `Student 2`).  
- **Headless Mode**: Run Chrome in background (y/n).

All settings are prompted at runtime.

## 🚀 Usage

```bash
python kahoot_bot.py
```

1. Read the warning and press **Enter**.  
2. Enter the **6-digit PIN**.  
3. Enter the **number of bots**.  
4. Specify the **base name** and **headless** mode.  
5. Watch your bots join the game!

## 👥 Contributing

Contributions are welcome! Please:

1. Fork the repository  
2. Create a feature branch (`git checkout -b feature/YourFeature`)  
3. Commit your changes (`git commit -m 'Add YourFeature'`)  
4. Push to branch (`git push origin feature/YourFeature`)  
5. Open a Pull Request

## ⚖️ License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## ❗ Disclaimer

This tool is for **educational purposes only**.  
Using it may violate Kahoot’s Terms of Service.  
Excessive botting can lead to account bans.  
