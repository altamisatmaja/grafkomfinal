from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w, h = 1380, 1000


def Buttton():
    glBegin(GL_POLYGON)
    glColor3f(68 / 255.0, 93 / 255.0, 72 / 255.0)
    glVertex2f(50, 300)
    glVertex2f(500, 300)

    glVertex2f(500, 300)
    glVertex2f(550, 250)

    glVertex2f(550, 250)
    glVertex2f(550, 150)

    glVertex2f(550, 150)
    glVertex2f(500, 100)

    glVertex2f(500, 100)
    glVertex2f(50, 100)

    glVertex2f(50, 100)
    glVertex2f(0, 150)

    glVertex2f(0, 150)
    glVertex2f(0, 250)

    glVertex2f(0, 250)
    glVertex2f(50, 300)
    glEnd()


def Tulisan_button():
    glColor3f(238 / 255.0, 242 / 255.0, 150 / 255.0)
    glLineWidth(5)
    glBegin(GL_LINES)
    # S
    glVertex2f(100, 280)
    glVertex2f(90, 290)

    glVertex2f(90, 290)
    glVertex2f(70, 290)

    glVertex2f(70, 290)
    glVertex2f(60, 280)

    glVertex2f(60, 280)
    glVertex2f(60, 260)

    glVertex2f(60, 260)
    glVertex2f(70, 250)

    glVertex2f(70, 250)
    glVertex2f(90, 250)

    glVertex2f(90, 250)
    glVertex2f(100, 240)

    glVertex2f(100, 240)
    glVertex2f(100, 220)

    glVertex2f(100, 220)
    glVertex2f(90, 210)

    glVertex2f(90, 210)
    glVertex2f(70, 210)

    glVertex2f(70, 210)
    glVertex2f(60, 220)
    # e
    glVertex2f(150, 290)
    glVertex2f(120, 290)

    glVertex2f(120, 290)
    glVertex2f(120, 210)

    glVertex2f(120, 210)
    glVertex2f(150, 210)

    glVertex2f(150, 250)
    glVertex2f(120, 250)
    # l
    glVertex2f(170, 290)
    glVertex2f(170, 210)

    glVertex2f(170, 210)
    glVertex2f(200, 210)

    # a
    glVertex2f(220, 210)
    glVertex2f(230, 290)

    glVertex2f(230, 290)
    glVertex2f(250, 290)

    glVertex2f(250, 290)
    glVertex2f(260, 210)

    glVertex2f(255, 250)
    glVertex2f(225, 250)
    # m
    glVertex2f(280, 210)
    glVertex2f(280, 290)

    glVertex2f(280, 290)
    glVertex2f(300, 250)

    glVertex2f(300, 250)
    glVertex2f(320, 290)

    glVertex2f(320, 290)
    glVertex2f(320, 210)

    # a
    glVertex2f(340, 210)
    glVertex2f(350, 290)

    glVertex2f(350, 290)
    glVertex2f(370, 290)

    glVertex2f(370, 290)
    glVertex2f(380, 210)

    glVertex2f(345, 250)
    glVertex2f(375, 250)

    # t
    glVertex2f(420, 210)
    glVertex2f(420, 290)

    glVertex2f(440, 290)
    glVertex2f(400, 290)

    # k
    glVertex2f(50, 180)
    glVertex2f(50, 140)

    glVertex2f(70, 180)
    glVertex2f(50, 160)

    glVertex2f(50, 160)
    glVertex2f(70, 140)

    # a
    glVertex2f(80, 140)
    glVertex2f(90, 180)

    glVertex2f(90, 180)
    glVertex2f(100, 180)

    glVertex2f(100, 180)
    glVertex2f(110, 140)

    glVertex2f(85, 160)
    glVertex2f(105, 160)

    # m
    glVertex2f(120, 140)
    glVertex2f(120, 180)

    glVertex2f(120, 180)
    glVertex2f(140, 160)

    glVertex2f(140, 160)
    glVertex2f(160, 180)

    glVertex2f(160, 180)
    glVertex2f(160, 140)

    # u
    glVertex2f(170, 180)
    glVertex2f(170, 140)

    glVertex2f(170, 140)
    glVertex2f(190, 140)

    glVertex2f(190, 140)
    glVertex2f(190, 180)

    # m
    glVertex2f(220, 140)
    glVertex2f(220, 180)

    glVertex2f(220, 180)
    glVertex2f(240, 160)

    glVertex2f(240, 160)
    glVertex2f(260, 180)

    glVertex2f(260, 180)
    glVertex2f(260, 140)

    # e
    glVertex2f(290, 180)
    glVertex2f(270, 180)

    glVertex2f(270, 180)
    glVertex2f(270, 140)

    glVertex2f(270, 140)
    glVertex2f(290, 140)

    glVertex2f(290, 160)
    glVertex2f(270, 160)

    # n
    glVertex2f(300, 140)
    glVertex2f(300, 180)

    glVertex2f(300, 180)
    glVertex2f(320, 140)

    glVertex2f(320, 140)
    glVertex2f(320, 180)

    # a
    glVertex2f(330, 140)
    glVertex2f(340, 180)

    glVertex2f(340, 180)
    glVertex2f(350, 180)

    glVertex2f(350, 180)
    glVertex2f(360, 140)

    glVertex2f(355, 160)
    glVertex2f(335, 160)

    # n
    glVertex2f(370, 140)
    glVertex2f(370, 180)

    glVertex2f(370, 180)
    glVertex2f(390, 140)

    glVertex2f(390, 140)
    glVertex2f(390, 180)

    # g
    glVertex2f(430, 180)
    glVertex2f(400, 180)

    glVertex2f(400, 180)
    glVertex2f(400, 140)

    glVertex2f(400, 140)
    glVertex2f(430, 140)

    glVertex2f(430, 140)
    glVertex2f(430, 160)

    glVertex2f(430, 160)
    glVertex2f(410, 160)

    glEnd()


