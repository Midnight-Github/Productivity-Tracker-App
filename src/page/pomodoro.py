import customtkinter as ctk

class Pomodoro(ctk.CTkFrame):
    def __init__(self, root):
        super().__init__(root)

        self.root = root