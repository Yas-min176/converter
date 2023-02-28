import PySimpleGUI as sg

layout = [
    [sg.Text('Texto'), sg.Spin(['item 1', 'item 2'])],
    [sg.Button('Botão')], 
    [sg.Input()]
]

window = sg.Window('Conversor', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-BUTTON1':
        print('button pressed')

window.close()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     