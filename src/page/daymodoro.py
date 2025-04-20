import customtkinter as ctk
import time

class Daymodoro(ctk.CTkFrame):
    def __init__(self, root):
        super().__init__(root)

        self.root = root

        self.centre_frame = ctk.CTkFrame(self, width=400, height=600, fg_color="white")
        self.centre_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.header_frame = ctk.CTkFrame(self.centre_frame, width=390, height=100)
        self.header_frame.place(relx=0.5, y=55, anchor="center")

        self.header_text_label = ctk.CTkLabel(self.header_frame, text="Daymodoro", font=("Arial", 30))
        self.header_text_label.place(relx=0.5, rely=0.5, anchor="center")

        self.description_text_label = ctk.CTkLabel(self.header_frame, text="stay productive", font=("Arial", 12), 
            text_color="gray")
        self.description_text_label.place(relx=0.5, rely=0.8, anchor="w")

        self.timer_frame = ctk.CTkFrame(self.centre_frame, width=390, height=300)
        self.timer_frame.place(relx=0.5, y=260, anchor="center")

        # Work timer
        self.work_timer_frame = ctk.CTkFrame(self.timer_frame, width=400, height=300, fg_color="transparent")
        self.work_timer_frame.place(x=60, y=45, anchor="center")

        self.work_text_label = ctk.CTkLabel(self.work_timer_frame, text="Total Work", font=("Arial", 12), 
            text_color="gray")
        self.work_text_label.grid(row=0, column=0, pady=(10, 0))

        self.work_timer_label = ctk.CTkLabel(self.work_timer_frame, text="24:00:00", font=("Arial", 24), 
            text_color="gray")
        self.work_timer_label.grid(row=1, column=0)

        self.work_timer_progressbar = ctk.CTkProgressBar(self.work_timer_frame, width=90, height=5)
        self.work_timer_progressbar.grid(row=2, column=0, pady=(0, 20))
        self.work_timer_progressbar.set(0)

        # session counter
        # self.

        # Break timer
        self.break_timer_frame = ctk.CTkFrame(self.timer_frame, width=400, height=300, fg_color="transparent")
        self.break_timer_frame.place(x=330, y=45, anchor="center")

        self.break_text_label = ctk.CTkLabel(self.break_timer_frame, text="Total Break", font=("Arial", 12), 
            text_color="gray")
        self.break_text_label.grid(row=0, column=0, pady=(10, 0))

        self.break_timer_label = ctk.CTkLabel(self.break_timer_frame, text="00:00:00", font=("Arial", 24), 
            text_color="gray")
        self.break_timer_label.grid(row=1, column=0)

        self.break_timer_progressbar = ctk.CTkProgressBar(self.break_timer_frame, width=90, height=5)
        self.break_timer_progressbar.grid(row=2, column=0, pady=(0, 20))
        self.break_timer_progressbar.set(0)

        # Section timer
        self.timer_running = False
        self.timer_state_var = ctk.StringVar(value="Work")

        self.section_timer_frame = ctk.CTkFrame(self.timer_frame, width=400, height=200, fg_color="transparent")
        self.section_timer_frame.place(x=195, y=160, anchor="center")

        self.section_text_label = ctk.CTkLabel(self.section_timer_frame, font=("Arial", 20), 
            textvariable=self.timer_state_var, text_color="gray80")
        self.section_text_label.grid(row=1, column=0, pady=(20, 0))

        self.section_timer_label = ctk.CTkLabel(self.section_timer_frame, text="00:00:00", font=("Arial", 70), 
            text_color="gray80")
        self.section_timer_label.grid(row=2, column=0)

        self.section_timer_progressbar = ctk.CTkProgressBar(self.section_timer_frame, width=265, height=10)
        self.section_timer_progressbar.grid(row=3, column=0, pady=(0, 10))
        self.section_timer_progressbar.set(0)

        # Set the countdown durations
        # self.total_work_duration = 24 * 3600  # 24 hours in seconds
        # self.total_break_duration = 8 * 3600  # 8 hours in seconds
        # self.work_end_time = time.time() + self.total_work_duration
        # self.break_end_time = time.time() + self.total_break_duration

        # # Start updating timers
        # self.update_timer(self.work_timer_label, self.work_timer_progressbar, self.total_work_duration, self.work_end_time)
        # self.update_timer(self.break_timer_label, self.break_timer_progressbar, self.total_break_duration, self.break_end_time)

    def update_timer(self, timer_label, progressbar, total_duration, end_time):
        # Calculate remaining time
        remaining_time = int(end_time - time.time())
        
        if remaining_time > 0:
            # Calculate hours, minutes, and seconds
            hours, remainder = divmod(remaining_time, 3600)
            minutes, seconds = divmod(remainder, 60)

            # Update the timer label
            timer_label.configure(text=f"{hours:02}:{minutes:02}:{seconds:02}")

            # Update the progress bar
            elapsed_time = total_duration - remaining_time
            progressbar.set(elapsed_time / total_duration)

            # Schedule the next update after 1 second
            self.after(1000, lambda: self.update_timer(timer_label, progressbar, total_duration, end_time))
        else:
            # When the timer reaches zero, display "00:00:00" and set progress bar to 100%
            timer_label.configure(text="00:00:00")
            progressbar.set(1)

