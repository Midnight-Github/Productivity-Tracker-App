import customtkinter as ctk
import time

class Home(ctk.CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)

        # Add a label to display the timer
        self.timer_label = ctk.CTkLabel(self, text="00:00:00", font=("Arial", 24))
        self.timer_label.grid(row=0, column=0, padx=20, pady=20)

        # Start the timer
        self.start_time = time.time()
        self.update_timer()

    def update_timer(self):
        # Calculate elapsed time
        current_time = time.time()
        elapsed_time = int(current_time - self.start_time)
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Update the timer label
        self.timer_label.configure(text=f"{hours:02}:{minutes:02}:{seconds:02}")

        # Calculate the next update interval to minimize drift
        next_update = 1000 - int((current_time - self.start_time) * 1000) % 1000
        self.after(next_update, self.update_timer)

