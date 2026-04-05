import customtkinter as ctk
from utils import find_pids_by_name, hide_process, reveal_process
import os

# Appearance Settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class ProcessGhostGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Process-Ghost 👻 v2.0")
        self.geometry("500x450")

        # Header
        self.label = ctk.CTkLabel(self, text="Process-Ghost Control Panel", font=("Roboto", 20, "bold"))
        self.label.pack(pady=20)

        # Process Name Input
        self.entry = ctk.CTkEntry(self, placeholder_text="Enter process name (e.g., sleep)", width=300)
        self.entry.pack(pady=10)

        # Buttons
        self.hide_button = ctk.CTkButton(self, text="GHOST IT (HIDE)", command=self.hide_action, fg_color="#E74C3C", hover_color="#C0392B")
        self.hide_button.pack(pady=10)

        self.reveal_button = ctk.CTkButton(self, text="REVEAL PROCESS", command=self.reveal_action, fg_color="#2ECC71", hover_color="#27AE60")
        self.reveal_button.pack(pady=10)

        # Log Terminal
        self.textbox = ctk.CTkTextbox(self, width=400, height=150)
        self.textbox.pack(pady=20)
        self.textbox.insert("0.0", "System Ready...\nEnsure you are running with sudo privileges.")

    def log(self, message):
        self.textbox.insert("end", f"\n> {message}")
        self.textbox.see("end")

    def hide_action(self):
        name = self.entry.get()
        pids = find_pids_by_name(name)
        if not pids:
            self.log(f"Error: Process '{name}' not found.")
            return
        for pid in pids:
            if hide_process(pid):
                self.log(f"SUCCESS: PID {pid} is now a ghost.")

    def reveal_action(self):
        name = self.entry.get()
        # Note: Since it's hidden, finding by name might fail. Using PID is safer.
        self.log(f"Attempting to reveal process: {name}")
        # Logic
