import PySimpleGUI as sg
from zip_extractor import extract_archive


label1 = sg.Text("Select archive")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Chose", key='archive')


label2 = sg.Text("Select dest folder")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Chose", key='folder')

extract_button = sg.Button("Extract")

output_label = sg.Text(key='output')

window = sg.Window('Compress Files',
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [extract_button, output_label]])

while True:
    event, values = window.read()
    file_paths = values['archive']
    folder = values['folder']
    extract_archive(file_paths, folder)
    window['output'].update(value='Files was successfully extracted')

    if event == sg.WIN_CLOSED:
        break

window.close()
