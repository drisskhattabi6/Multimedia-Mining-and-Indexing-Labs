from time import sleep
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import cv2 as cv
import numpy as np

# Rotation
angleX = 0.0
angleY = 0.0
# Texture
ID = [0, 0, 0, 0, 0, 0]


def Init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glEnable(GL_DEPTH_TEST)
    # Texture
    glEnable(GL_TEXTURE_2D)
    loadImage()


def keyPressed(key, x, y):
    if key == b"\x1b":  # Touche ESC
        exit(1)


def DrawGLScene():
    global angleX, angleY, ID
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glRotatef(angleX, 1.0, 0.0, 0.0)
    glRotatef(angleY, 0.0, 1.0, 0.0)
    glBindTexture(GL_TEXTURE_2D, ID[0])
    glBegin(GL_QUADS)
    glTexCoord2i(0, 1)
    glVertex3f(-5.0, -5.0, -5.0)
    glTexCoord2i(1, 1)
    glVertex3f(5.0, -5.0, -5.0)
    glTexCoord2i(1, 0)
    glVertex3f(5.0, 5.0, -5.0)
    glTexCoord2i(0, 0)
    glVertex3f(-5.0, 5.0, -5.0)
    glEnd()
    # Left
    glBindTexture(GL_TEXTURE_2D, ID[1])
    glBegin(GL_QUADS)
    glTexCoord2i(1, 1)
    glVertex3f(-5.0, -5.0, -5.0)
    glTexCoord2i(1, 0)
    glVertex3f(-5.0, 5.0, -5.0)
    glTexCoord2i(0, 0)
    glVertex3f(-5.0, 5.0, 5.0)
    glTexCoord2i(0, 1)
    glVertex3f(-5.0, -5.0, 5.0)
    glEnd()
    # BACK
    glBindTexture(GL_TEXTURE_2D, ID[2])
    glBegin(GL_QUADS)
    glTexCoord2i(1, 1)
    glVertex3f(-5.0, -5.0, 5.0)
    glTexCoord2i(0, 1)
    glVertex3f(5.0, -5.0, 5.0)
    glTexCoord2i(0, 0)
    glVertex3f(5.0, 5.0, 5.0)
    glTexCoord2i(1, 0)
    glVertex3f(-5.0, 5.0, 5.0)
    glEnd()
    # Right
    glBindTexture(GL_TEXTURE_2D, ID[3])
    glBegin(GL_QUADS)
    glTexCoord2i(1, 1)
    glVertex3f(5.0, -5.0, 5.0)
    glTexCoord2i(0, 1)
    glVertex3f(5.0, -5.0, -5.0)
    glTexCoord2i(0, 0)
    glVertex3f(5.0, 5.0, -5.0)
    glTexCoord2i(1, 0)
    glVertex3f(5.0, 5.0, 5.0)
    glEnd()
    # up
    glBindTexture(GL_TEXTURE_2D, ID[4])
    glBegin(GL_QUADS)
    glTexCoord2i(1, 1)
    glVertex3f(5.0, 5.0, 5.0)
    glTexCoord2i(0, 1)
    glVertex3f(5.0, 5.0, -5.0)
    glTexCoord2i(0, 0)
    glVertex3f(-5.0, 5.0, -5.0)
    glTexCoord2i(1, 0)
    glVertex3f(-5.0, 5.0, 5.0)
    glEnd()
    # down
    glBindTexture(GL_TEXTURE_2D, ID[5])
    glBegin(GL_QUADS)
    glTexCoord2i(1, 1)
    glVertex3f(5.0, -5.0, 5.0)
    glTexCoord2i(0, 1)
    glVertex3f(5.0, -5.0, -5.0)
    glTexCoord2i(0, 0)
    glVertex3f(-5.0, -5.0, -5.0)
    glTexCoord2i(1, 0)
    glVertex3f(-5.0, -5.0, 5.0)
    glEnd()
    glutSwapBuffers()


def loadImage():
    global ID
    for i in range(0, 6):
        image = cv.imread("Image Synthesis (OpenGL)/prof-code/Lab3/skybox/" + str(i) + ".png", 1)
        ix = image.shape[0]
        iy = image.shape[1]
        ID[i] = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, ID[i])
        glTexImage2D(
            GL_TEXTURE_2D,
            0,
            3,
            ix, iy,
            0,
            GL_BGR,
            GL_UNSIGNED_BYTE,
            np.uint8(image).tobytes(),
        )
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)


def reshape(w, h):
    ## Où afficher sur l'écran (tout l'écran)
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    ## Vue perspective (exemple 2)
    gluPerspective(60.0, w / h, 0.1, 25.0)
    gluLookAt(0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0, 1.0, 0.0)
    glMatrixMode(GL_MODELVIEW)


def anime():
    global angleX, angleY
    # angleX = angleX + 2
    angleY = angleY + 2
    if angleY >= 360:
        angleY = 0
    if angleX >= 360:
        angleX = 0
    glutPostRedisplay()
    sleep(0.05)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(200, 200)
    glutCreateWindow(b"OpenGL: Texture")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(anime)
    glutKeyboardFunc(keyPressed)
    glutReshapeFunc(reshape)
    Init()
    glutMainLoop()


if __name__ == "__main__":
    main()