def menang():
    glColor3f(238 / 255.0, 242 / 255.0, 150 / 255.0)
    glLineWidth(15)
    glBegin(GL_LINES)
    # F
    glVertex2f(60, 580)
    glVertex2f(160, 580)

    glVertex2f(160, 580)
    glVertex2f(160, 540)

    glVertex2f(160, 540)
    glVertex2f(100, 540)

    glVertex2f(100, 540)
    glVertex2f(100, 500)

    glVertex2f(100, 500)
    glVertex2f(160, 500)

    glVertex2f(160, 500)
    glVertex2f(160, 460)

    glVertex2f(160, 460)
    glVertex2f(100, 460)

    glVertex2f(100, 460)
    glVertex2f(100, 400)

    glVertex2f(100, 400)
    glVertex2f(60, 400)

    glVertex2f(60, 400)
    glVertex2f(60, 580)
    # I
    glVertex2f(180, 580)
    glVertex2f(280, 580)

    glVertex2f(280, 580)
    glVertex2f(280, 540)

    glVertex2f(280, 540)
    glVertex2f(240, 540)

    glVertex2f(240, 540)
    glVertex2f(240, 440)

    glVertex2f(240, 440)
    glVertex2f(280, 440)

    glVertex2f(280, 440)
    glVertex2f(280, 400)

    glVertex2f(280, 400)
    glVertex2f(180, 400)

    glVertex2f(180, 400)
    glVertex2f(180, 440)

    glVertex2f(180, 440)
    glVertex2f(220, 440)

    glVertex2f(220, 440)
    glVertex2f(220, 540)

    glVertex2f(220, 540)
    glVertex2f(180, 540)

    glVertex2f(180, 540)
    glVertex2f(180, 580)
    # N
    glVertex2f(300, 580)
    glVertex2f(360, 580)

    glVertex2f(360, 580)
    glVertex2f(360, 560)

    glVertex2f(360, 560)
    glVertex2f(380, 560)

    glVertex2f(380, 560)
    glVertex2f(380, 540)

    glVertex2f(380, 540)
    glVertex2f(400, 540)

    glVertex2f(400, 540)
    glVertex2f(400, 520)

    glVertex2f(400, 520)
    glVertex2f(420, 520)

    glVertex2f(420, 520)
    glVertex2f(420, 500)

    glVertex2f(420, 500)
    glVertex2f(440, 500)

    glVertex2f(440, 500)
    glVertex2f(440, 480)

    glVertex2f(440, 480)
    glVertex2f(460, 480)

    glVertex2f(460, 480)
    glVertex2f(460, 580)

    glVertex2f(460, 580)
    glVertex2f(500, 580)

    glVertex2f(500, 580)
    glVertex2f(500, 400)

    glVertex2f(500, 400)
    glVertex2f(420, 400)

    glVertex2f(420, 400)
    glVertex2f(420, 420)

    glVertex2f(420, 420)
    glVertex2f(400, 420)

    glVertex2f(400, 420)
    glVertex2f(400, 440)

    glVertex2f(400, 440)
    glVertex2f(380, 440)

    glVertex2f(380, 440)
    glVertex2f(380, 460)

    glVertex2f(380, 460)
    glVertex2f(360, 460)

    glVertex2f(360, 460)
    glVertex2f(360, 480)

    glVertex2f(360, 480)
    glVertex2f(340, 480)

    glVertex2f(340, 480)
    glVertex2f(340, 400)

    glVertex2f(340, 400)
    glVertex2f(300, 400)

    glVertex2f(300, 400)
    glVertex2f(300, 580)
    # I
    glVertex2f(520, 580)
    glVertex2f(620, 580)

    glVertex2f(620, 580)
    glVertex2f(620, 540)

    glVertex2f(620, 540)
    glVertex2f(580, 540)

    glVertex2f(580, 540)
    glVertex2f(580, 440)

    glVertex2f(580, 440)
    glVertex2f(620, 440)

    glVertex2f(620, 440)
    glVertex2f(620, 400)

    glVertex2f(620, 400)
    glVertex2f(520, 400)

    glVertex2f(520, 400)
    glVertex2f(520, 440)

    glVertex2f(520, 440)
    glVertex2f(560, 440)

    glVertex2f(560, 440)
    glVertex2f(560, 540)

    glVertex2f(560, 540)
    glVertex2f(520, 540)

    glVertex2f(520, 540)
    glVertex2f(520, 580)

    # S
    glVertex2f(700, 580)
    glVertex2f(800, 580)

    glVertex2f(800, 580)
    glVertex2f(800, 540)

    glVertex2f(800, 540)
    glVertex2f(700, 540)

    glVertex2f(700, 540)
    glVertex2f(700, 580)

    glVertex2f(660, 540)
    glVertex2f(700, 540)

    glVertex2f(700, 540)
    glVertex2f(700, 500)

    glVertex2f(700, 500)
    glVertex2f(660, 500)

    glVertex2f(660, 500)
    glVertex2f(660, 540)

    glVertex2f(700, 500)
    glVertex2f(760, 500)

    glVertex2f(760, 500)
    glVertex2f(760, 470)

    glVertex2f(760, 470)
    glVertex2f(700, 470)

    glVertex2f(700, 470)
    glVertex2f(700, 500)

    glVertex2f(760, 480)
    glVertex2f(800, 480)

    glVertex2f(800, 480)
    glVertex2f(800, 440)

    glVertex2f(800, 440)
    glVertex2f(760, 440)

    glVertex2f(760, 440)
    glVertex2f(760, 480)

    glVertex2f(680, 440)
    glVertex2f(780, 440)

    glVertex2f(780, 440)
    glVertex2f(780, 400)

    glVertex2f(780, 400)
    glVertex2f(680, 400)

    glVertex2f(680, 400)
    glVertex2f(680, 440)

    # H
    glVertex2f(840, 580)
    glVertex2f(880, 580)

    glVertex2f(880, 580)
    glVertex2f(880, 520)

    glVertex2f(880, 520)
    glVertex2f(900, 520)

    glVertex2f(900, 520)
    glVertex2f(900, 500)

    glVertex2f(900, 500)
    glVertex2f(920, 500)

    glVertex2f(920, 500)
    glVertex2f(920, 520)

    glVertex2f(920, 520)
    glVertex2f(940, 520)

    glVertex2f(940, 520)
    glVertex2f(940, 580)

    glVertex2f(940, 580)
    glVertex2f(980, 580)

    glVertex2f(980, 580)
    glVertex2f(980, 400)

    glVertex2f(980, 400)
    glVertex2f(940, 400)

    glVertex2f(940, 400)
    glVertex2f(940, 460)

    glVertex2f(940, 460)
    glVertex2f(920, 460)

    glVertex2f(920, 460)
    glVertex2f(920, 480)

    glVertex2f(920, 480)
    glVertex2f(900, 480)

    glVertex2f(900, 480)
    glVertex2f(900, 460)

    glVertex2f(900, 460)
    glVertex2f(880, 460)

    glVertex2f(880, 460)
    glVertex2f(880, 400)

    glVertex2f(880, 400)
    glVertex2f(840, 400)

    glVertex2f(840, 400)
    glVertex2f(840, 580)
    glEnd()


