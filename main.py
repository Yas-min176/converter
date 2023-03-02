import PySimpleGUI as sg

layout = [
    [sg.Text('Text', enable_events = True, key = '-TEXT-'), sg.Spin(['item 1', 'item 2'])],
    [sg.Button('Botão', key = '-BUTTON1-')], 
    [sg.Input()],
    [sg.Text('Teste'), sg.Button('Botão de Teste', key = '-BUTTON2-')]
]

window = sg.Window('Conversor', layout)

while True:
    event, values = window.read()

    match event:
        case sg.WIN_CLOSED:
            break

        case '-BUTTON1-':
            print(values[1])

        case '-BUTTON2-':
            print('Test')

        case '-TEXT-':
            print('Text was pressed')

    # match values[0]:
    #     case 1:
    #         text1 = 'item 1'

    #     case 2:
    #         text1 = 'item 2'




window.close()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     