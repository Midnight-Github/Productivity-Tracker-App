from module.json_handler import current_user_json_handler
import os

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

def resetTaskTime(location):
    if current_user_json_handler.data['username'] is None:
        print("You must be logged in to reset task time.")
        return

    path_components = os.path.normpath(location).split(os.sep)
    data = current_user_json_handler.data["user_data"]["tracker"]  # pyright: ignore

    for component in path_components:
        if component not in data:
            print(f"Task '{location}' does not exist.")
            return
        data = data[component]

    data["time"] = 0
    current_user_json_handler.dump()
    print(f"Reset time for task '{location}'")

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

