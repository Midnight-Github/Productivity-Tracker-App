import customtkinter as ctk
from module.json_handler import current_user_json_handler, user_data_json_handler
import time

class Home(ctk.CTkFrame):
    def __init__(self, root):
        super().__init__(root)

        self.root = root

        self.daymodoro_button = ctk.CTkButton(self, text="Daymodoro", command=lambda: self.root.showPage("Daymodoro"))
        self.daymodoro_button.grid(row=0, column=0, padx=20, pady=20)

        self.pomodoro_button = ctk.CTkButton(self, text="Pomodoro", command=lambda: self.root.showPage("Pomodoro"))
        self.pomodoro_button.grid(row=0, column=1, padx=20, pady=20)

        self.flomodoro_button = ctk.CTkButton(self, text="Flomodoro", command=lambda: self.root.showPage("Flomodoro"))
        self.flomodoro_button.grid(row=0, column=2, padx=20, pady=20)

        self.settings_button = ctk.CTkButton(self, text="Settings", command=lambda: self.root.showPage("Settings"))
        self.settings_button.grid(row=1, column=0, padx=20, pady=20)
    

