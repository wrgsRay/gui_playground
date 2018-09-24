"""
@author: wrgsray
python 3.6
"""
import PySimpleGUI as sg


def main():
    layout = [
        [sg.Text('Please enter your name, address, phone')],
        [sg.Text('Name', size=(15,1)), sg.InputText()],
        [sg.Text('Address', size=(15, 1)), sg.InputText()],
        [sg.Text('Phone', size=(15, 1)), sg.InputText()],
        [sg.Submit(), sg.Cancel()]
    ]
    window = sg.Window('Simple data entry window').Layout(layout)
    button, values = window.Read()

    print(button, values[0], values[1], values[2])


if __name__ == '__main__':
    main()
