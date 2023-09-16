import PySimpleGUI as sg


label1 = sg.Text("Enter Feet")
input1 = sg.InputText(key='feet')

label2 = sg.Text("Enter Inches")
input2 = sg.InputText(key='inches')

button = sg.Button("Convert")
input_with_result = sg.Text(key='output_value')

button_ex = sg.Button("Exit")

window = sg.Window('Convert value',
                   layout=[[label1, input1],
                           [label2, input2],
                           [button, button_ex, input_with_result]])

while True:
    event, value = window.read()

    if event == 'Exit':
        break
    if event == sg.WIN_CLOSED:
        break
    print(value)
    feet_value = value['feet']
    inches_value = value['inches']
    if feet_value == "" or inches_value == "":
        sg.Popup('Please, feel all fields!')
        continue
    feet_to_meters = float(feet_value) * 0.3048
    inches_to_meters = float(inches_value) * 0.0254
    meters = str(feet_to_meters + inches_to_meters) + ' m'
    window['output_value'].update(value=meters)




window.close()
