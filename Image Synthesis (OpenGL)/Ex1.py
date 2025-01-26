from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

camera_pos = [5.0, 5.0, 5.0]  
camera_target = [1.0, 1.0, 0.0]  
camera_up = [0.0, 1.0, 0.0]  

control_points = [
    [[0.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 2.0, 0.0]],
    [[1.0, 0.0, 0.0], [1.0, 1.0, 1.0], [1.0, 2.0, 0.0]],
    [[2.0, 0.0, 0.0], [2.0, 1.0, 0.0], [2.0, 2.0, 0.0]]
]

current_point = [0, 0]  
step = 0.1  
sign = 1

def draw_control_points():
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 0.0)
    for i in range(3):
        for j in range(3):
            if i == current_point[0] and j == current_point[1]:
                glColor3f(1.0, 1.0, 0.0)
            else:
                glColor3f(1.0, 0.0, 0.0)
            glVertex3fv(control_points[i][j])
    glEnd()

def evaluate_bezier_surface(u, v):
    def bezier_basis(t):
        return [(1-t)**2, 2*t*(1-t), t**2]
    
    bu = bezier_basis(u)
    bv = bezier_basis(v)
    
    point = [0.0, 0.0, 0.0]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                point[k] += bu[i] * bv[j] * control_points[i][j][k]
    return point

def draw_bezier_surface():
    glColor3f(0.0, 0.0, 1.0)
    steps = 20
    
    for i in range(steps):
        u = i / float(steps-1)
        glBegin(GL_LINE_STRIP)
        for j in range(steps):
            v = j / float(steps-1)
            point = evaluate_bezier_surface(u, v)
            glVertex3fv(point)
        glEnd()
        
    for j in range(steps):
        v = j / float(steps-1)
        glBegin(GL_LINE_STRIP)
        for i in range(steps):
            u = i / float(steps-1)
            point = evaluate_bezier_surface(u, v)
            glVertex3fv(point)
        glEnd()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, w/h, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(camera_pos[0], camera_pos[1], camera_pos[2],
              camera_target[0], camera_target[1], camera_target[2],
              camera_up[0], camera_up[1], camera_up[2])
    
    draw_bezier_surface()
    draw_control_points()
    
    glutSwapBuffers()

def keyboard(key, x, y):
    global current_point, sign, camera_pos, camera_target
    
    key = key.decode('utf-8').lower()
    i, j = current_point
    
    if key == 'x':
        control_points[i][j][0] += sign * step
    elif key == 'y':
        control_points[i][j][1] += sign * step
    elif key == 'z':
        control_points[i][j][2] += sign * step
    elif key == '-':
        sign = -sign
    elif key == '\t':
        current_point[1] += 1
        if current_point[1] > 2:
            current_point[1] = 0
            current_point[0] += 1
            if current_point[0] > 2:
                current_point[0] = 0
    
    elif key == 'w':
        camera_pos[2] -= 0.5
    elif key == 'a':
        camera_pos[0] -= 0.5
    elif key == 's':
        camera_pos[2] += 0.5
    elif key == 'd':
        camera_pos[0] += 0.5
    elif key == 'q':
        camera_pos[1] += 0.5
    elif key == 'e':
        camera_pos[1] -= 0.5
    elif key == 'r':
        camera_pos = [5.0, 5.0, 5.0]
        camera_target = [1.0, 1.0, 0.0]
    
    glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Bezier Surface Control")
    
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()