import PySimpleGUI as sg


label1 = sg.Text("Enter Feet")
input1 = sg.InputText()

label2 = sg.Text("Enter Inches")
input2 = sg.InputText()

button = sg.Button("Convert")

window = sg.Window('Compress Files',
                   layout=[[label1, input1],
                           [label2, input2],
                           [button]])


window.read()
window.close()
