import PySimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select files to compress")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Chose", key='files')


label2 = sg.Text("Select distanation folder")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Chose", key='folder')

compress_button = sg.Button("Compress")

output_label = sg.Text(key='output')

window = sg.Window('Compress Files',
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button, output_label]])

while True:
    event, values = window.read()
    print(event)
    print(values)
    file_paths = values['files'].split(';')
    folder = values['folder']
    print(file_paths)
    print(folder)
    make_archive(file_paths, folder)
    window['output'].update(value='Compression completed')

    if event == sg.WIN_CLOSED:
        break

window.close()
