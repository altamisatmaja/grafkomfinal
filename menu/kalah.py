from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w, h = 1380, 1000


def menang():
    glColor3f(238 / 255.0, 242 / 255.0, 150 / 255.0)
    glLineWidth(15)
    glBegin(GL_LINES)
    # g
    glVertex2f(100, 460)
    glVertex2f(280, 460)

    glVertex2f(280, 460)
    glVertex2f(280, 420)

    glVertex2f(280, 420)
    glVertex2f(160, 420)

    glVertex2f(160, 420)
    glVertex2f(140, 400)

    glVertex2f(140, 400)
    glVertex2f(140, 300)

    glVertex2f(140, 300)
    glVertex2f(160, 280)

    glVertex2f(160, 280)
    glVertex2f(240, 280)

    glVertex2f(240, 280)
    glVertex2f(260, 300)

    glVertex2f(260, 300)
    glVertex2f(260, 320)

    glVertex2f(260, 320)
    glVertex2f(240, 340)

    glVertex2f(240, 340)
    glVertex2f(180, 340)

    glVertex2f(180, 340)
    glVertex2f(180, 380)

    glVertex2f(180, 380)
    glVertex2f(300, 380)

    glVertex2f(300, 380)
    glVertex2f(300, 240)

    glVertex2f(300, 240)
    glVertex2f(100, 240)

    glVertex2f(100, 240)
    glVertex2f(100, 460)

    # A
    glVertex2f(380, 460)
    glVertex2f(460, 460)

    glVertex2f(460, 460)
    glVertex2f(480, 240)

    glVertex2f(480, 240)
    glVertex2f(440, 340)

    glVertex2f(440, 340)
    glVertex2f(400, 340)

    glVertex2f(400, 340)
    glVertex2f(360, 240)

    glVertex2f(360, 240)
    glVertex2f(380, 460)

    glVertex2f(400, 440)
    glVertex2f(440, 440)

    glVertex2f(440, 440)
    glVertex2f(440, 360)

    glVertex2f(440, 360)
    glVertex2f(400, 360)

    glVertex2f(400, 360)
    glVertex2f(400, 440)

    # M
    glVertex2f(540, 240)
    glVertex2f(540, 460)

    glVertex2f(540, 460)
    glVertex2f(580, 460)

    glVertex2f(660, 460)
    glVertex2f(700, 460)

    glVertex2f(700, 460)
    glVertex2f(700, 240)

    glVertex2f(700, 240)
    glVertex2f(660, 240)

    glVertex2f(660, 240)
    glVertex2f(660, 360)

    glVertex2f(580, 360)
    glVertex2f(580, 240)

    glVertex2f(580, 240)
    glVertex2f(540, 240)

    glVertex2f(540, 240)
    glVertex2f(540, 460)

    # E
    glVertex2f(760, 460)
    glVertex2f(900, 460)

    glVertex2f(900, 460)
    glVertex2f(900, 420)

    glVertex2f(900, 420)
    glVertex2f(800, 420)

    glVertex2f(800, 420)
    glVertex2f(800, 370)

    glVertex2f(800, 370)
    glVertex2f(900, 370)

    glVertex2f(900, 370)
    glVertex2f(900, 330)

    glVertex2f(900, 330)
    glVertex2f(800, 330)

    glVertex2f(800, 330)
    glVertex2f(800, 280)

    glVertex2f(800, 280)
    glVertex2f(900, 280)

    glVertex2f(900, 280)
    glVertex2f(900, 240)

    glVertex2f(900, 240)
    glVertex2f(760, 240)

    glVertex2f(760, 240)
    glVertex2f(760, 460)

    # O
    glVertex2f(300, 200)
    glVertex2f(360, 200)

    glVertex2f(360, 200)
    glVertex2f(380, 180)

    glVertex2f(380, 180)
    glVertex2f(380, 120)

    glVertex2f(380, 120)
    glVertex2f(360, 100)

    glVertex2f(360, 100)
    glVertex2f(300, 100)

    glVertex2f(300, 100)
    glVertex2f(280, 120)

    glVertex2f(280, 120)
    glVertex2f(280, 180)

    glVertex2f(280, 180)
    glVertex2f(300, 200)

    glVertex2f(320, 180)
    glVertex2f(340, 180)

    glVertex2f(340, 180)
    glVertex2f(360, 160)

    glVertex2f(360, 160)
    glVertex2f(360, 140)

    glVertex2f(360, 140)
    glVertex2f(340, 120)

    glVertex2f(340, 120)
    glVertex2f(320, 120)

    glVertex2f(320, 120)
    glVertex2f(300, 140)

    glVertex2f(300, 140)
    glVertex2f(300, 160)

    glVertex2f(300, 160)
    glVertex2f(320, 180)

    # V
    glVertex2f(420, 200)
    glVertex2f(460, 200)

    glVertex2f(460, 200)
    glVertex2f(460, 120)

    glVertex2f(460, 120)
    glVertex2f(500, 120)

    glVertex2f(500, 120)
    glVertex2f(500, 200)

    glVertex2f(500, 200)
    glVertex2f(540, 200)

    glVertex2f(540, 200)
    glVertex2f(520, 100)

    glVertex2f(520, 100)
    glVertex2f(440, 100)

    glVertex2f(440, 100)
    glVertex2f(420, 200)

    # E
    glVertex2f(580, 200)
    glVertex2f(640, 200)

    glVertex2f(640, 200)
    glVertex2f(640, 180)

    glVertex2f(640, 180)
    glVertex2f(600, 180)

    glVertex2f(600, 180)
    glVertex2f(600, 160)

    glVertex2f(600, 160)
    glVertex2f(640, 160)

    glVertex2f(640, 160)
    glVertex2f(640, 140)

    glVertex2f(640, 140)
    glVertex2f(600, 140)

    glVertex2f(600, 140)
    glVertex2f(600, 120)

    glVertex2f(600, 120)
    glVertex2f(640, 120)

    glVertex2f(640, 120)
    glVertex2f(640, 100)

    glVertex2f(640, 100)
    glVertex2f(580, 100)

    glVertex2f(580, 100)
    glVertex2f(580, 200)

    # R
    glVertex2f(680, 200)
    glVertex2f(720, 200)

    glVertex2f(720, 200)
    glVertex2f(740, 180)

    glVertex2f(740, 180)
    glVertex2f(740, 160)

    glVertex2f(740, 160)
    glVertex2f(720, 140)

    glVertex2f(720, 140)
    glVertex2f(740, 100)

    glVertex2f(740, 100)
    glVertex2f(700, 140)

    glVertex2f(700, 140)
    glVertex2f(700, 100)

    glVertex2f(700, 100)
    glVertex2f(680, 100)

    glVertex2f(680, 100)
    glVertex2f(680, 200)

    glVertex2f(700, 180)
    glVertex2f(720, 180)

    glVertex2f(720, 180)
    glVertex2f(720, 160)

    glVertex2f(720, 160)
    glVertex2f(700, 160)

    glVertex2f(700, 160)
    glVertex2f(700, 180)

    glEnd()

    glPointSize(40)
    glBegin(GL_POINTS)
    glVertex2f(120, 440)
    glVertex2f(120, 400)
    glVertex2f(120, 380)
    glVertex2f(120, 340)
    glVertex2f(120, 320)
    glVertex2f(120, 280)
    glVertex2f(120, 260)
    glVertex2f(160, 260)
    glVertex2f(200, 260)
    glVertex2f(240, 260)
    glVertex2f(128, 282)
    glVertex2f(140, 270)
    glVertex2f(150, 440)
    glVertex2f(180, 440)
    glVertex2f(200, 440)
    glVertex2f(220, 440)
    glVertex2f(240, 440)
    glVertex2f(260, 440)
    glVertex2f(138, 426)
    glVertex2f(126, 410)
    glVertex2f(270, 270)
    glVertex2f(270, 290)
    glVertex2f(270, 310)
    glVertex2f(270, 350)
    glVertex2f(270, 330)
    glVertex2f(240, 360)
    glVertex2f(270, 360)
    glVertex2f(200, 360)
    glVertex2f(290, 360)
    glVertex2f(290, 350)
    glVertex2f(290, 330)
    glVertex2f(290, 310)
    glVertex2f(290, 290)
    glVertex2f(290, 270)
    glEnd()
    glPointSize(30)
    glBegin(GL_POINTS)
    glVertex2f(390, 350)
    glVertex2f(450, 350)
    glVertex2f(420, 350)
    glVertex2f(120, 320)
    glVertex2f(420, 450)
    glVertex2f(445, 450)
    glVertex2f(395, 450)
    glVertex2f(386, 438)
    glVertex2f(386, 360)
    glVertex2f(386, 404)
    glVertex2f(386, 420)
    glVertex2f(386, 382)
    glVertex2f(451, 440)
    glVertex2f(452, 420)
    glVertex2f(452, 400)
    glVertex2f(452, 380)
    glVertex2f(455, 360)
    glVertex2f(385, 335)
    glVertex2f(375.5, 309.5)
    glVertex2f(375, 306)
    glVertex2f(456, 340)
    glVertex2f(463, 311)
    glVertex2f(466, 304)
    glEnd()
    glPointSize(40)
    glBegin(GL_POINTS)
    glVertex2f(560, 420)
    glVertex2f(560, 380)
    glVertex2f(560, 340)
    glVertex2f(560, 260)
    glVertex2f(560, 300)
    glVertex2f(560, 440)
    glVertex2f(680, 440)
    glVertex2f(680, 400)
    glVertex2f(680, 320)
    glVertex2f(680, 360)
    glVertex2f(680, 260)
    glVertex2f(680, 280)
    glVertex2f(580, 400)
    glVertex2f(620, 360)
    glVertex2f(660, 400)
    glVertex2f(580, 420)
    glVertex2f(580, 375)
    glVertex2f(660, 420)
    glVertex2f(606, 392)
    glVertex2f(634, 392)
    glVertex2f(660, 375)
    glEnd()
    glPointSize(40)
    glBegin(GL_POINTS)
    glVertex2f(880, 440)
    glVertex2f(840, 440)
    glVertex2f(800, 440)
    glVertex2f(780, 440)
    glVertex2f(780, 360)
    glVertex2f(780, 400)
    glVertex2f(780, 320)
    glVertex2f(780, 280)
    glVertex2f(820, 260)
    glVertex2f(860, 260)
    glVertex2f(880, 260)
    glVertex2f(780, 260)
    glVertex2f(880, 350)
    glVertex2f(850, 350)
    glVertex2f(800, 350)
    glVertex2f(820, 350)
    glEnd()


