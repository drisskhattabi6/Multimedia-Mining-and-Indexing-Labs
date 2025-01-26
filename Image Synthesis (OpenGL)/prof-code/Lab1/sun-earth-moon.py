from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Labs Note 8")
    # Couleur du fond
    glClearColor(0.0, 0.0, 0.0, 1)
    glutDisplayFunc(aff)
    glutKeyboardFunc(keyboard)
    glutReshapeFunc(redim)
    glutMainLoop()


def redim(w, h):
    # Où afficher sur la fenêtre (toute la fenêtre)
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Mode parallèle
    # glOrtho(-3.,3.,-3.,3.,-10,10.)
    # Mode perspective
    gluPerspective(90.0, w / h, 0.1, 15)
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
    # Effacer le Buffer des couleurs
    glClear(GL_COLOR_BUFFER_BIT)
    # Initialiser la matrice courante à l'identité
    glLoadIdentity()
    gluLookAt(5, 5, 5, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    # Affichage les axes
    axes()
    # L'objet suivant ne subit aucune transformation
    glColor3f(1.0, 0.0, 0.0)
    glutSolidSphere(1.0, 12, 12)
    # Deux sphères sur l'axe des X.
    glRotatef(30, 0.0, 1.0, 0.0)
    glTranslated(5.0, 0.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    # L'objet suivant subit 2 transformations
    glutSolidSphere(0.4, 12, 12)
    glRotatef(90, 0.0, 1.0, 0.0)
    glTranslated(1.2, 0.0, 0.0)
    glColor3f(1.0, 1.0, 1.0)
    # L'objet suivant subit 4 transformations
    glutSolidSphere(0.1, 12, 12)
    # Afficher le back buffer (ce qui est dessiné en arrière plan,
    # En cas de Single buffering, utiliser glFlush()
    glutSwapBuffers()


if __name__ == "__main__":
    main()
