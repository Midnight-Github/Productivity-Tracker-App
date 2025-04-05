import customtkinter as ctk
import tkinter as tk

class Signup(ctk.CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.root = root

        #Create Login FRAME
        self.login_frame = ctk.CTkFrame(master=self, width=320, height=380)
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        #TOP text
        self.text = ctk.CTkLabel(master=self.login_frame, text="Log Into Account", font=('Century Gothic', 25))
        self.text.place(x=50, y=45)

        self.error_label = ctk.CTkLabel(master=self.login_frame, text="", font=('Century Gothic', 12), text_color="red")
        self.error_label.place(x=25, y=80)

        #Username entry block
        self.u_block = ctk.CTkEntry(master=self.login_frame, width=220, placeholder_text="Username")
        self.u_block.place(x=50, y=110)

        #Password entry block
        self.show_password_var = ctk.BooleanVar()
        self.p_block = ctk.CTkEntry(master=self.login_frame, width=220, placeholder_text="Password", show="*")
        self.p_block.place(x=50, y=150)

        #checkbox for showing password
        self.show_password = ctk.CTkCheckBox(master=self.login_frame, text="Show Password", font=('Century Gothic', 12), checkbox_height=12, checkbox_width=12, border_width=1)
        self.show_password.place(x=60, y=190)

        #Forgot password text
        self.label3 = ctk.CTkLabel(master=self.login_frame, text="Create an account?", font=('Century Gothic', 10))
        self.label3.place(x=210, y=350)
        self.label3.bind("<Enter>", lambda event: self.label3.configure(cursor="hand2"))
        # Change cursor back to the default arrow when mouse leaves the widget
        self.label3.bind("<Leave>", lambda event: self.label3.configure(cursor="arrow"))
        # Bind the click event to open the Forgot Password frame
        # self.label3.bind("<Button-1>", lambda event: self.master.open_forgot_password_frame())

        #Login button
        self.login_button = ctk.CTkButton(master=self.login_frame, width=100, text="Login", corner_radius=6, fg_color="#3498db", text_color="#ffffff", hover_color="#2980b9")
        self.login_button.place(x=110, y=250)

        #Register button
        self.register_button = ctk.CTkButton(master=self.login_frame, width=100, text="Register", corner_radius=6, fg_color="#3498db", text_color="#ffffff", hover_color="#2980b9")
        self.register_button.place(x=110, y=290)