def dekorasi():
    glColor3f(238 / 255.0, 242 / 255.0, 150 / 255.0)
    glPointSize(30)
    glBegin(GL_POINTS)
    glVertex2f(910, 490)
    glVertex2f(980, 600)
    glVertex2f(960, 540)
    glVertex2f(1200, 300)
    glVertex2f(150, 150)
    glVertex2f(50, 50)
    glVertex2f(120, 80)
    glVertex2f(200, 50)
    glVertex2f(1000, 100)
    glVertex2f(1200, 400)
    glVertex2f
    glVertex2f(1000, 200)
    glVertex2f(1100, 300)
    glVertex2f(1100, 150)
    glVertex2f(1200, 700)
    glVertex2f
    glVertex2f
    glEnd()


def dekorasi2():
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(50)
    glBegin(GL_POINTS)
    glVertex2f(380, 10)
    glVertex2f(350, 10)
    glVertex2f(360, 10)
    glVertex2f(340, 10)
    glEnd()


def dekorasi3():
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(50)
    glBegin(GL_POINTS)
    glVertex2f(660, 20)
    glVertex2f(620, 20)
    glVertex2f(700, 20)
    glVertex2f(740, 20)
    glEnd()


def Tulisan1():
    glColor3f(238 / 255.0, 242 / 255.0, 150 / 255.0)
    glLineWidth(3)
    glBegin(GL_LINES)
    # T
    glVertex2f(290, 40)
    glVertex2f(290, 15)

    glVertex2f(280, 40)
    glVertex2f(300, 40)

    # R
    glVertex2f(305, 15)
    glVertex2f(305, 40)

    glVertex2f(305, 40)
    glVertex2f(315, 40)

    glVertex2f(315, 40)
    glVertex2f(315, 30)

    glVertex2f(315, 30)
    glVertex2f(305, 30)

    glVertex2f(305, 30)
    glVertex2f(315, 15)

    # Y
    glVertex2f(330, 40)
    glVertex2f(320, 15)

    glVertex2f(320, 40)
    glVertex2f(326, 32)
    # A
    glVertex2f(340, 15)
    glVertex2f(345, 40)

    glVertex2f(345, 40)
    glVertex2f(350, 40)

    glVertex2f(350, 40)
    glVertex2f(355, 15)

    glVertex2f(342.5, 27.5)
    glVertex2f(352.5, 27.5)
    # G
    glVertex2f(375, 40)
    glVertex2f(360, 40)

    glVertex2f(360, 40)
    glVertex2f(360, 15)

    glVertex2f(360, 15)
    glVertex2f(375, 15)

    glVertex2f(375, 15)
    glVertex2f(375, 25)

    glVertex2f(375, 25)
    glVertex2f(365, 25)
    # A
    glVertex2f(380, 15)
    glVertex2f(385, 40)

    glVertex2f(385, 40)
    glVertex2f(390, 40)

    glVertex2f(390, 40)
    glVertex2f(395, 15)

    glVertex2f(382.5, 27.5)
    glVertex2f(392.5, 27.5)

    # I
    glVertex2f(400, 40)
    glVertex2f(410, 40)

    glVertex2f(410, 15)
    glVertex2f(400, 15)

    glVertex2f(405, 40)
    glVertex2f(405, 15)

    # N

    glVertex2f(415, 15)
    glVertex2f(415, 40)

    glVertex2f(415, 40)
    glVertex2f(430, 15)

    glVertex2f(430, 15)
    glVertex2f(430, 40)

    glEnd()


