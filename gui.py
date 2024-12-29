import functions
import FreeSimpleGUI as sg


label = sg.Text("Enter A To-Do: ")
input_box = sg.InputText(tooltip="Enter Todo: ")
add_button = sg.Button("Add")


window = sg.Window("ListLee", layout=[[label], [input_box, add_button]])
window.read()
window.close()