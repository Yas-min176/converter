import PySimpleGUI as sg

layout = [
    [
        sg.Input(key='-INPUT-'),
        sg.Spin(['km to mile', 'mile to km', 'kg to pound', 'pound to kg', 'sec to min', 'sec to hour', 'sec to day',
                 'min to sec', 'min to hour', 'min to day', 'hour to sec', 'hour to min', 'hour to day', 'day to sec',
                 'day to min', 'day to hour', 'km/h to m/s', 'm/s to km/h'], key='-UNITS-'),
        sg.Button('Convert', key='-CONVERT-')
    ],
    [sg.Text('Conversion', key='-OUTPUT-')]
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

                    # ------------------------ distance ------------------------------
                    case 'km to mile':
                        output = round(float(input_value) * 0.06214)
                        output_string = f'{input_value} km are {output} miles.'

                    case 'mile to km':
                        output = round(float(input_value) / 0.06214)
                        output_string = f'{input_value} miles are {output} km.'

                    # ------------------------- weight -------------------------------
                    case 'kg to pound':
                        output = round(float(input_value) * 2.20462)
                        output_string = f'{input_value} kg are {output} pounds.'

                    case 'pound to kg':
                        output = round(float(input_value) / 2.20462)
                        output_string = f'{input_value} pounds are {output} km.'

                    # -------------------------- time -------------------------------
                    case 'sec to min':
                        output = round(float(input_value) / 60)
                        output_string = f'{input_value} seconds are {output} minutes'

                    case 'sec to hour':
                        output = round(float(input_value) / 3600)
                        output_string = f'{input_value} seconds are {output} hours'

                    case 'sec to day':
                        output = round(float(input_value) / 86400)
                        output_string = f'{input_value} seconds are {output} days'

                    case 'min to sec':
                        output = round(float(input_value) * 60)
                        output_string = f'{input_value} minutes are {output} seconds'

                    case 'min to hour':
                        output = round(float(input_value) / 60)
                        output_string = f'{input_value} minutes are {output} hours'

                    case 'min to day':
                        output = round(float(input_value) / 1440)
                        output_string = f'{input_value} minutes are {output} days'

                    case 'hour to sec':
                        output = round(float(input_value) * 3600)
                        output_string = f'{input_value} hours are {output} seconds'

                    case 'hour to min':
                        output = round(float(input_value) * 60)
                        output_string = f'{input_value} hours are {output} minutes'

                    case 'hour to day':
                        output = round(float(input_value) / 24)
                        output_string = f'{input_value} hours are {output} days'

                    case 'day to sec':
                        output = round(float(input_value) * 86400)
                        output_string = f'{input_value} days are {output} seconds'

                    case 'day to min':
                        output = round(float(input_value) * 1440)
                        output_string = f'{input_value} days are {output} minutes'

                    case 'day to hour':
                        output = round(float(input_value) * 24)
                        output_string = f'{input_value} days are {output} hours'

                    # ------------------------- speed -------------------------------
                    case 'km/h to m/s':
                        output = round(float(input_value) / 3.6)
                        output_string = f'{input_value} km/h are {output} m/s'

                    case 'm/s to km/h':
                        output = round(float(input_value) * 3.6)
                        output_string = f'{input_value} m/s are {output} km/h'

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
