import math
from OpenGL.GL import *
from OpenGL.GLU import *

def init_environment():
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_NORMALIZE)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_LIGHTING)

    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, [5.0, 8.0, 5.0, 1.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 0.9, 0.7, 1.0]) 
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])

    glEnable(GL_LIGHT1)
    glLightfv(GL_LIGHT1, GL_POSITION, [-5.0, 0.0, 5.0, 1.0])
    glLightfv(GL_LIGHT1, GL_DIFFUSE, [0.2, 0.2, 0.4, 1.0])

    glEnable(GL_LIGHT2)
    glLightfv(GL_LIGHT2, GL_POSITION, [0.0, 5.0, -5.0, 1.0])
    glLightfv(GL_LIGHT2, GL_DIFFUSE, [0.8, 0.5, 0.2, 1.0])
    glLightfv(GL_LIGHT2, GL_SPECULAR, [1.0, 0.8, 0.4, 1.0])

def set_material(mat_type, color=(1,1,1,1)):
    glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, [0,0,0,1])
    if mat_type == "chrome":
        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, color)
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
        glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 100.0)
    elif mat_type == "matte":
        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, color)
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [0.1, 0.1, 0.1, 1.0])
        glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 10.0)
    elif mat_type == "emission":
        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, color)
        glMaterialfv(GL_FRONT_AND_BACK, GL_EMISSION, color)

def draw_cube():
    glBegin(GL_QUADS)
    glNormal3f(0,0,1); glVertex3f(-0.5,-0.5,0.5); glVertex3f(0.5,-0.5,0.5); glVertex3f(0.5,0.5,0.5); glVertex3f(-0.5,0.5,0.5)
    glNormal3f(0,0,-1); glVertex3f(-0.5,-0.5,-0.5); glVertex3f(-0.5,0.5,-0.5); glVertex3f(0.5,0.5,-0.5); glVertex3f(0.5,-0.5,-0.5)
    glNormal3f(0,1,0); glVertex3f(-0.5,0.5,-0.5); glVertex3f(-0.5,0.5,0.5); glVertex3f(0.5,0.5,0.5); glVertex3f(0.5,0.5,-0.5)
    glNormal3f(0,-1,0); glVertex3f(-0.5,-0.5,-0.5); glVertex3f(0.5,-0.5,-0.5); glVertex3f(0.5,-0.5,0.5); glVertex3f(-0.5,-0.5,0.5)
    glNormal3f(1,0,0); glVertex3f(0.5,-0.5,-0.5); glVertex3f(0.5,0.5,-0.5); glVertex3f(0.5,0.5,0.5); glVertex3f(0.5,-0.5,0.5)
    glNormal3f(-1,0,0); glVertex3f(-0.5,-0.5,-0.5); glVertex3f(-0.5,-0.5,0.5); glVertex3f(-0.5,0.5,0.5); glVertex3f(-0.5,0.5,-0.5)
    glEnd()

