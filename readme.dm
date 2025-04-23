# Productivity Tracker App

## Overview
The Productivity Tracker App is a command-line tool designed to help users manage their tasks and track time spent on various activities. It provides features for task management, user authentication, and time tracking, all in a simple and intuitive interface.

## Features
- **User Authentication**:
  - Register a new account.
  - Login and logout functionality.
  - Delete an account securely.

- **Task Management**:
  - Add tasks to specific locations.
  - Remove tasks from locations.
  - Rename tasks.
  - Reset time spent on tasks.

- **Time Tracking**:
  - Track time spent on tasks.
  - Update the timer for ongoing tasks.

- **Help System**:
  - Get detailed usage instructions for all commands.

## Commands
### Authentication Commands
- `login <username> <password>`: Login to your account.
- `register <username> <password>`: Register a new account.
- `logout`: Logout from the current account.
- `delete`: Delete the current account.

### Task Management Commands
- `tracker_add_task <location>`: Add a new task to the specified location.
- `tracker_remove_task <location>`: Remove a task from the specified location.
- `tracker_reset_time <location>`: Reset the time spent on a task.
- `tracker_rename_task <initial_location> <new_location>`: Rename a task.

### Other Commands
- `help (<command>)`: Show help for a specific command. If no command is provided, list all available commands.
- `quit`: Exit the application.

## How to Run
1. Clone the repository:
2. Navigate to the project directory:
3. Install dependencies (if any):
4. Run the application:

## File Structure

## Dependencies
- Python 3.10 or higher
- `bcrypt` for password hashing

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve the app.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.