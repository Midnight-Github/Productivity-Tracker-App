# Productivity Tracker App

## Note
This project is currently under development.

## Overview
The Productivity Tracker App is a command-based tool designed to help users track time spent on various activities and generate reports and analyses. It provides features for a multi-user system with simple password authentication, time tracking, and built-in variations of the Pomodoro technique. A gui-based version of the app is also available.

## Features
- **User Authentication**:
  - Register a new account.
  - Login and logout functionality.
  - Delete an account securely.

- **Task Management**:
  - Add tasks and sub-tasks in a hierarchical order.
  - Remove tasks.
  - Rename tasks.
  - Update time spent on tasks.

- **Time Tracking (Planned)**:
  - Track time spent on tasks.
  - Generate reports and analytics for time spent on each task.

- **Pomodoro Variants (Planned)**:
  - **Pomodoro**: Traditional time management technique. Uses a timer to break work into intervals, typically 25 minutes long, followed by short breaks
  - **Flomodoro**: A flexible version of the Pomodoro technique. Users can work for any duration with the timer, and the break time will be calculated dynamically based on the work period.
  - **Daymodoro**: A unique Pomodoro variant exclusive to this app. The total work time and break time are fixed, typically in a 5:1 ratio, allowing users to alternate between the two modes.

## Commands
### Authentication Commands
- `login <username> <password>`: Login to your account.
- `register <username> <password>`: Register a new account.
- `logout`: Logout from the current account.
- `delete`: Delete the current account.

### Task Management Commands
- `tracker add task <location>`: Add a new task to the specified location.
- `tracker remove task <location>`: Remove a task from the specified location.
- `tracker update time <location> <time>`: UPdate the time spent on a task to the give value.
- `tracker rename task <initial_location> <new_location>`: Rename a task.

### Other Commands
- `help (<command>)`: Show help for a specific command. If no command is provided, list all available commands.
- `quit`: Exit the application.

## How to Run
1. Clone the repository:
   ```bash
   git clone -b no-gui https://github.com/Midnight-Github/Productivity-Tracker-App.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Productivity-Tracker-App
   ```
3. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   py src/main.py
   ```

## Project Structure
```
Productivity-Tracker-App/
│
├── src/
│   ├── main.py                # Entry point of the application
│   ├── command/
│   │   ├── auth.py            # Handles user authentication
│   │   ├── help.py            # Provides help and usage instructions
│   │   ├── tracker.py         # Manages task-related operations
│   ├── module/
│   │   ├── json_handler.py    # Handles JSON file operations
│   │   ├── state.py           # Reserved for application state management
│   └── data/
│       ├── accounts.json      # Stores user account data
│       ├── current_user.json  # Stores the currently logged-in user data
│
├── README.md                  # Documentation for the project
├── requirements.txt           # Python dependencies
└── LICENSE                    # License for the project
```

## Dependencies
- Python 3.10 or higher
- `bcrypt` for password hashing

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve the app.

## License (todo)
This project is licensed under the MIT License. See the `LICENSE` file for details.