def draw_room():
    # LANTAI (Y disesuaikan ke -4.91 biar permukaan pas sama kertasmu -4.86)
    glPushMatrix()
    set_material("matte", (0.4, 0.4, 0.42, 1.0)) 
    glTranslatef(0, -4.91, 7.0) 
    glScalef(31.0, 0.1, 31.0) 
    draw_cube()
    glPopMatrix()

    list_color = (0.2, 0.1, 0.05, 1.0)

    # LIST LANTAI 
    glPushMatrix()
    set_material("matte", list_color)
    glTranslatef(0.0, -4.76, -7.8); glScalef(31.0, 0.4, 0.4); draw_cube()
    glPopMatrix()
    glPushMatrix()
    set_material("matte", list_color)
    glTranslatef(0.0, -4.76, 21.8); glScalef(31.0, 0.4, 0.4); draw_cube()
    glPopMatrix()
    glPushMatrix()
    set_material("matte", list_color)
    glTranslatef(-14.8, -4.76, 7.0); glScalef(0.4, 0.4, 31.0); draw_cube()
    glPopMatrix()
    glPushMatrix()
    set_material("matte", list_color)
    glTranslatef(14.8, -4.76, 7.0); glScalef(0.4, 0.4, 31.0); draw_cube()
    glPopMatrix()

    # PLAFON
    glPushMatrix()
    set_material("matte", (0.85, 0.85, 0.85, 1.0)) 
    glTranslatef(0, 10.0, 7.0); glScalef(31.0, 0.1, 31.0); draw_cube()
    glPopMatrix()

    # DINDING BELAKANG
    glPushMatrix()
    set_material("matte", (0.1, 0.2, 0.15, 1.0)) 
    glTranslatef(0, 2.5, -8.0); glScalef(31.0, 15.0, 0.5); draw_cube()
    glPopMatrix()

    # PIGURA 1 & 2
    glPushMatrix()
    glTranslatef(0.0, 5.0, -7.7); set_material("matte", (0.2, 0.1, 0.05, 1.0)); glScalef(6.2, 3.7, 0.2); draw_cube()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0.0, 5.0, -7.4); set_material("matte", (0.9, 0.85, 0.75, 1.0)); glScalef(5.8, 3.3, 0.1); draw_cube()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(4.0, 6.0, -7.7); set_material("matte", (0.1, 0.1, 0.1, 1.0)); glScalef(2.0, 2.0, 0.2); draw_cube()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(4.0, 6.0, -7.4); set_material("matte", (0.95, 0.95, 0.95, 1.0)); glScalef(1.8, 1.8, 0.1); draw_cube()
    glPopMatrix()
    
    # --- JENDELA RETRO V2 (DI DINDING KIRI) ---
    glPushMatrix()
    glTranslatef(-14.8, 5.0, 7.0) 
    
    # Kaca Bercahaya Biru Pucat (Cahaya Bulan)
    set_material("emission", (0.2, 0.35, 0.45, 1.0)) 
    glPushMatrix()
    glScalef(0.1, 8.0, 12.0) 
    draw_cube()
    glPopMatrix()

    # Kusen Utama
    set_material("matte", list_color) 
    glPushMatrix(); glTranslatef(0.1, 4.1, 0.0); glScalef(0.3, 0.4, 12.4); draw_cube(); glPopMatrix()
    glPushMatrix(); glTranslatef(0.1, -4.1, 0.0); glScalef(0.3, 0.4, 12.4); draw_cube(); glPopMatrix()
    glPushMatrix(); glTranslatef(0.1, 0.0, 6.1); glScalef(0.3, 8.0, 0.4); draw_cube(); glPopMatrix()
    glPushMatrix(); glTranslatef(0.1, 0.0, -6.1); glScalef(0.3, 8.0, 0.4); draw_cube(); glPopMatrix()
    
    # Teralis Tengah (Grid 3x2)
    glPushMatrix(); glTranslatef(0.15, 0.0, -2.0); glScalef(0.2, 8.0, 0.2); draw_cube(); glPopMatrix()
    glPushMatrix(); glTranslatef(0.15, 0.0, 2.0); glScalef(0.2, 8.0, 0.2); draw_cube(); glPopMatrix()
    glPushMatrix(); glTranslatef(0.15, 0.0, 0.0); glScalef(0.2, 0.2, 12.0); draw_cube(); glPopMatrix()

    # Ambang Jendela (Sill) - Menonjol ke dalam ruangan
    glPushMatrix()
    glTranslatef(0.4, -4.3, 0.0) 
    glScalef(1.2, 0.2, 13.0) 
    draw_cube()
    glPopMatrix()

    glPopMatrix()
    # ------------------------------------------

    # DINDING DEPAN, KIRI, KANAN
    glPushMatrix()
    set_material("matte", (0.1, 0.2, 0.15, 1.0)); glTranslatef(0, 2.5, 22.0); glScalef(31.0, 15.0, 0.5); draw_cube()
    glPopMatrix()
    glPushMatrix()
    set_material("matte", (0.08, 0.18, 0.13, 1.0)); glTranslatef(-15.0, 2.5, 7.0); glScalef(0.5, 15.0, 31.0); draw_cube()
    glPopMatrix()
    glPushMatrix()
    set_material("matte", (0.08, 0.18, 0.13, 1.0)); glTranslatef(15.0, 2.5, 7.0); glScalef(0.5, 15.0, 31.0); draw_cube()
    glPopMatrix()

