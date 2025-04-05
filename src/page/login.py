import customtkinter as ctk
import tkinter as tk
from module.json_handler import accounts_json_handler, current_user_json_handler
import bcrypt

class Login(ctk.CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.root = root

        self.login_frame = ctk.CTkFrame(self, width=320, height=380)
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.heading_label = ctk.CTkLabel(self.login_frame, text="Log Into Account", font=('Century Gothic', 25))
        self.heading_label.place(x=50, y=45)

        self.error_label = ctk.CTkLabel(self.login_frame, text="", font=('Century Gothic', 12), text_color="red")
        self.error_label.place(relx=0.5, y=90, anchor=tk.CENTER)

        self.username_entry = ctk.CTkEntry(self.login_frame, width=220, placeholder_text="Username")
        self.username_entry.place(x=50, y=110)

        self.password_entry = ctk.CTkEntry(self.login_frame, width=220, placeholder_text="Password", show="*")
        self.password_entry.place(x=50, y=150)

        self.show_password_var = ctk.BooleanVar()
        self.show_password = ctk.CTkCheckBox(self.login_frame, text="Show Password", font=('Century Gothic', 12), 
            checkbox_height=12, checkbox_width=12, border_width=1, command=self.toggleShowPassword, 
            variable=self.show_password_var)
        self.show_password.place(x=60, y=190)

        self.login_button = ctk.CTkButton(self.login_frame, width=100, text="Login", corner_radius=6, 
            fg_color="#3498db", text_color="#ffffff", hover_color="#2980b9", command=self.loginAccount)
        self.login_button.place(x=110, y=270)

        self.create_account_label = ctk.CTkLabel(self.login_frame, text="Create an account?", 
            font=('Century Gothic', 10))
        self.create_account_label.place(x=210, y=350)
        self.create_account_label.bind("<Enter>", 
            command=lambda event: self.create_account_label.configure(cursor="hand2"))
        self.create_account_label.bind("<Leave>", 
            command=lambda event: self.create_account_label.configure(cursor="arrow"))
        self.create_account_label.bind("<Button-1>", 
            command=self.showSignupPage)

    def showSignupPage(self, event):
        self.root.reinitPage("Signup")
        self.root.showPage("Signup")

    def toggleShowPassword(self):
        if self.show_password_var.get():
            self.password_entry.configure(show="")
            return

        self.password_entry.configure(show="*")

    def checkUserExist(self, username):
        accounts = accounts_json_handler.data

        if not accounts:
            return False

        for account in accounts:
            if account["username"] == username:
                return True
        return False

    def checkPassword(self, username, password):
        accounts = accounts_json_handler.data
        for account in accounts:
            if account["username"] == username and account["password"] == password:
                return True
        return False

    def authenticateUser(self, username, password):
        if username == "" or password == "":
            self.error_label.configure(text="Please fill in all fields")
            return False

        if not self.checkUserExist(username):
            self.error_label.configure(text="User does not exist")
            return False

        if not self.checkPassword(username, password):
            self.error_label.configure(text="Incorrect Password")
            return False

        return True

    def loginAccount(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not self.authenticateUser(username, password):
            return

        current_user_json_handler.data["username"] = username # pyright: ignore
        current_user_json_handler.data["auto_login"] = False
        current_user_json_handler.dump()

        self.root.reinitPage("Home")
        self.root.showPage("Home")