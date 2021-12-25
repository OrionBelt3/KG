import PySimpleGUI as sg
import matplotlib.pyplot as plt
import numpy as np

A = 0
B = 2*np.pi
phi = np.linspace(A, B, int(B-A) * 10)

def x(phi, a):
    print(x)
    return a*(np.cos(phi))**3

def y(phi, a):
    return a*(np.sin(phi))**3


def draw_plot(a=1):
    if a <= 0:
        sg.popup('Please, enter correct a value!')
    else:
        plt.plot(x(phi, a), y(phi, a))
        plt.grid(True)
        plt.show(block=True)

layout = [
    [sg.Text('Parameter a:'), sg.InputText()],
    [sg.Button('Plot'), sg.Button('Exit'), sg.Button('Enter')]]

window = sg.Window('___Setting window___', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Plot':
        draw_plot()
    elif event == 'Enter':
        #plt.close()
        draw_plot(int(values[0]))
window.close()