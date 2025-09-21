

# MongoDB TODO List CLI Application 📝

A simple, command-line interface (CLI) application for managing a TODO list, built with Python and MongoDB. This project demonstrates basic CRUD (Create, Read, Update, Delete) operations and serves as a great starting point for learning how to connect a Python application to a NoSQL database.

## \#\# Features ✨

  * **Create** new tasks.
  * **View** all existing tasks with their unique IDs.
  * **Update** the description of an existing task.
  * **Delete** a task from the list.
  * Simple and interactive menu-driven interface.

-----

## \#\# Requirements 🛠️

  * Python 3.x
  * A running instance of MongoDB (the script connects to a local instance by default).
  * The `pymongo` Python library.

-----

## \#\# Installation & Setup 🚀

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2.  **Install the required Python library:**

    ```bash
    pip install pymongo
    ```

3.  **Ensure your MongoDB server is running.** This script assumes your MongoDB instance is running locally on the default port `27017`.

-----

## \#\# How to Use ▶️

1.  Run the application from your terminal:

    ```bash
    python your_script_name.py
    ```

2.  You will be presented with a menu. Simply enter the number corresponding to the action you want to perform.

    ```
    ===== TODO List Menu =====
    1. Create Task
    2. View Tasks
    3. Update Task
    4. Delete Task
    5. Exit
    ==========================
    Enter your choice:
    ```

-----

## \#\# Code Overview 🔍

The application logic is contained within a single Python script.

  * **Database Connection:** The script connects to a local MongoDB instance and uses a database named `todo_db` and a collection named `tasks`.

  * **CRUD Functions:**

      * `create_task(description)`: Inserts a new task document into the `tasks` collection.
      * `read_tasks()`: Retrieves and prints all tasks, displaying their unique `_id` and description.
      * `update_task(task_id, new_description)`: Finds a task by its `_id` and updates its description.
      * `delete_task(task_id)`: Finds a task by its `_id` and removes it from the collection.

  * **Main Loop:** An infinite `while` loop runs the main menu, collects user input, and calls the appropriate function until the user chooses to exit.