def draw_table():
    # Papan Meja (Y disesuaikan ke -2.81 biar permukaan pas sama kertasmu -2.76)
    glPushMatrix()
    set_material("matte", (0.35, 0.2, 0.1, 1.0))
    glTranslatef(0, -2.81, 0)
    glScalef(6.0, 0.1, 4.0) 
    draw_cube()
    glPopMatrix()
    
    # Kaki Meja
    quadric = gluNewQuadric()
    positions = [(-2.5, -4.86, 1.5), (2.5, -4.86, 1.5), (-2.5, -4.86, -1.5), (2.5, -4.86, -1.5)]
    for pos in positions:
        glPushMatrix()
        set_material("matte", (0.2, 0.1, 0.05, 1.0))
        glTranslatef(*pos)
        glRotatef(-90, 1, 0, 0)
        gluCylinder(quadric, 0.15, 0.15, 2.05, 16, 16) 
        glPopMatrix()

    # Buku Kiri
    glPushMatrix()
    set_material("matte", (0.1, 0.2, 0.3, 1.0)); glTranslatef(-1.8, -2.72, 0.0); glRotatef(15, 0, 1, 0); glScalef(1.2, 0.15, 1.6); draw_cube()
    glPopMatrix()
    glPushMatrix()
    set_material("matte", (0.6, 0.2, 0.15, 1.0)); glTranslatef(-1.8, -2.57, 0.0); glRotatef(-10, 0, 1, 0); glScalef(1.0, 0.15, 1.4); draw_cube()
    glPopMatrix()

    # Mug Kanan
    glPushMatrix()
    set_material("matte", (0.1, 0.4, 0.2, 1.0)) 
    glTranslatef(1.8, -2.76, 0.0) 
    glRotatef(-90, 1, 0, 0) 
    gluCylinder(quadric, 0.2, 0.2, 0.4, 16, 16) 
    gluDisk(quadric, 0, 0.2, 16, 1) 
    glPopMatrix()

def draw_socket_and_cable():
    glPushMatrix(); set_material("matte", (0.9, 0.9, 0.9, 1.0)); glTranslatef(3.0, -0.5, -7.7); glScalef(0.5, 0.7, 0.2); draw_cube(); glPopMatrix()
    glPushMatrix(); set_material("matte", (0.1, 0.1, 0.1, 1.0)); glTranslatef(0, 0, 0.51); glScalef(0.4, 0.4, 0.1); draw_cube(); glPopMatrix()

    set_material("matte", (0.1, 0.1, 0.1, 1.0))
    glLineWidth(3.0)
    glBegin(GL_LINE_STRIP)
    for i in range(200):
        t = i / 199.0 
        base_x = 0.0 + t * (3.0 - 0.0)
        base_z = -1.2 + t * (-7.6 - (-1.2))
        base_y = -2.6 + t * (-0.5 - (-2.6)) - (math.sin(t * math.pi) * 0.2) 
        radius = 0.08 if 0.05 < t < 0.95 else 0.0
        x = base_x + math.cos(t * 80) * radius
        y = base_y + math.sin(t * 80) * radius
        z = base_z
        glVertex3f(x, y, z)
    glEnd()
    glLineWidth(1.0)

def draw_flying_papers(time_counter, wind_power, fan_speed_level, head_pan_angle):
    set_material("matte", (0.95, 0.95, 0.95, 1.0)) 
    def lerp(start, end, t): return start + (end - start) * t
    wind_drift = head_pan_angle * 0.05

    rest_A = (-4.0, -4.84, 2.0) 
    fly_A = (-3.5 + math.sin(time_counter)*0.5 + wind_drift, 1.5 + math.cos(time_counter*2)*0.5, 1.0)
    glPushMatrix()
    glTranslatef(lerp(rest_A[0], fly_A[0], wind_power), lerp(rest_A[1], fly_A[1], wind_power), lerp(rest_A[2], fly_A[2], wind_power))
    glRotatef(45, 0, 1, 0) 
    glRotatef(lerp(0, time_counter * 100 * max(1, fan_speed_level), wind_power), 1, 0, 1) 
    glScalef(0.5, 0.01, 0.7)
    draw_cube()
    glPopMatrix()

    rest_B = (1.8, -2.74, 0.5) 
    fly_B = (2.5 + math.sin(time_counter*3)*0.3 + wind_drift, 0.5 + math.sin(time_counter*3)*0.3, 2.0)
    glPushMatrix()
    glTranslatef(lerp(rest_B[0], fly_B[0], wind_power), lerp(rest_B[1], fly_B[1], wind_power), lerp(rest_B[2], fly_B[2], wind_power))
    glRotatef(-20, 0, 1, 0) 
    glRotatef(lerp(0, time_counter * 80 * max(1, fan_speed_level), wind_power), 1, 1, 0) 
    glScalef(0.5, 0.01, 0.7)
    draw_cube()
    glPopMatrix()

    rest_C = (3.5, -4.84, 3.5) 
    fly_C = (1.0 + math.cos(time_counter*4)*0.5 + wind_drift, 1.0 + math.sin(time_counter*5)*0.4, 3.5)
    glPushMatrix()
    glTranslatef(lerp(rest_C[0], fly_C[0], wind_power), lerp(rest_C[1], fly_C[1], wind_power), lerp(rest_C[2], fly_C[2], wind_power))
    glRotatef(15, 0, 1, 0) 
    glRotatef(lerp(0, time_counter * 120 * max(1, fan_speed_level), wind_power), 0, 1, 1) 
    glScalef(0.5, 0.01, 0.7)
    draw_cube()
    glPopMatrix()