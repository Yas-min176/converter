import PySimpleGUI as sg

layout = [
    [
        sg.Input(key='-INPUT-'),
        sg.Spin(['mile to feet', 'mile to km', 'mile to m', 'mile to cm', 'mile to mm', 'feet to mile', 'feet to km',
                 'feet to m', 'feet to cm', 'feet to mm', 'km to mile', 'km to feet', 'km to m', 'km to cm', 'km to mm',
                 'm to mile', 'm to feet', 'm to km', 'm to cm', 'm to mm', 'cm to mile', 'cm to feet', 'cm to km',
                 'cm to m', 'cm to mm',  'mm to feet', 'mm to mile', 'mm to km', 'mm to m', 'mm to cm',
                 'kg to pound', 'pound to kg', 'sec to min', 'sec to hour', 'sec to day',
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

                    case 'mile to feet':
                        output = round(float(input_value) * 5280)
                        output_string = f'{input_value} miles are {output} mm'

                    case 'mile to km':
                        output = round(float(input_value) * 1.60934)
                        output_string = f'{input_value} miles are {output} km.'

                    case 'mile to m':
                        output = round(float(input_value) * 1609.34)
                        output_string = f'{input_value} miles are {output} m.'

                    case 'mile to cm':
                        output = round(float(input_value) * 160934)
                        output_string = f'{input_value} miles are {output} cm.'

                    case 'mile to mm':
                        output = round(float(input_value) * 1609344)
                        output_string = f'{input_value} miles are {output} mm'

                    case 'feet to mile':
                        output = round(float(input_value) * 0.000189394)
                        output_string = f'{input_value} feet are {output} miles'

                    case 'feet to km':
                        output = round(float(input_value) * 0.000304800097536)
                        output_string = f'{input_value} feet are {output} km'

                    case 'feet to m':
                        output = round(float(input_value) * 0.304800097536)
                        output_string = f'{input_value} feet are {output} m'

                    case 'feet to cm':
                        output = round(float(input_value) * 30.4800097536)
                        output_string = f'{input_value} feet are {output} cm'

                    case 'feet to mm':
                        output = round(float(input_value) * 304.800097536)
                        output_string = f'{input_value} feet are {output} mm'

                    case 'km to mile':
                        output = round(float(input_value) * 0.06214)
                        output_string = f'{input_value} km are {output} miles.'

                    case 'km to feet':
                        output = round(float(input_value) * 3280.84)
                        output_string = f'{input_value} km are {output} cm.'

                    case 'km to m':
                        output = round(float(input_value) * 1000)
                        output_string = f'{input_value} km are {output} meters.'

                    case 'km to cm':
                        output = round(float(input_value) * 100000)
                        output_string = f'{input_value} km are {output} cm.'

                    case 'km to mm':
                        output = round(float(input_value) * 1000000)
                        output_string = f'{input_value} km are {output} mm.'

                    case 'm to mile':
                        output = round(float(input_value) * 0.000621371)
                        output_string = f'{input_value} meters are {output} mile'

                    case 'm to feet':
                        output = round(float(input_value) * 3.28084)
                        output_string = f'{input_value} meters are {output} feet'

                    case 'm to km':
                        output = round(float(input_value) / 1000 )
                        output_string = f'{input_value} meters are {output} km'

                    case 'm to cm':
                        output = round(float(input_value) * 100)
                        output_string = f'{input_value} meters are {output} cm'

                    case 'm to mm':
                        output = round(float(input_value) * 1000)
                        output_string = f'{input_value} meters are {output} mm'

                    case 'cm to mile':
                        output = round(float(input_value) * 6.2137)
                        output_string = f'{input_value} cm are {output} miles'

                    case 'cm to feet':
                        output = round(float(input_value) * 0.0328084)
                        output_string = f'{input_value} cm are {output} feet'

                    case 'cm to km':
                        output = round(float(input_value) / 100000)
                        output_string = f'{input_value} cm are {output} km'

                    case 'cm to m':
                        output = round(float(input_value) / 100)
                        output_string = f'{input_value} cm are {output} m'

                    case 'cm to mm':
                        output = round(float(input_value) * 10)
                        output_string = f'{input_value} cm are {output} km'

                    case 'mm to mile':
                        output = round(float(input_value) * 6.2137)
                        output_string = f'{input_value} mm are {output} miles'

                    case 'mm to feet':
                        output = round(float(input_value) * 0.00328084)
                        output_string = f'{input_value} mm are {output} feet'

                    case 'mm to km':
                        output = round(float(input_value) * 1000000)
                        output_string = f'{input_value} mm are {output} km'

                    case 'mm to m':
                        output = round(float(input_value) * 1000)
                        output_string = f'{input_value} mm are {output} meters'

                    case 'mm to cm':
                        output = round(float(input_value) * 10)
                        output_string = f'{input_value} mm are {output} cm'

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
