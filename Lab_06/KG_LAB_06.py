from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import PySimpleGUI as sg

name = 'Sphere'
a = 50
move = 0
intensive = 0.5
X = 30
Y = 30
Z = 30

def key_event(key):
    if key == 27:
        exit(0)

def draw():
    glutInit(sys.argv)
    #GLUT_DOUBLE - окно с двойным буфером
    #GLUT_RGB - rgb палитра
    #GLUT_DEPTH - окно с буфером глубины
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(400,400)
    glutCreateWindow(name)

    #задний фон
    glClearColor(.1,.1,.1,1.)
    #При шадинге цвет каждой вершины индивидуален, при прорисовке линии цвет интерполируется между вершинами.
    glShadeModel(GL_SMOOTH)

    #освещение
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    lightZeroPosition = [X,Y,Z,1.] #изменение позиции источника света
    lightZeroColor1 = [intensive,1.0,1.0,1.0] #интенсивность и цвет освещения
    lightZeroColor2 = [intensive,1.0,1.0,1.0]
    lightZeroColor3 = [intensive,1.0,1.0,1.0]
    #управление свойствами источника света 
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    glLightfv(GL_LIGHT0, GL_SPECULAR, lightZeroColor1)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)

    glLightfv(GL_LIGHT1, GL_POSITION, lightZeroPosition)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, lightZeroColor2)
    glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, 0.05)

    glLightfv(GL_LIGHT2, GL_POSITION, lightZeroPosition)
    glLightfv(GL_LIGHT2, GL_DIFFUSE, lightZeroColor3)
    glLightf(GL_LIGHT2, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT2, GL_LINEAR_ATTENUATION, 0.05)

    #включить нулевой источник света
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)
    glEnable(GL_LIGHT2)

    #функция рисования для текущего окна
    glutDisplayFunc(display) 
    #говорит о том, что команды относятся к проекту
    glMatrixMode(GL_PROJECTION)
    gluPerspective(40.,1.,1.,40.)
    #оворит о том, что работы будет теперь просмотром, а не проектом
    glMatrixMode(GL_MODELVIEW) #перемещение
    gluLookAt(0,0,10,
              0,0,0,
              0,1,0)
    glPushMatrix()
    glutMainLoop()


def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    #color = [1., 1., 0., 1.]
    color = [50.0]
    glMaterialfv(GL_FRONT, GL_SHININESS, color)
    #создание сферы (радиус, количество проекций вдоль оси OZ и поперек оси OZ)
    #glutWireSphere(2,a,a)
    glutSolidSphere(2,a,a)
    glPopMatrix()
    glutSwapBuffers()

layout = [
    [sg.Text('Approximation')],
    [sg.Slider(orientation ='horizontal', key='slider1', range=(4,100))],
    [sg.Text('Light source intensity')],
    [sg.Slider(orientation ='horizontal', key='slider2', range=(0,100))],
    [sg.Text('Camera X:')],
    [sg.Slider(orientation ='horizontal', key='slider3', range=(-100,100))],
    [sg.Text('Camera Y:')],
    [sg.Slider(orientation ='horizontal', key='slider4', range=(-100,100))],
    [sg.Text('Camera Z:')],
    [sg.Slider(orientation ='horizontal', key='slider5', range=(-100,100))],
    [sg.Button('Plot'), sg.Button('Exit'), sg.Button('Enter')]]

window = sg.Window('LAB_06', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Plot':
        draw()
    elif event == 'Enter':
        a = int(values['slider1'])
        intensive = int(values['slider2'])/100
        X = int(values['slider3'])
        Y = int(values['slider4'])
        Z = int(values['slider5'])
        draw()
window.close()