import customtkinter as ctk
import tkinter as tk

class Signup(ctk.CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.root = root

        self.login_frame = ctk.CTkFrame(self, width=320, height=380)
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.heading_label = ctk.CTkLabel(self.login_frame, text="Create Account", font=('Century Gothic', 25))
        self.heading_label.place(x=50, y=45)

        self.error_label = ctk.CTkLabel(self.login_frame, text="", font=('Century Gothic', 12), text_color="red")
        self.error_label.place(x=25, y=80)

        self.username_entry = ctk.CTkEntry(self.login_frame, width=220, placeholder_text="Username")
        self.username_entry.place(x=50, y=110)

        self.show_password_var = ctk.BooleanVar()
        self.password_entry = ctk.CTkEntry(self.login_frame, width=220, placeholder_text="Password", show="*")
        self.password_entry.place(x=50, y=150)

        self.confirm_password_entry = ctk.CTkEntry(self.login_frame, width=220, placeholder_text="Confirm Password", show="*")
        self.confirm_password_entry.place(x=50, y=190)

        self.show_password = ctk.CTkCheckBox(self.login_frame, text="Show Password", font=('Century Gothic', 12), checkbox_height=12, checkbox_width=12, border_width=1, command=self.toggleShowPassword, variable=self.show_password_var)
        self.show_password.place(x=60, y=230)

        self.create_account_button = ctk.CTkButton(self.login_frame, width=100, text="Create", corner_radius=6, fg_color="#3498db", text_color="#ffffff", hover_color="#2980b9")
        self.create_account_button.place(x=110, y=270)

        self.create_account_label = ctk.CTkLabel(self.login_frame, text="Already have an account?", font=('Century Gothic', 10))
        self.create_account_label.place(x=178, y=350)
        self.create_account_label.bind("<Enter>", command=lambda event: self.create_account_label.configure(cursor="hand2"))
        self.create_account_label.bind("<Leave>", command=lambda event: self.create_account_label.configure(cursor="arrow"))
        self.create_account_label.bind("<Button-1>", command=self.showLoginPage)

    def showLoginPage(self, event):
        self.root.reinitPage("Login")
        self.root.showPage("Login")

    def toggleShowPassword(self):
        if self.show_password_var.get():
            self.password_entry.configure(show="")
            return

        self.password_entry.configure(show="*")