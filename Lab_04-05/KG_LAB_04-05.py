from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import PySimpleGUI as sg

name = 'Sphere'
a = 50
intensive = 0.5

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
    lightZeroPosition = [10.,10.,10.,1.] #изменение позиции источника света
    lightZeroColor = [intensive,1.0,1.0,1.0] #интенсивность и цвет освещения
    #управление свойствами источника света 
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)

    #включить нулевой источник света
    glEnable(GL_LIGHT0)

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
    color = [1.0,1.,0.,1.]
    glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
    #создание сферы (радиус, количество проекций вдоль оси OZ и поперек оси OZ)
    glutWireSphere(2,a,a)
    glPopMatrix()
    glutSwapBuffers()

layout = [
    [sg.Text('Approximation')],
    [sg.Slider(orientation ='horizontal', key='slider1', range=(4,100))],
    [sg.Text('Light source intensity')],
    [sg.Slider(orientation ='horizontal', key='slider2', range=(0,100))],
    [sg.Button('Plot'), sg.Button('Exit'), sg.Button('Enter')]]

window = sg.Window('___Setting window___', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Plot':
        draw()
    elif event == 'Enter':
        a = int(values['slider1'])
        intensive = int(values['slider2'])/100
        draw()
window.close()