from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Lab 01")

    ## Couleur du fond
    glClearColor(0.0, 0.0, 0.0, 1)

    glutDisplayFunc(aff)
    glutKeyboardFunc(keyboard)
    glutReshapeFunc(redim)

    glutMainLoop()


def redim(w, h):

    ## Où afficher sur l'écran (tout l'écran)
    glViewport(0, 0, w, h)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    ## Vue orthographique
    glOrtho(-3.0, 3.0, -3.0, 3.0, -10.0, 10.0)
    gluLookAt(2.5, 1.5, 2.5, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    ## Vue perspective (exemple 2)
    # gluPerspective(90., w/h, 0.1, 15.)
    # gluLookAt(5., 1., 1., 0., 0., 0., 0., 1., 0.)

    glMatrixMode(GL_MODELVIEW)


def keyboard(self, key, x, y):
    intKey = int.from_bytes(key, "little")
    if intKey == 27:
        exit(1)


def axes():
    glLineStipple(1, 0x0CFF)
    glEnable(GL_LINE_STIPPLE)
    glLineWidth(1)

    # Tracer les axes
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-10.0, 0.0, 0.0)
    glVertex3f(10.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -10.0, 0.0)
    glVertex3f(0.0, 10.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -10.0)
    glVertex3f(0.0, 0.0, 10.0)
    glEnd()
    glDisable(GL_LINE_STIPPLE)


def aff():
    # Effacer un Buffer
    glClear(GL_COLOR_BUFFER_BIT)

    ## Affichage des axes
    glLoadIdentity()
    axes()

    ## Exemple (1)
    ## avec le type GL_POINTS on peut voir l'effet
    ## de la modification de :      glPointSize(3)
    ## Modifier le paramètre type pour le test

    # glBegin(GL_TRIANGLES)

    # glColor3f(1.0, 1.0, 0.0)
    # glVertex3f(0.0, 1.0, 0.0)
    # glVertex3f(0.0, 0.5, 0.0)
    # glVertex3f(0.5, 0.0, 0.0)

    # glColor3f(0.0, 0.0, 1.0)
    # glVertex3f(1.0, 0.0, 0.0)
    # glColor3f(1.0, 0.0, 0.0)
    # glVertex3f(0.5, 1.0, 0.0)
    # glColor3f(0.0, 1.0, 0.0)
    # glVertex3f(1.0, 0.5, 0.0)

    # glEnd()

    # Utiliser les objets GLUT
    # glutSolidTorus(0.5,1.,36,36)
    # glutWireSphere(1,36,36)
    # glutWireTeapot(0.5)

    # Deux cubes sur l'axe des X. Exemple (2)

    glTranslated(3.0, 0.0, 0.0)
    glColor3f(1.0, 0.0, 0.0)
    glutSolidCube(0.5)

    glLoadIdentity()
    glTranslated(-3.0, 0.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)
    glutSolidCube(0.5)

    ## Afficher le back buffer (ce qui est dessiné en arrière plan,
    ## En cas de Single buffering, utiliser glFlush()
    glutSwapBuffers()


if __name__ == "__main__":
    main()
