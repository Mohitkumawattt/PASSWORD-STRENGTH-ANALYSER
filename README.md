# 🔐 Password Strength Analyzer

A modern **Graphical User Interface (GUI)** based Password Strength Analyzer built with Python & Tkinter.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-FF6B6B?style=for-the-badge&logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Security-SHA256-00C853?style=for-the-badge)

## 📋 About the Project

**Password Strength Analyzer** is a user-friendly desktop application that helps users evaluate the strength of their passwords in real-time. It not only gives a strength score but also provides detailed feedback, estimated cracking time, and prevents password reuse using secure **SHA-256 hashing**.

This project demonstrates practical application of password security concepts, GUI development, and basic cryptography.

## ✨ Key Features

- 🖥️ **Beautiful Dark Theme GUI** with clean layout
- 🔢 Password Strength Scoring (Out of 5)
- ⏱️ **Estimated Crack Time** Calculation
- 🔐 **SHA-256 Hashing** for secure password history
- 🚫 Smart Password Reuse Detection
- 👁️ Show/Hide Password Toggle
- 📋 Complete Analysis Report
- 📁 Automatic Logging System

## 🛠️ Technologies Used

- **Python 3**
- **Tkinter** – GUI Framework
- **hashlib** – SHA-256 Hashing
- **re** – Regular Expressions
- **File Handling** – Persistent History

## 🚀 How to Run

### Prerequisites
- Python 3.8 or higher

### Installation & Run

1. Clone or download this repository
2. Open terminal in the project folder
3. Run the command:
   ``` python filename.py
   ```
Example Output
Input: MyName@2024
Output Includes:

Password Score: 4/5
Strength: STRONG PASSWORD
Estimated Crack Time: Several Years
SHA-256 Hash: a1b2c3d4e5f6...
Detailed character analysis
Security suggestions

🔐 Security Features

Uses SHA-256 cryptographic hashing to securely store password history
Never stores plain text passwords
Warns user if same password is used again
Provides practical security tips

Author
Mohit Kumawat
Passionate Learner | Cybersecurity Enthusiast

Made with ❤️ and dedication for learning Python GUI and Cybersecurity.