def dekorasi():
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(35)
    glBegin(GL_POINTS)
    glVertex2f(530, 3)
    glVertex2f(532, 3)
    glVertex2f(534, 3)
    glVertex2f(536, 3)
    glVertex2f(540, 3)
    glVertex2f(543, 3)
    glVertex2f(546, 3)
    glVertex2f(549, 3)
    glEnd()


def dekorasi2():
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(35)
    glBegin(GL_POINTS)
    glVertex2f(75, 3)
    glVertex2f(62, 3)
    glVertex2f(55, 3)
    glVertex2f(50, 3)
    glVertex2f
    glVertex2f
    glVertex2f
    glVertex2f
    glEnd()


def dekorasi3():
    glColor3f(238 / 255.0, 242 / 255.0, 150 / 255.0)
    glPointSize(35)
    glBegin(GL_POINTS)
    glVertex2f(700, 350)
    glVertex2f
    glVertex2f(900, 500)
    glVertex2f(800, 400)
    glVertex2f(600, 300)
    glVertex2f(800, 200)
    glVertex2f
    glVertex2f(750, 600)
    glVertex2f(0.5, 62)
    glVertex2f
    glVertex2f(10, 80)
    glVertex2f(2, 354)
    glEnd()


def Tulisan1():
    glColor3f(238 / 255.0, 242 / 255.0, 150 / 255.0)
    glLineWidth(3)
    glBegin(GL_LINES)
    # n
    glVertex2f(490, 15)
    glVertex2f(490, 30)

    glVertex2f(490, 30)
    glVertex2f(500, 15)

    glVertex2f(500, 15)
    glVertex2f(500, 30)

    # e
    glVertex2f(510, 30)
    glVertex2f(505, 30)

    glVertex2f(505, 30)
    glVertex2f(505, 15)

    glVertex2f(505, 15)
    glVertex2f(510, 15)

    glVertex2f(505, 22)
    glVertex2f(510, 22)

    # X
    glVertex2f(524, 30)
    glVertex2f(514, 15)

    glVertex2f(514, 30)
    glVertex2f(524, 15)

    # t
    glVertex2f(527, 30)
    glVertex2f(536, 30)

    glVertex2f(532, 30)
    glVertex2f(532, 15)

    glEnd()


