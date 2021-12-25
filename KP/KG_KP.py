import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import scipy as sp
import scipy.interpolate
import random
import PySimpleGUI as sg

def draw(aprox=10, carcas=True):
    if carcas == True:
        alp = 0.2
    else:
        alp = 1
    random.seed(1)
    data_size = 5
    max_value_range = 132651
    x = np.array([random.random()*max_value_range for p in range(0,data_size)])
    y = np.array([random.random()*max_value_range for p in range(0,data_size)])
    z = 2*x*x*x + np.sqrt(y)*y + random.random()

    #ax.scatter3D(x,y,z, c='r')
    x_grid = np.linspace(0, 132651, aprox*len(x))
    y_grid = np.linspace(0, 132651, aprox*len(y))

    B1, B2 = np.meshgrid(x_grid, y_grid, indexing='xy')
    Z = np.zeros((x.size, z.size))

    spline = sp.interpolate.Rbf(x,y,z,function='thin_plate',smooth=5, episilon=5)
    Z = spline(B1,B2)

    fig = plt.figure(figsize=(10,6))
    ax = axes3d.Axes3D(fig)
    ax.plot_wireframe(B1, B2, Z)
    ax.plot_surface(B1, B2, Z,alpha=alp)
    plt.show()

layout = [
    [sg.Slider(orientation ='horizontal', key='aprox', range=(2,100))],
    [sg.Checkbox('carcas visible ', default=False, key='carcas')],
    [sg.Button('Plot'), sg.Button('Exit'), sg.Button('Enter')]]

window = sg.Window('___Setting window___', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Plot':
        draw()
    elif event == 'Enter':
        draw(int(values['aprox']), values['carcas'])
window.close()