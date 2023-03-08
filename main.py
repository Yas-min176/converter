import PySimpleGUI as sg

layout = [
    [
        sg.Input(key = '-INPUT-'),
        sg.Spin(['km to mile', 'kg to pound', 'sec to min'], key = '-UNITS-'),
        sg.Button('Convert', key = '-CONVERT-')
    ],
    [sg.Text('Conversion', key = '-OUTPUT-')]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    match event:

        case sg.WIN_CLOSED:
            break

        case '-CONVERT-':
            input_value = values['-INPUT-']
            if input_value.isnumeric():
                print(input_value)
                match values['-UNITS-']:
                    case 'km to mile':
                        output = round(float(input_value) * 0.06214)
                        output_string = f'{input_value} km are {output} miles.'

                    case 'kg to pound':
                        output = round(float(input_value) * 2.20462)
                        output_string = f'{input_value} kg are {output} pounds.'

                    case 'sec to min':
                        output = round(float(input_value)/60)
                        output_string = f'{input_value} seconds are {output} minutes'

                window['-OUTPUT-'].update(output_string)



    # match event:
    #     case sg.WIN_CLOSED:
    #         break
    #
    #     case '-BUTTON1-':
    #         print(values[1])
    #
    #     case '-BUTTON2-':
    #         print('Test')
    #
    #     case '-TEXT-':
    #         print('Text was pressed')

    # match values[0]:
    #     case 1:
    #         text1 = 'item 1'

    #     case 2:
    #         text1 = 'item 2'

window.close()
