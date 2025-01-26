from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from time import sleep


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_STENCIL)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Lab : Les buffers (3)")
    # Couleur du fond
    glClearColor(0.0, 0.0, 0.0, 1)
    # Activer le test de profondeur
    glEnable(GL_DEPTH_TEST)
    # CallBacks
    glutDisplayFunc(affiche)
    glutKeyboardFunc(keyboard)
    glutReshapeFunc(redim)
    glutMainLoop()


def axes():
    glLineStipple(3, 0xAAAA)
    glEnable(GL_LINE_STIPPLE)
    glLineWidth(3)
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


def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearStencil(0)


def affiche():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | GL_STENCIL_BUFFER_BIT)
    glLoadIdentity()
    axes()
    taille = 3.0
    ty = 1.0
    # L'objet déborde
    # glLoadIdentity();
    # glColor3f(1.0,0.0,0.0);
    # glTranslatef(0.,ty,0.);
    # glutSolidTeapot(0.5);
    # glLoadIdentity();
    # glColor3f(0.7,0.7,0.7);
    # glBegin(GL_QUADS);
    # glVertex3f(-(taille/2),0.0,-(taille/2));
    # glVertex3f(-(taille/2),0.0,(taille/2));
    # glVertex3f((taille/2),0.0,(taille/2));
    # glVertex3f((taille/2),0.0,-(taille/2));
    # glEnd();
    # glLoadIdentity();
    # glDisable(GL_DEPTH_TEST);
    # glColor3f(0.5,0.0,0.0);
    # glScalef(1.,-1.,1.);
    # glTranslatef(0.,ty,0.);
    # glutSolidTeapot(0.5);
    # glEnable(GL_DEPTH_TEST);
    # Si les deux le test de stencil et celui de pronfondeur réussissent on remplace
    glEnable(GL_STENCIL_TEST)
    glStencilFunc(GL_ALWAYS, 0x1, 0x1)
    glStencilOp(GL_KEEP, GL_KEEP, GL_REPLACE)
    glLoadIdentity()
    glColor3f(0.7, 0.7, 0.7)
    glBegin(GL_QUADS)
    glVertex3f(-(taille / 2), 0.0, -(taille / 2))
    glVertex3f(-(taille / 2), 0.0, (taille / 2))
    glVertex3f((taille / 2), 0.0, (taille / 2))
    glVertex3f((taille / 2), 0.0, -(taille / 2))
    glEnd()
    # Tracer les reflets (Sans test de profondeur)
    glStencilFunc(GL_EQUAL, 0x1, 0x1)
    glStencilOp(GL_KEEP, GL_KEEP, GL_KEEP)
    glDisable(GL_DEPTH_TEST)
    glLoadIdentity()
    glColor3f(1.0, 0.0, 0.0)
    glScalef(1.0, -1.0, 1.0)
    glTranslatef(0.0, ty, 0.0)
    glutSolidTeapot(0.5)
    glDisable(GL_STENCIL_TEST)
    glEnable(GL_DEPTH_TEST)
    glLoadIdentity()
    glColor3f(1.0, 0.0, 0.0)
    glTranslatef(0.0, ty, 0.0)
    glutSolidTeapot(0.5)
    glutSwapBuffers()


def redim(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-3.0, 3.0, -3.0, 3.0, -10.0, 10)
    gluLookAt(1.5, 1.5, 1.5, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glMatrixMode(GL_MODELVIEW)


def keyboard(key, x, y):
    if key == b"\x1b":  # Touche ESC
        exit(1)


if __name__ == "__main__":
    main()
