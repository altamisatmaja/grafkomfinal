from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image  # Make sure to install the Pillow library: pip install Pillow

w, h = 1280, 650
background_speed = 1.0 # Adjust the speed as needed
background_x = 0
background_texture = None  # Initialize texture ID
background_x2 = w

def load_texture(image):
    image_data = image.convert("RGBA").tobytes("raw", "RGBA", 0, -1)
    glBindTexture(GL_TEXTURE_2D, background_texture)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

def draw_background():
    global background_x, background_x2

    glEnable(GL_TEXTURE_2D)

    glBindTexture(GL_TEXTURE_2D, background_texture)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex2f(background_x, 0)
    glTexCoord2f(1, 0); glVertex2f(background_x + w, 0)
    glTexCoord2f(1, 1); glVertex2f(background_x + w, h)
    glTexCoord2f(0, 1); glVertex2f(background_x, h)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, background_texture)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex2f(background_x2, 0)
    glTexCoord2f(1, 0); glVertex2f(background_x2 + w, 0)
    glTexCoord2f(1, 1); glVertex2f(background_x2 + w, h)
    glTexCoord2f(0, 1); glVertex2f(background_x2, h)
    glEnd()

    glDisable(GL_TEXTURE_2D)

    # Check if the first background has reached the end
    if background_x <= -w:
        background_x = w

    # Check if the second background has reached the end
    if background_x2 <= 0:
        background_x2 = w

    background_x -= background_speed
    background_x2 -= background_speed

def Button():
    glBegin(GL_POLYGON)
    glColor3f(68/255.0, 93/255.0, 72/255.0)
    glVertex2f(20, 0)
    glVertex2f(0, 20)
    glVertex2f(0, 100)
    glVertex2f(20, 120)
    glVertex2f(300, 120)
    glVertex2f(320, 100)
    glVertex2f(320, 20)
    glVertex2f(300, 0)
    glEnd()

def Level():
    glColor3f(238/255.0, 242/255.0, 150/255.0)
    glLineWidth(5)
    glBegin(GL_LINES)
    #L
    glVertex2f(30, 100)
    glVertex2f(30, 52.5)
    glVertex2f(30, 50)
    glVertex2f(60, 50)
    #E
    glVertex2f(70, 97.5)
    glVertex2f(70, 52.5)
    glVertex2f(72.5, 100)
    glVertex2f(95, 100)
    glVertex2f(72.5, 75)
    glVertex2f(95, 75)
    glVertex2f(72.5, 50)
    glVertex2f(95, 50)
    #V
    glVertex2f(105, 100)
    glVertex2f(105, 80)
    glVertex2f(110, 80)
    glVertex2f(110, 70)
    glVertex2f(115, 70)
    glVertex2f(115, 60)
    glVertex2f(120, 60)
    glVertex2f(120, 50)
    glVertex2f(125, 70)
    glVertex2f(125, 60)
    glVertex2f(130, 80)
    glVertex2f(130, 70)
    glVertex2f(135, 100)
    glVertex2f(135, 80)
    #E
    glVertex2f(145, 97.5)
    glVertex2f(145, 52.5)
    glVertex2f(147.5, 100)
    glVertex2f(170, 100)
    glVertex2f(147.5, 75)
    glVertex2f(170, 75)
    glVertex2f(147.5, 50)
    glVertex2f(170, 50)
    #L
    glVertex2f(180, 100)
    glVertex2f(180, 52.5)
    glVertex2f(180, 50)
    glVertex2f(210, 50)
    glEnd()

def Angka_1():
    glColor3f(238/255.0, 242/255.0, 150/255.0)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(225, 90)
    glVertex2f(235, 90)
    glVertex2f(235, 100)
    glVertex2f(235, 50)
    glEnd()

def Angka_2():
    glColor3f(238/255.0, 242/255.0, 150/255.0)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(225, 95)
    glVertex2f(225, 80)
    glVertex2f(227.5, 97.5)
    glVertex2f(250, 97.5)
    glVertex2f(252.5, 95)
    glVertex2f(252.5, 70)
    glVertex2f(230, 67.5)
    glVertex2f(250, 67.5)
    glVertex2f(227.5, 65)
    glVertex2f(227.5, 47.5)
    glVertex2f(225, 50)
    glVertex2f(255, 50)
    glEnd()

def Angka_3():
    glColor3f(238/255.0, 242/255.0, 150/255.0)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(225, 95)
    glVertex2f(225, 80)
    glVertex2f(227.5, 97.5)
    glVertex2f(250, 97.5)
    glVertex2f(252.5, 95)
    glVertex2f(252.5, 80)
    glVertex2f(240, 72.5)
    glVertex2f(250, 72.5)
    glVertex2f(252.5, 70)
    glVertex2f(252.5, 52.5)
    glVertex2f(227.5, 50)
    glVertex2f(250, 50)
    glVertex2f(225, 52.5)
    glVertex2f(225, 65)
    glEnd()

def iterate():
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, w, 0.0, h, 0.0, 1.0)  # left, right, bottom, top
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def draw_text(x, y, text, font):
    glRasterPos2f(x, y)
    for character in text:
        glutBitmapCharacter(font, ord(character))

# Fungsi untuk menampilkan layar
def showScreen():
    global background_x, background_texture

    if background_texture is None:
        # Generate texture ID
        background_texture = glGenTextures(1)

        # JANGAN LUPA DIGANTI PATH NYA
        background_image = Image.open("assets/backgroundmenu.png")
        load_texture(background_image)

    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    # Draw the moving background
    draw_background()
    background_x -= background_speed
    if background_x <= -w:
        background_x = 0
        # Tentukan posisi dan teks yang ingin ditampilkan
    text_position_x = 230
    text_position_y = 600
    text_to_display = "PILIHLAH LEVEL GAME KALIAN! MULAILAH DARI LEVEL TERMUDAH!"

    # Tentukan jenis font (Anda dapat mencoba GLUT_BITMAP_HELVETICA_18 atau jenis font lainnya)
    font = GLUT_BITMAP_TIMES_ROMAN_24

    # Atur warna teks
    glColor3f(1.0, 1.0, 1.0)

    # Gambar teks di atas tombol "Start Game"
    draw_text(text_position_x, text_position_y, text_to_display, font)

    # Menggeser Level, Angka_1, Angka_2, dan Angka_3 tanpa menggeser Button
    glPushMatrix()  # Simpan matriks saat ini
    glTranslatef(450, 50, 0)
    Button()
    glTranslatef(20, -15, 0)
    Level()
    Angka_3()
    glPopMatrix()  # Kembalikan matriks ke kondisi sebelumnya
    
    glPushMatrix()  # Simpan matriks saat ini
    glTranslatef(450, 230, 0)
    Button()
    glTranslatef(20, -15, 0)
    Level()
    Angka_2()
    glPopMatrix()  # Kembalikan matriks ke kondisi sebelumnya

    glPushMatrix()  # Simpan matriks saat ini
    glTranslatef(450, 410, 0)
    Button()
    glTranslatef(20, -15, 0)
    Level()
    Angka_1()
    glPopMatrix()  # Kembalikan matriks ke kondisi sebelumnya
    
    
    glutSwapBuffers()

def update_background(value):
    glutPostRedisplay()
    glutTimerFunc(16, update_background, 0)

# Inisialisasi GLUT
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(w, h)
glutInitWindowPosition(0, 0)
glutCreateWindow("Game Mario Bros")

# Daftarkan fungsi tampilan dan idle
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
# Start the background update loop
glutTimerFunc(0, update_background, 0)
# Memulai loop utama GLUT
glutMainLoop()