from module.json_handler import current_user_json_handler
import os
import time

def addTask(location):
    if current_user_json_handler.data['username'] is None:
        print("You must be logged in to add a task.")
        return

    path_components = os.path.normpath(location).split(os.sep)
    data = current_user_json_handler.data["user_data"]["tracker"]  # pyright: ignore

    for component in path_components:
        if component not in data.keys():
            data[component] = {"time": 0}

        data = data[component]

    current_user_json_handler.dump()
    print(f"Added task '{location}'")

def removeTask(location):
    if current_user_json_handler.data['username'] is None:
        print("You must be logged in to remove a task.")
        return

    path_components = os.path.normpath(location).split(os.sep)
    data = current_user_json_handler.data["user_data"]["tracker"]  # pyright: ignore

    for component in path_components[:-1]:
        if component not in data:
            print(f"Task '{location}' does not exist.")
            return
        data = data[component]

    last_component = path_components[-1]
    if last_component in data:
        del data[last_component]
        current_user_json_handler.dump()
        print(f"Removed task '{location}'")
    else:
        print(f"Task '{location}' does not exist.")

def updateTaskTime(location, value):  # value: 'HH:MM:SS' # need to test
    if current_user_json_handler.data['username'] is None:
        print("You must be logged in to update task time.")
        return

    path_components = os.path.normpath(location).split(os.sep)
    data = current_user_json_handler.data["user_data"]["tracker"]  # pyright: ignore

    for component in path_components:
        if component not in data:
            print(f"Task '{location}' does not exist.")
            return
        data = data[component]

    try:
        parsed_time = time.strptime(value, "%H:%M:%S")
        total_seconds = parsed_time.tm_hour * 3600 + parsed_time.tm_min * 60 + parsed_time.tm_sec
    except ValueError:
        print("Invalid time format. Please use 'HH:MM:SS'.")
        return

    data["time"] = total_seconds
    current_user_json_handler.dump()
    print(f"Updated time for task '{location}' to {total_seconds} seconds.")

def renameTask(initial_location, new_name):
    if current_user_json_handler.data['username'] is None:
        print("You must be logged in to rename a task.")
        return

    path_components = os.path.normpath(initial_location).split(os.sep)
    data = current_user_json_handler.data["user_data"]["tracker"]  # pyright: ignore

    # Traverse to the parent of the task to be renamed
    for component in path_components[:-1]:
        if component not in data:
            print(f"Task '{initial_location}' does not exist.")
            return
        data = data[component]

    last_component = path_components[-1]
    if last_component in data:
        task_data = data[last_component]
        del data[last_component]

        # Add the task with the new name at the same level
        if new_name in data:
            print(f"A task with the name '{new_name}' already exists.")
            return

        data[new_name] = task_data
        current_user_json_handler.dump()
        print(f"Renamed task from '{initial_location}' to '{new_name}'")
    else:
        print(f"Task '{initial_location}' does not exist.")

def moveTask(initial_location, new_location): # broken
    if current_user_json_handler.data['username'] is None:
        print("You must be logged in to move a task.")
        return

    path_components_initial = os.path.normpath(initial_location).split(os.sep)
    path_components_new = os.path.normpath(new_location).split(os.sep)

    data = current_user_json_handler.data["user_data"]["tracker"]  # pyright: ignore

    # Traverse to the parent of the initial task
    for component in path_components_initial[:-1]:
        if component not in data:
            print(f"Task '{initial_location}' does not exist.")
            return
        data = data[component]

    last_component_initial = path_components_initial[-1]
    if last_component_initial not in data:
        print(f"Task '{initial_location}' does not exist.")
        return

    task_data = data[last_component_initial]
    del data[last_component_initial]

    # Traverse to the parent of the new location
    for component in path_components_new[:-1]:
        if component not in data:
            data[component] = {"time": 0}
        data = data[component]

    last_component_new = path_components_new[-1]
    if last_component_new in data:
        print(f"A task with the name '{new_location}' already exists.")
        return

    data[last_component_new] = task_data
    current_user_json_handler.dump()
    print(f"Moved task from '{initial_location}' to '{new_location}'")