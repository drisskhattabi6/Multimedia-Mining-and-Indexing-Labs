from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from time import sleep

# Paramètres de l'animation
DIST_ST = 10
DIST_TL = 1.5
angle1 = 0
angle2 = 0


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Lab : Les buffers (2)")
    # Couleur du fond
    glClearColor(0.0, 0.0, 0.0, 1)
    # Activer le test de profondeur
    glEnable(GL_DEPTH_TEST)
    # CallBacks
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutIdleFunc(anime)
    glutReshapeFunc(reshape)
    glutMainLoop()


def axes():
    glLineStipple(4, 0xAAAA)
    glEnable(GL_LINE_STIPPLE)
    glLineWidth(3)
    # Tracer les axes
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-100.0, 0.0, 0.0)
    glVertex3f(100.0, 0.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -100.0, 0.0)
    glVertex3f(0.0, 100.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -100.0)
    glVertex3f(0.0, 0.0, 100.0)
    glEnd()
    glDisable(GL_LINE_STIPPLE)


def display():
    global DIST_ST, DIST_TL, angle1, angle2
    # Effacer l'écran avec la couleur du fond courant
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    axes()
    glColor3f(1.0, 0.0, 0.0)
    glutSolidSphere(5.0, 36, 36)
    glRotatef(angle1, 0.0, 1.0, 0.0)
    glTranslatef(DIST_ST, 0.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glutSolidSphere(1.0, 12, 12)
    glRotatef(angle2, 0.0, 1.0, 0.0)
    glTranslatef(DIST_TL, 0.0, 0.0)
    glColor3f(1.0, 1.0, 1.0)
    glutSolidSphere(0.3, 12, 12)
    glutSwapBuffers()


def anime():
    global angle1, angle2
    angle1 += 6
    if angle1 > 360:
        angle1 = 0
        angle2 += 1
    if angle2 > 360:
        angle2 = 0
    glutPostRedisplay()
    # Pause de 200 ms
    sleep(0.2)


def reshape(w, h):
    # Où afficher sur l'écran (tout l'écran)
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Vue perspective (exemple 2)
    gluPerspective(90.0, w / h, 0.1, 100.0)
    gluLookAt(-10.0, 10.0, 10.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glMatrixMode(GL_MODELVIEW)


def keyboard(key, x, y):
    if key == b"\x1b":  # Touche ESC
        exit(1)


if __name__ == "__main__":
    main()
