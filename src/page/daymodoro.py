import customtkinter as ctk
import time

class Daymodoro(ctk.CTkFrame):
    def __init__(self, root):
        super().__init__(root)

        self.root = root

        self.header_frame = ctk.CTkFrame(self, width=390, height=100)
        self.header_frame.place(relx=0.5, rely=0.2, anchor="center")

        self.header_text_label = ctk.CTkLabel(self.header_frame, text="Daymodoro", font=("Arial", 30))
        self.header_text_label.place(relx=0.5, rely=0.5, anchor="center")

        self.description_text_label = ctk.CTkLabel(self.header_frame, text="stay productive", font=("Arial", 12), 
            text_color="gray")
        self.description_text_label.place(relx=0.5, rely=0.8, anchor="w")

        self.timer_frame = ctk.CTkFrame(self, width=400, height=800)
        self.timer_frame.place(relx=0.5, rely=0.5, anchor="center")

        # work timer
        self.work_text_label = ctk.CTkLabel(self.timer_frame, text="Total Work", font=("Arial", 12), 
            text_color="gray")
        self.work_text_label.grid(row=0, column=0, padx=(0, 50), pady=(10, 0))

        self.work_timer_label = ctk.CTkLabel(self.timer_frame, text="24:00:00", font=("Arial", 24), 
            text_color="gray")
        self.work_timer_label.grid(row=1, column=0, padx=(20, 40), pady=(0, 20), sticky="w")

        # break timer
        self.break_text_label = ctk.CTkLabel(self.timer_frame, text="Total Break", font=("Arial", 12), 
            text_color="gray")
        self.break_text_label.grid(row=0, column=2, padx=(50, 0), pady=(10, 0))

        self.break_timer_label = ctk.CTkLabel(self.timer_frame, text="00:00:00", font=("Arial", 24), 
            text_color="gray")
        self.break_timer_label.grid(row=1, column=2, padx=(40, 20), pady=(0, 20), sticky="e")

        # interval timer
        self.timer_running = False
        self.timer_state_var = ctk.StringVar(value="Work")
        self.interval_text_label = ctk.CTkLabel(self.timer_frame, font=("Arial", 20), 
            textvariable=self.timer_state_var, text_color="gray80")
        self.interval_text_label.grid(row=2, column=0, padx=20, pady=(20, 0), columnspan=3)

        self.interval_timer_label = ctk.CTkLabel(self.timer_frame, text="00:00:00", font=("Arial", 70), 
            text_color="gray80")
        self.interval_timer_label.grid(row=3, column=0, padx=60, pady=(0, 10), columnspan=3)

        # Set the countdown duration (24 hours in seconds)
        self.total_duration = 24 * 3600  # 24 hours in seconds
        self.end_time = time.time() + self.total_duration  # Calculate the end time
        self.update_timer(self.work_timer_label)

        # work progress bar
        self.work_progress = ctk.CTkProgressBar(self.timer_frame, width=300)
        self.work_progress.grid(row=5, column=0, columnspan=3, pady=10)
        self.work_progress.set(0)  # Initialize progress to 0

    def update_timer(self, timer_label):
        # Calculate remaining time
        remaining_time = int(self.end_time - time.time())
        
        if remaining_time > 0:
            # Calculate hours, minutes, and seconds
            hours, remainder = divmod(remaining_time, 3600)
            minutes, seconds = divmod(remainder, 60)

            # Update the timer label
            timer_label.configure(text=f"{hours:02}:{minutes:02}:{seconds:02}")

            # Schedule the next update after 1 second
            self.after(1000, lambda: self.update_timer(timer_label))
        else:
            # When the timer reaches zero, display "00:00:00"
            timer_label.configure(text="00:00:00")

