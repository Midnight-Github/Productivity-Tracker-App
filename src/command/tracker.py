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
        if component not in data:
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

def moveTask(src_location, dest_location):
    if current_user_json_handler.data['username'] is None:
        print("You must be logged in to move a task.")
        return

    src_components = os.path.normpath(src_location).split(os.sep)
    dest_components = os.path.normpath(dest_location).split(os.sep)

    # Circular move protection
    if src_location == dest_location or dest_components[:len(src_components)] == src_components:
        print("Cannot move a task into itself or its own subtree.")
        return

    data = current_user_json_handler.data["user_data"]["tracker"] # pyright: ignore

    # Traverse to source parent
    src_parent = data
    for component in src_components[:-1]:
        if component not in src_parent:
            print(f"Source path '{src_location}' does not exist.")
            return
        src_parent = src_parent[component]

    src_task = src_components[-1]
    if src_task not in src_parent:
        print(f"Task '{src_location}' does not exist.")
        return

    # Get the task data to move
    task_data = src_parent[src_task]

    # Traverse to destination parent
    dest_parent = data
    for component in dest_components[:-1]:
        if component not in dest_parent:
            print(f"Destination path '{dest_location}' does not exist.")
            return
        dest_parent = dest_parent[component]

    dest_task = dest_components[-1]
    if dest_task in dest_parent:
        print(f"Destination '{dest_location}' already exists.")
        return

    # Move the task
    dest_parent[dest_task] = task_data
    del src_parent[src_task]
    current_user_json_handler.dump()
    print(f"Moved task '{src_location}' to '{dest_location}'.")

def startTask(task_location):
    if current_user_json_handler.data['username'] is None:
        print("You must be logged in to start a task.")
        return

    path_components = os.path.normpath(task_location).split(os.sep)
    data = current_user_json_handler.data["user_data"]["tracker"]  # pyright: ignore

    for component in path_components:
        if component not in data:
            print(f"Task '{task_location}' does not exist.")
            return
        data = data[component]

    if "start_time" in data:
        print(f"Task '{task_location}' is already started.")
        return

    data["start_time"] = time.time()
    current_user_json_handler.dump()

    print(f"Started task '{task_location}'")

def stopTask(task_location):
    if current_user_json_handler.data['username'] is None:
        print("You must be logged in to stop a task.")
        return

    path_components = os.path.normpath(task_location).split(os.sep)
    data = current_user_json_handler.data["user_data"]["tracker"]  # pyright: ignore

    for component in path_components:
        if component not in data:
            print(f"Task '{task_location}' does not exist.")
            return
        data = data[component]

    if "start_time" not in data:
        print(f"Task '{task_location}' is not started.")
        return

    elapsed_time = time.time() - data["start_time"]
    data["time"] += elapsed_time
    del data["start_time"]
    current_user_json_handler.dump()

    print(f"Stopped task '{task_location}'. Time spend: {elapsed_time:.2f} seconds. Total time spent: {data['time']:.2f} seconds.")