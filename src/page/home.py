import customtkinter as ctk
from module.json_handler import current_user_json_handler, user_data_json_handler
import time

class Home(ctk.CTkFrame):
    def __init__(self, root):
        super().__init__(root)

        self.current_username = current_user_json_handler.data["username"]

        self.current_user_data = self.getCurrentUserData()
        if self.current_user_data is None:
            self.createDefaultUserData()
            self.current_user_data = self.getCurrentUserData()

    def getCurrentUserData(self):
        user_data = user_data_json_handler.data

        for data in user_data:
            if self.current_username == data["username"]:
                return data
        
        return None

    def createDefaultUserData(self):
        user_data_json_handler.data.append({
            "username": self.current_username,
            "wakeup_time": 28_800, # 8:00
            "sleep_time": 82_800,  # 23:00
            "total_work_seconds": 25_200, # 7 hours
            "work_session_seconds": 1_500, # 25 minutes
            "break_session_seconds": 300, # 5 minutes
            "break_work_ratio": 0.2, # 20% break
        })
        user_data_json_handler.dump()
        


    #     # Add a label to display the timer
    #     self.timer_label = ctk.CTkLabel(self, text="24:00:00", font=("Arial", 24))
    #     self.timer_label.grid(row=0, column=0, padx=20, pady=20)

    #     # Set the countdown duration (24 hours in seconds)
    #     self.total_duration = 24 * 3600  # 24 hours in seconds
    #     self.end_time = time.time() + self.total_duration  # Calculate the end time
    #     self.update_timer()

    # def update_timer(self):
    #     # Calculate remaining time
    #     remaining_time = int(self.end_time - time.time())
        
    #     if remaining_time > 0:
    #         # Calculate hours, minutes, and seconds
    #         hours, remainder = divmod(remaining_time, 3600)
    #         minutes, seconds = divmod(remainder, 60)

    #         # Update the timer label
    #         self.timer_label.configure(text=f"{hours:02}:{minutes:02}:{seconds:02}")

    #         # Schedule the next update
    #         next_update = max(0, self.end_time - time.time())
    #         self.after(int(next_update * 1000), self.update_timer)
    #     else:
    #         # When the timer reaches zero, display "00:00:00"
    #         self.timer_label.configure(text="00:00:00")

