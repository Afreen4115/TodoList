from bson import ObjectId
from pymongo import MongoClient

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

db=client.todo_db   #todo_db is our database name
tasks_collection=db.tasks # tasks is our collection name

def create_task(description):
    task={
        'task':description
    }
    result=tasks_collection.insert_one(task)
    print(f'✅ Task created with id: {result.inserted_id}')


def read_tasks():
    tasks = list(tasks_collection.find())
    if not tasks:
        print("No tasks found")
        return
    print("\n--- Your Tasks ---")
    for docs in tasks:
        print(f"ID: {docs['_id']} - Task: {docs['task']}")
    print("------------------")

def update_task(task_id, new_description):
    try:
        obj_id = ObjectId(task_id)
        result = tasks_collection.update_one(
            {'_id': obj_id},
            {'$set': {'task': new_description}}
        )
        if result.modified_count > 0:
            print(f"✅ Task {task_id} updated successfully.")
        else:
            print(f"⚠️ No task found with ID: {task_id}")
    except Exception as e:
        print(f"Error: Invalid ID format. {e}")


def delete_task(task_id):
    try:
        obj_id = ObjectId(task_id)
        result = tasks_collection.delete_one({'_id': obj_id})
        if result.deleted_count > 0:
            print(f"✅ Task {task_id} deleted successfully.")
        else:
            print(f"⚠️ No task found with ID: {task_id}")
    except Exception as e:
        print(f"Error: Invalid ID format. {e}")

while True:
    print("\n===== TODO List Menu =====")
    print("1. Create Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    print("==========================")

    choice = input("Enter your choice: ")

    if choice=="1":
        description=input("Enter your task: ")
        create_task(description)
    elif choice=="2":
        read_tasks()
    elif choice=="3":
        read_tasks()
        task_id = input("Enter the ID of the task to update: ")
        new_description = input("Enter the new task description: ")
        update_task(task_id, new_description)
    elif choice=="4":
        read_tasks()
        task_id = input("Enter the ID of the task to delete: ")
        delete_task(task_id)
    elif choice=="5":
        print("Exiting application.")
        client.close()
        break
    else:
        print("Provide a valid option")