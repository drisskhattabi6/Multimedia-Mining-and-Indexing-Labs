from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Paramètres de l'animation
anglex = 0.0
angley = 0.0
anglez = 0.0
pasTranslate = 0.3
pasRotate = 3
signe = 1.0
tx = 0.0
ty = 0.0
tz = 0.0


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Lab : Les buffers (1)")
    # Couleur du fond
    glClearColor(0.0, 0.0, 0.0, 1)
    # Activer l'élimination des faces cachées
    glEnable(GL_CULL_FACE)
    # Par défaut les faces négatives sont cachées
    # Pour cacher les faces positives, enlever ce commenttaire.
    # glCullFace(GL_FRONT)
    # Activer la transparence
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    # CallBacks
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(fleches)
    glutReshapeFunc(reshape)
    glutMainLoop()


def desFaces():
    glBegin(GL_QUADS)
    # Les trois faces en bas sont négatives
    # La face rouge est transparente
    glColor4f(1.0, 0.0, 0.0, 0.2)
    glVertex3d(1, 1, -1)
    glVertex3d(1, -1, -1)
    glVertex3d(-1, -1, -1)
    glVertex3d(-1, 1, -1)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3d(1, 1, 1)
    glVertex3d(1, -1, 1)
    glVertex3d(1, -1, -1)
    glVertex3d(1, 1, -1)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3d(-1, 1, 1)
    glVertex3d(-1, 1, -1)
    glVertex3d(-1, -1, -1)
    glVertex3d(-1, -1, 1)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    # Afficher un objet au centre
    glLoadIdentity()
    glColor4f(0.0, 1.0, 1.0, 1.0)
    glutSolidSphere(0.2, 36, 36)
    # glutSolidTeapot(.5);
    # Afficher les 3 faces
    glLoadIdentity()
    glTranslatef(tx, ty, tz)
    glRotatef(anglex, 1.0, 0.0, 0.0)
    glRotatef(angley, 0.0, 1.0, 0.0)
    glRotatef(anglez, 0.0, 0.0, 1.0)
    desFaces()
    glutSwapBuffers()


def reshape(w, h):
    # Où afficher sur l'écran (tout l'écran)
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Vue perspective (exemple 2)
    gluPerspective(90.0, w / h, 0.1, 25.0)
    gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glMatrixMode(GL_MODELVIEW)


def keyboard(self, key, x, y):
    global tx, ty, tz, signe, pasTranslate
    if key == b"\x1b":  # Touche ESC
        exit(1)
    elif key == b"x":
        tx = tx + signe * pasTranslate
    elif key == b"y":
        ty += signe * pasTranslate
    elif key == b"z":
        tz += signe * pasTranslate
    elif key == b"s":  # Changer le sens de la translation
        signe *= -1
    glutPostRedisplay()


def fleches(key, x, y):
    global anglex, angley, anglez, pasRotate
    if key == GLUT_KEY_LEFT:
        angley = angley + pasRotate
    if angley > 360.0:
        angley = 0.0
    elif key == GLUT_KEY_RIGHT:
        angley = angley - pasRotate
    if angley < 0.0:
        angley = 360.0
    elif key == GLUT_KEY_UP:
        anglex = anglex + pasRotate
    if anglex > 360.0:
        anglex = 0.0
    elif key == GLUT_KEY_DOWN:
        anglex = anglex - pasRotate
    if anglex < 0.0:
        anglex = 360.0
    elif key == GLUT_KEY_PAGE_UP:
        anglez = anglez + pasRotate
    if anglez > 360.0:
        anglez = 0.0
    elif key == GLUT_KEY_PAGE_DOWN:
        anglez = anglez - pasRotate
    if anglez < 0.0:
        anglez = 360.0
    glutPostRedisplay()


if __name__ == "__main__":
    main()
