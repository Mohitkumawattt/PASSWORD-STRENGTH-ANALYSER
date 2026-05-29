import re
import hashlib
import os
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

HISTORY_FILE = "password_hashes.dat"
LOG_FILE = "password_history.txt"

def load_password_history():
    hashes = set()
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            for line in f:
                stripped = line.strip()
                if stripped:
                    hashes.add(stripped)
    return hashes

def save_password_hash(pwd_hash):
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"{pwd_hash}\n")

password_history = load_password_history()

def calculate_crack_time(password, score):
    length = len(password)
    if length == 0:
        return "Instant"
    if score <= 1:
        return "Few Seconds"
    elif score == 2:
        return "A few minutes to Hours"
    elif score == 3:
        return "Days to Months"
    elif score == 4:
        return "Several Years"
    else:
        if length >= 14:
            return "Trillions of Years 🔥"
        return "Hundreds to Thousands of Years"

def check_password_strength(password):
    score = 0
    length = len(password)
    
    has_lower = bool(re.search(r'[a-z]', password))
    has_upper = bool(re.search(r'[A-Z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]', password))
    
    if length >= 8:
        score += 1
        
    if has_lower: score += 1
    if has_upper: score += 1
    if has_digit: score += 1
    if has_special: score += 1
    
    if score > 5: score = 5
    
    if score == 5: strength = "VERY STRONG PASSWORD"
    elif score >= 4: strength = "STRONG PASSWORD"
    elif score >= 3: strength = "MEDIUM PASSWORD"
    else: strength = "WEAK PASSWORD"
    
    return {
        "strength": strength, "score": score, "length": length,
        "lower": has_lower, "upper": has_upper, "digit": has_digit, "special": has_special
    }

def toggle_password():
    if password_entry.cget('show') == '*':
        password_entry.config(show='')
        show_btn.config(text="Hide Password")
    else:
        password_entry.config(show='*')
        show_btn.config(text="Show Password")

def analyze_password_gui():
    global password_history
    password = password_entry.get()
    
    if not password:
        messagebox.showwarning("Empty Input", "Please enter a password first!")
        return
        
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    if password_hash in password_history:
        messagebox.showerror("Security Rule", "🚨 This password has already been scanned/used!\nPlease create a fresh, unique password.")
        return
        
    res = check_password_strength(password)
    crack_time = calculate_crack_time(password, res['score'])
    
    output_text.config(state=tk.NORMAL)
    output_text.delete('1.0', tk.END)
    
    report = "----- PASSWORD ANALYSIS -----\n\n"
    report += f"{'✔ Good Password Length' if res['length'] >= 8 else '✘ Password Too Short'} ({res['length']} chars)\n"
    report += f"{'✔ Uppercase Letter Found' if res['upper'] else '✘ No Uppercase Letter'}\n"
    report += f"{'✔ Lowercase Letter Found' if res['lower'] else '✘ No Lowercase Letter'}\n"
    report += f"{'✔ Number Found' if res['digit'] else '✘ No Number'}\n"
    report += f"{'✔ Special Character Found' if res['special'] else '✘ No Special Character'}\n"
    report += "common_passwords.txt file not found\n\n"
    
    report += "----- RESULT -----\n\n"
    report += f"Password Score: {res['score']} / 5\n"
    report += f"{res['strength']}\n"
    report += f"Estimated Crack Time: {crack_time}\n\n"
    
    report += "SHA-256 HASH:\n"
    report += f"{password_hash}\n"
    
    output_text.insert(tk.END, report)
    output_text.config(state=tk.DISABLED)
    
    password_history.add(password_hash)
    save_password_hash(password_hash)
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Score: {res['score']}/5 | {res['strength']}\n")

# --- UI Setup (Perfect Window Adjustments) ---
root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("800x700")  # Window size to support nice screen width layout
root.configure(bg="#1E1E1E")

title_label = tk.Label(root, text="Password Strength Analyzer", font=("Arial", 22, "bold"), fg="white", bg="#1E1E1E")
title_label.pack(pady=(25, 10))

sub_label = tk.Label(root, text="Enter Password", font=("Arial", 12), fg="white", bg="#1E1E1E")
sub_label.pack(pady=5)

password_entry = tk.Entry(root, font=("Arial", 14), width=45, show="*", bd=0, highlightthickness=1)
password_entry.pack(pady=5)

show_btn = tk.Button(root, text="Show Password", font=("Arial", 10, "bold"), fg="white", bg="#1E73BE", bd=0, padx=10, pady=5, command=toggle_password)
show_btn.pack(pady=10)

analyze_btn = tk.Button(root, text="Analyze Password", font=("Arial", 12, "bold"), fg="white", bg="#4CAF50", bd=0, padx=15, pady=8, command=analyze_password_gui)
analyze_btn.pack(pady=10)

# Exact Fix-Sized Screen Frame in Middle with Dark Space around it
output_frame = tk.Frame(root, bg="white", width=550, height=350)
output_frame.pack(pady=20, padx=40)
output_frame.pack_propagate(False) # Prevents the frame from shrinking/expanding

# Text Display Widget inside the fixed white canvas
output_text = tk.Text(output_frame, font=("Arial", 11), bg="white", fg="black", bd=0, wrap=tk.WORD, state=tk.DISABLED)
output_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

root.mainloop()
