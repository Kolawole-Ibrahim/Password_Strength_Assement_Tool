import tkinter as tk
from tkinter import messagebox
import re

def assess_password_strength(password):
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r'[A-Z]', password)),
        "lowercase": bool(re.search(r'[a-z]', password)),
        "digit": bool(re.search(r'\d', password)),
        "special": bool(re.search(r'[\W_]', password))
    }

    met_criteria = sum(criteria.values())

    if met_criteria == 5:
        strength = "Strong"
    elif met_criteria == 4:
        strength = "Medium"
    else:
        strength = "Weak"

    feedback = []
    if not criteria["length"]:
        feedback.append("Password should be at least 8 characters long.")
    if not criteria["uppercase"]:
        feedback.append("Include at least one uppercase letter.")
    if not criteria["lowercase"]:
        feedback.append("Include at least one lowercase letter.")
    if not criteria["digit"]:
        feedback.append("Include at least one digit.")
    if not criteria["special"]:
        feedback.append("Include at least one special character.")

    return strength, feedback

def check_password():
    password = password_entry.get()
    strength, feedback = assess_password_strength(password)
    feedback_msg = "\n".join(feedback)
    messagebox.showinfo("Password Strength", f"Strength: {strength}\n\nFeedback:\n{feedback_msg}")

# GUI setup
app = tk.Tk()
app.title("Password Strength Checker")

tk.Label(app, text="Enter Password:").pack(pady=10)
password_entry = tk.Entry(app, show='*', width=30)
password_entry.pack(pady=5)

check_button = tk.Button(app, text="Check Strength", command=check_password)
check_button.pack(pady=20)

app.mainloop()

