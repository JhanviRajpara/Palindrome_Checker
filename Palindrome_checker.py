import tkinter as tk
from tkinter import messagebox

class PalindromeChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("Palindrome Checker")
        self.root.geometry("400x200")

        # Label and entry for input text
        tk.Label(root, text="Enter a word or phrase:", font=("Arial", 14)).pack(pady=10)
        self.input_entry = tk.Entry(root, font=("Arial", 14), width=30)
        self.input_entry.pack(pady=5)

        # Check button
        check_button = tk.Button(root, text="Check Palindrome", font=("Arial", 14), command=self.check_palindrome)
        check_button.pack(pady=20)

        # Label to display result
        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

    def check_palindrome(self):
        # Get and clean input
        text = self.input_entry.get()
        cleaned_text = ''.join(char.lower() for char in text if char.isalnum())

        # Check if cleaned text is a palindrome
        if cleaned_text == cleaned_text[::-1]:
            self.result_label.config(text=f"'{text}' is a palindrome!", fg="green")
        else:
            self.result_label.config(text=f"'{text}' is not a palindrome.", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = PalindromeChecker(root)
    root.mainloop()