def Tulisan2():
    glColor3f(238 / 255.0, 242 / 255.0, 150 / 255.0)
    glLineWidth(3)
    glBegin(GL_LINES)
    # m
    glVertex2f(10, 15)
    glVertex2f(10, 30)

    glVertex2f(10, 30)
    glVertex2f(15, 25)

    glVertex2f(15, 25)
    glVertex2f(20, 30)

    glVertex2f(20, 30)
    glVertex2f(20, 15)

    # e
    glVertex2f(32, 30)
    glVertex2f(25, 30)

    glVertex2f(25, 30)
    glVertex2f(25, 15)

    glVertex2f(25, 15)
    glVertex2f(32, 15)

    glVertex2f(25, 22)
    glVertex2f(32, 22)

    # N
    glVertex2f(35, 15)
    glVertex2f(35, 30)

    glVertex2f(35, 30)
    glVertex2f(45, 15)

    glVertex2f(45, 15)
    glVertex2f(45, 30)

    # U
    glVertex2f(50, 30)
    glVertex2f(50, 15)

    glVertex2f(50, 15)
    glVertex2f(60, 15)

    glVertex2f(60, 15)
    glVertex2f(60, 30)

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
    glTranslatef(300, 0, 0)
    Buttton()
    dekorasi()
    dekorasi2()
    dekorasi3()
    glTranslatef(28, -15, 0)
    Tulisan_button()
    Tulisan1()
    Tulisan2()
    glutSwapBuffers()


# Inisialisasi GLUT
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(w, h)
glutInitWindowPosition(0, 0)
glutCreateWindow("MENANG")

# Daftarkan fungsi tampilan dan idle
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)

# Memulai loop utama GLUT
glutMainLoop()