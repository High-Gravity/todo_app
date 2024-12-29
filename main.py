import functions
import time

now = time.strftime("%B %d, %Y %H:%M:%S")
print("It is " + now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ").lower()
    user_action = user_action.strip()

    if user_action.startswith('add'):
        try:
            todo = user_action[4:]
            items = functions.get_todos()
            items.append(todo.capitalize() + "\n")

            functions.write_todos(items)

        except ValueError:
            print("Command not recognized...")
            continue

    elif user_action.startswith('show'):
        items = functions.get_todos()

        for index, item in enumerate(items):
            item = item.strip("\n")
            todo = f"{index + 1}. {item}"
            print(todo)

    elif user_action.startswith('edit'):
        number = int(user_action[5:])
        number = number - 1
        items = functions.get_todos()
        items[number] = input("Add a todo: ").lower() + "\n"

        functions.write_todos(items)

        print(f"{number} has been updated")

    elif user_action.startswith('complete'):
        try:
            items = functions.get_todos()
            number = int(user_action[9:])
            items.pop(number - 1)

            functions.write_todos(items)

            print(f"{number} has been completed.")

        except IndexError:
            print("There is no list item with that number...")

    elif user_action.startswith('exit'):
        break

    else:
        print(f"Command Not Recognized: {user_action}")

print("Goodbye!")