import customtkinter as ctk

class Settings(ctk.CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.root = root
