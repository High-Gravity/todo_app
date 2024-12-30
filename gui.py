import functions
import FreeSimpleGUI as sg


label = sg.Text("Enter a To-Do: ")
input_box = sg.InputText(tooltip="Enter Todo: ", key='todo')
add_button = sg.Button("Add")


window = sg.Window("ListLee",
                   layout=[[label], [input_box, add_button]],
                   font=('Georgia', 20))


while True:
   event,values = window.read()
   match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break
window.close()