def Tulisan2():
    glColor3f(238 / 255.0, 242 / 255.0, 150 / 255.0)
    glLineWidth(3)
    glBegin(GL_LINES)
    # E
    glVertex2f(15, 40)
    glVertex2f(0, 40)

    glVertex2f(0, 40)
    glVertex2f(0, 15)

    glVertex2f(0, 15)
    glVertex2f(15, 15)

    glVertex2f(14, 28)
    glVertex2f(0, 28)
    # X
    glVertex2f(20, 40)
    glVertex2f(40, 15)

    glVertex2f(40, 40)
    glVertex2f(20, 15)
    # I
    glVertex2f(45, 40)
    glVertex2f(55, 40)

    glVertex2f(50, 40)
    glVertex2f(50, 15)

    glVertex2f(45, 15)
    glVertex2f(55, 15)
    # T
    glVertex2f(60, 40)
    glVertex2f(70, 40)

    glVertex2f(65, 15)
    glVertex2f(65, 40)

    glEnd()


def iterate():
    glViewport(170, 250, w, h)  # Menggunakan layar yang diperbesar dua kali
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, w, 0.0, h, 0.0, 1.0)  # left, right, bottom, top
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


# Fungsi untuk menampilkan layar
def showScreen():
    glClearColor(0.0, 0.0, 0.0, 0.0)  # Set warna latar belakang menjadi putih (RGBA)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    menang()
    dekorasi()
    dekorasi2()
    dekorasi3()
    glTranslatef(300, 0, 0)
    glTranslatef(28, -15, 0)
    Tulisan1()
    Tulisan2()
    glutSwapBuffers()


# Inisialisasi GLUT
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(w, h)
glutInitWindowPosition(0, 0)
glutCreateWindow("KALAH")

# Daftarkan fungsi tampilan dan idle
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)

# Memulai loop utama GLUT
glutMainLoop()