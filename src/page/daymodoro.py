import customtkinter as ctk
import time
from module.json_handler import user_json_handler

class Daymodoro(ctk.CTkFrame):
    def __init__(self, root):
        super().__init__(root)

        self.root = root

        self.current_user = root.current_user

        self.current_user_data = self.getCurrentUserData()

