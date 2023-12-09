from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image  # Make sure to install the Pillow library: pip install Pillow

w, h = 1280, 650
background_speed = 1.0 # Adjust the speed as needed
background_x = 0
background_texture = None  # Initialize texture ID
background_x2 = w

button_clicked = False

def check_button_click(x, y):
    global button_clicked

    button_x, button_y, button_width, button_height = 20, 0, 300, 120

    if button_x <= x <= button_x + button_width and button_y <= y <= button_y + button_height:
        button_clicked = True


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


def Buttton_Start():
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

def Judul_Game():
    glColor3f(117/255.0, 14/255.0, 33/255.0)
    glLineWidth(20)
    glBegin(GL_LINES)
    #M
    glVertex2f(20, 200)
    glVertex2f(20, 300)
    glVertex2f(100, 200)
    glVertex2f(100, 300)
    #A
    glVertex2f(140, 200)
    glVertex2f(140, 280)
    glVertex2f(150, 290)
    glVertex2f(190, 290)
    glVertex2f(200, 280)
    glVertex2f(200, 200)
    glVertex2f(150, 240)
    glVertex2f(190, 240)
    #R
    glVertex2f(240, 200)
    glVertex2f(240, 300)
    glVertex2f(240, 290)
    glVertex2f(290, 290)
    #I
    glVertex2f(340, 290)
    glVertex2f(380, 290)
    glVertex2f(340, 210)
    glVertex2f(380, 210)
    glVertex2f(360, 200)
    glVertex2f(360, 300)
    #O
    glVertex2f(420, 220)
    glVertex2f(420, 280)
    glVertex2f(430, 290)
    glVertex2f(470, 290)
    glVertex2f(480, 220)
    glVertex2f(480, 280)
    glVertex2f(430, 210)
    glVertex2f(470, 210)
    #B
    glVertex2f(580, 200)
    glVertex2f(580, 300)
    glVertex2f(580, 260)
    glVertex2f(620, 260)
    glVertex2f(580, 210)
    glVertex2f(620, 210)
    #R
    glVertex2f(670, 200)
    glVertex2f(670, 300)
    glVertex2f(670, 290)
    glVertex2f(720, 290)
    #O
    glVertex2f(770, 220)
    glVertex2f(770, 280)
    glVertex2f(780, 290)
    glVertex2f(820, 290)
    glVertex2f(830, 220)
    glVertex2f(830, 280)
    glVertex2f(780, 210)
    glVertex2f(820, 210)
    #S
    glVertex2f(880, 290)
    glVertex2f(920, 290)
    glVertex2f(880, 260)
    glVertex2f(920, 260)
    glVertex2f(880, 210)
    glVertex2f(920, 210)
    glEnd()

    glPointSize(20)
    glBegin(GL_POINTS)
    #M
    glVertex2f(40, 280)
    glVertex2f(60, 260)
    glVertex2f(60, 240)
    glVertex2f(80, 280)
    #R
    glVertex2f(300, 270)
    glVertex2f(280, 250)
    glVertex2f(260, 250)
    glVertex2f(300, 230)
    glVertex2f(300, 210)
    #B
    glVertex2f(600, 290)
    glVertex2f(620, 275)
    glVertex2f(630, 240)
    glVertex2f(630, 230)
    #R
    glVertex2f(730, 270)
    glVertex2f(710, 250)
    glVertex2f(690, 250)
    glVertex2f(730, 230)
    glVertex2f(730, 210)
    #S
    glVertex2f(870, 270)
    glVertex2f(930, 230)
    glVertex2f(930, 240)
    glVertex2f(870, 230)
    glEnd()

def iterate():
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, w, 0.0, h, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def mouse_click(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        check_button_click(x, y)


def draw_text(x, y, text, font):
    glRasterPos2f(x, y)
    for character in text:
        glutBitmapCharacter(font, ord(character))

def showScreen():
    global background_x, background_texture, button_clicked

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

    glTranslatef(160, 200, 0)
    Judul_Game()

    glTranslatef(300, -25, 0)
    Buttton_Start()

    # Check if the button is clicked
    if button_clicked:
        # Handle the button click here
        print("Button clicked!")

        # Reset button_clicked to False to avoid running the code multiple times
        button_clicked = False

    # Tentukan posisi dan teks yang ingin ditampilkan
    text_position_x = 82.5
    text_position_y = 52.5
    text_to_display = "START GAME"

    # Tentukan jenis font (Anda dapat mencoba GLUT_BITMAP_HELVETICA_18 atau jenis font lainnya)
    font = GLUT_BITMAP_TIMES_ROMAN_24

    # Atur warna teks
    glColor3f(1.0, 1.0, 1.0)

    # Gambar teks di atas tombol "Start Game"
    draw_text(text_position_x, text_position_y, text_to_display, font)

    glutSwapBuffers()


def update_background(value):
    glutPostRedisplay()
    glutTimerFunc(16, update_background, 0)

# Initialize GLUT
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(w, h)
glutInitWindowPosition(0, 0)
glutCreateWindow("Game Mario Bros")

# Register display function
glutDisplayFunc(showScreen)

glutMouseFunc(mouse_click)


# Start the background update loop
glutTimerFunc(0, update_background, 0)

# Start the main GLUT loop
glutMainLoop()
