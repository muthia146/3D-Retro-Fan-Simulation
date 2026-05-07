from OpenGL.GL import *
from OpenGL.GLU import *
from scene import set_material, draw_cube

def draw_fan(fan_speed_level, blade_angle, head_pan_angle):
    glPushMatrix()
    
    glTranslatef(0.0, -1.99, 0.0) 
    
    quadric = gluNewQuadric()
    
    # 1. BASE (Dudukan)
    glPushMatrix()
    set_material("chrome", (0.6, 0.5, 0.4, 1.0))
    glTranslatef(0.0, -0.8, 0.0)
    glRotatef(-90, 1, 0, 0)
    gluCylinder(quadric, 1.2, 1.2, 0.2, 32, 1)
    glTranslatef(0, 0, 0.2)
    gluDisk(quadric, 0, 1.2, 32, 1)
    
    # Tombol Kecepatan
    colors = [(0,0,1,1), (0,1,0,1), (1,0,0,1), (1,1,0,1)]
    for i, col in enumerate(colors):
        glPushMatrix()
        set_material("matte", col)
        glTranslatef(-0.4 + (i*0.25), -0.8, 0.05)
        if i == fan_speed_level: glTranslatef(0, 0, -0.05) 
        gluSphere(quadric, 0.08, 16, 16)
        glPopMatrix()
        
    # Lampu Indikator Power
    glPushMatrix()
    if fan_speed_level > 0:
        set_material("emission", (0.0, 1.0, 0.0, 1.0))
    else:
        set_material("matte", (0.4, 0.0, 0.0, 1.0))
    glTranslatef(-0.7, -0.5, 0.05)
    gluSphere(quadric, 0.05, 16, 16)
    glPopMatrix()
    glPopMatrix()

    # 2. NECK & JOINT
    glPushMatrix()
    set_material("chrome", (0.5, 0.5, 0.5, 1.0))
    glTranslatef(0, -0.6, 0)
    glRotatef(-90, 1, 0, 0)
    # Tiang dibikin tinggi (2.5) biar elegan
    gluCylinder(quadric, 0.1, 0.1, 2.5, 16, 1)
    glPopMatrix()
    
    # Poros geleng disesuaikan tinggi tiang
    glTranslatef(0, 1.9, 0)
    gluSphere(quadric, 0.15, 16, 16)

    # 3. KEPALA KIPAS (Osilasi)
    glRotatef(head_pan_angle, 0, 1, 0)
    
    glPushMatrix()
    set_material("chrome", (0.6, 0.5, 0.4, 1.0))
    glTranslatef(0, 0, -0.8)
    gluCylinder(quadric, 0.35, 0.35, 0.8, 32, 1)
    glRotatef(180, 1, 0, 0)
    gluSphere(quadric, 0.35, 32, 32)
    glPopMatrix()

    # JARING PELINDUNG
    glPushMatrix()
    set_material("chrome", (0.8, 0.8, 0.8, 1.0))
    glTranslatef(0, 0, 0.2)
    
    gluQuadricDrawStyle(quadric, GLU_LINE)
    glPushMatrix()
    glScalef(1.0, 1.0, 0.25)
    gluSphere(quadric, 1.5, 30, 15) 
    glPopMatrix()
    
    gluQuadricDrawStyle(quadric, GLU_FILL)
    glPushMatrix()
    gluCylinder(quadric, 1.5, 1.5, 0.05, 32, 1)
    glPopMatrix()
    glPopMatrix()

    # PLAT MERK
    glPushMatrix()
    set_material("chrome", (1.0, 0.9, 0.5, 1.0))
    glTranslatef(0, 0, 0.6)
    gluDisk(quadric, 0, 0.25, 32, 1)
    glPopMatrix()

    # 4. BALING-BALING
    glPushMatrix()
    glTranslatef(0, 0, 0.1)
    glRotatef(blade_angle, 0, 0, 1)
    
    set_material("matte", (0.9, 0.85, 0.7, 1.0)) # Baling-baling warna Cream/Ivory
    for i in range(3):
        glPushMatrix()
        glRotatef(i * 120, 0, 0, 1)
        glTranslatef(0, 0.65, 0)
        glRotatef(15, 0, 1, 0)
        glScalef(0.4, 1.3, 0.02) 
        draw_cube()
        glPopMatrix()
    glPopMatrix()
    
    glPopMatrix() 