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
# Illumination
ambianteGlobale = [0.7, 0.7, 0.7, 1.0]
diffuse_0 = [0.9, 0.9, 0.9, 1.0]
speculaire_0 = [1.0, 1.0, 1.0, 1.0]
position_0 = [0.0, 5.0, 5.0, 1.0]
flat = False
# Matériel: Cube
rouge = [1.0, 0.0, 0.0, 1.0]
vert = [0.0, 1.0, 0.0, 1.0]
bleu = [0.0, 0.0, 1.0, 1.0]
# Matériel : théière (cuivre)
m_ambiante = [0.19125, 0.0735, 0.0225, 1.0]
m_diffuse = [0.7038, 0.27048, 0.0828, 1.0]
m_speculaire = [0.256777, 0.137622, 0.086014, 1.0]
m_exposant = [128]


# valeur dans [0, 128]
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Lab 02a")
    ## Couleur du fond
    glClearColor(0.0, 0.0, 0.0, 1)
    glEnable(GL_DEPTH_TEST)
    # Illumination globale
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambianteGlobale)
    glEnable(GL_LIGHTING)
    # Avec l'activation de l'illumination, les propriétés
    # associées au matériel et les normales n'ont aucun effet
    # éliminer le commentaire suivant pour activer la source 0
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse_0)
    glLightfv(GL_LIGHT0, GL_SPECULAR, speculaire_0)
    glLightfv(GL_LIGHT0, GL_POSITION, position_0)
    glEnable(GL_LIGHT0)
    # Menu
    print("Tapez 'x', 'y' ou 'z' pour une translation selon un des axes.")
    print("Tapez sur une des flèshes, 'Page UP' ou 'Page Down' pour une rotation autour de x , y ou z.")
    print("Tapez 's' pour changer le sens de la rotation/translation")
    print("Tapez 'f' pour changer de mode d'ombrage")
    # CallBacks
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(fleches)
    glutReshapeFunc(reshape)
    glutMainLoop()


def unCube():
    global rouge, vert, bleu
    glBegin(GL_QUADS)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, rouge)
    glNormal3d(0, 0, 1)
    glVertex3d(-1, 1, 1)
    glVertex3d(-1, -1, 1)
    glVertex3d(1, -1, 1)
    glVertex3d(1, 1, 1)
    glNormal3d(0, 0, -1)
    glVertex3d(1, 1, -1)
    glVertex3d(1, -1, -1)
    glVertex3d(-1, -1, -1)
    glVertex3d(-1, 1, -1)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, vert)
    glNormal3d(1, 0, 0)
    glVertex3d(1, 1, 1)
    glVertex3d(1, -1, 1)
    glVertex3d(1, -1, -1)
    glVertex3d(1, 1, -1)
    glNormal3d(-1, 0, 0)
    glVertex3d(-1, 1, 1)
    glVertex3d(-1, 1, -1)
    glVertex3d(-1, -1, -1)
    glVertex3d(-1, -1, 1)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, bleu)
    glNormal3d(0, -1, 0)
    glVertex3d(-1, -1, 1)
    glVertex3d(-1, -1, -1)
    glVertex3d(1, -1, -1)
    glVertex3d(1, -1, 1)
    glNormal3d(0, 1, 0)
    glVertex3d(-1, 1, 1)
    glVertex3d(1, 1, 1)
    glVertex3d(1, 1, -1)
    glVertex3d(-1, 1, -1)
    glEnd()


def display():
    global bleu
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # Modèle d'ombrage
    if flat == True:
        glShadeModel(GL_FLAT)
    else:
        glShadeModel(GL_SMOOTH)
    # Afficher les 3 faces
    glLoadIdentity()
    glTranslatef(tx, ty, tz)
    glRotatef(anglex, 1.0, 0.0, 0.0)
    glRotatef(angley, 0.0, 1.0, 0.0)
    glRotatef(anglez, 0.0, 0.0, 1.0)
    # Exemple : 1
    # Cube : propirètés de refléctance diffuse
    # aspect spéculaire de la lumière sans effet
    # unCube()
    # Exemple : 2
    # Sphere: propirètés de refléctance diffuse
    # glMaterialfv(GL_FRONT, GL_DIFFUSE, bleu)
    # glutSolidSphere(2,24,24)
    # Exemple 3 :
    # Théière : propriétés de réflectance diffuse et spéculaire
    glMaterialfv(GL_FRONT,GL_AMBIENT,m_ambiante)
    glMaterialfv(GL_FRONT,GL_DIFFUSE,m_diffuse)
    glMaterialfv(GL_FRONT,GL_SPECULAR,m_speculaire)
    glMaterialfv(GL_FRONT,GL_SHININESS,m_exposant)
    glutSolidTeapot(1.5)
    glutSwapBuffers()


def reshape(w, h):
    # Où afficher sur l'écran (tout l'écran)
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Vue perspective (exemple 2)
    gluPerspective(90.0, w / h, 0.1, 25.0)
    gluLookAt(0.0, 4.0, 4.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glMatrixMode(GL_MODELVIEW)


def keyboard(key, x, y):
    global tx, ty, tz, signe, pasTranslate, flat
    if key == b"\x1b":  # Touche ESC
        exit(1)
    elif key == b"x":
        print("x")
        tx = tx + signe * pasTranslate
    elif key == b"y":
        ty += signe * pasTranslate
    elif key == b"z":
        print("z")
        tz += signe * pasTranslate
    elif key == b"s":  # Changer le sens de la translation
        signe *= -1
    elif key == b"f":  # Lambert vs Goraud
        if flat:
            flat = False
        else:
            flat = True
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
