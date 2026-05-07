import sys
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Import fungsi dari file modular kita
from scene import init_environment, draw_room, draw_table, draw_socket_and_cable, draw_flying_papers
from fan import draw_fan

# --- VARIABEL GLOBAL & STATE ---
cam_angle_x = 15.0
cam_angle_y = 30.0
cam_zoom = -12.0

fan_speed_level = 0
blade_angle = 0.0
head_pan_angle = 0.0
head_pan_dir = 1
time_counter = 0.0
wind_power = 0.0 
is_oscillating = True

# Variabel deteksi klik mouse
mouse_down = False

def main():
    global cam_angle_x, cam_angle_y, cam_zoom
    global fan_speed_level, blade_angle, head_pan_angle, head_pan_dir, time_counter, wind_power
    global mouse_down
    global is_oscillating

    pygame.init()
    display = (1000, 700)
    pygame.display.set_mode(display, int(DOUBLEBUF) | int(OPENGL))
    pygame.display.set_caption("Simulasi Kipas Angin Modular - Final Project")

    init_environment()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (display[0] / display[1]), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

    clock = pygame.time.Clock()

    while True:
        dt = clock.tick(60) / 1000.0
        time_counter += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # --- KONTROL KECEPATAN (KEYBOARD) ---
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0: fan_speed_level = 0
                if event.key == pygame.K_1: fan_speed_level = 1
                if event.key == pygame.K_2: fan_speed_level = 2
                if event.key == pygame.K_3: fan_speed_level = 3
                if event.key == pygame.K_o:
                    is_oscillating = not is_oscillating

            # --- KONTROL KAMERA (MOUSE) ---
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Klik Kiri Mouse ditahan
                    mouse_down = True
                    pygame.mouse.get_rel()  # Reset titik awal tarikan mouse
                elif event.button == 4:  # Roda Mouse Scroll UP (Zoom In)
                    cam_zoom += 1.0
                elif event.button == 5:  # Roda Mouse Scroll DOWN (Zoom Out)
                    cam_zoom -= 1.0
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Klik Kiri Mouse dilepas
                    mouse_down = False
            
            if event.type == pygame.MOUSEMOTION:
                if mouse_down:  # Kalau mouse digeser sambil ditahan
                    dx, dy = event.rel
                    cam_angle_y += dx * 0.5  # Angka 0.5 ini sensitivitasnya
                    cam_angle_x += dy * 0.5

        # --- KONTROL KAMERA (KEYBOARD) - Tetap Ada ---
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]: cam_angle_y -= 2
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: cam_angle_y += 2
        if keys[pygame.K_UP] or keys[pygame.K_w]: cam_angle_x -= 2
        if keys[pygame.K_DOWN] or keys[pygame.K_s]: cam_angle_x += 2
        if keys[pygame.K_q]: cam_zoom += 0.2  # Zoom In pakai Q
        if keys[pygame.K_e]: cam_zoom -= 0.2  # Zoom Out pakai E

        # Update Animasi (Fisika)
        if fan_speed_level > 0:
            wind_power = min(1.0, wind_power + dt * 0.5) 
            blade_angle -= (15 * fan_speed_level)

            if is_oscillating:
                head_pan_angle += (30 * dt) * head_pan_dir
                if head_pan_angle > 45 or head_pan_angle < -45:
                    head_pan_dir *= -1
        else:
            wind_power = max(0.0, wind_power - dt * 3.0)

        # Proses Rendering
        glClear(int(GL_COLOR_BUFFER_BIT) | int(GL_DEPTH_BUFFER_BIT))  # type: ignore
        glLoadIdentity()
        
        # Eksekusi Transformasi Kamera
        glTranslatef(0.0, 0.0, cam_zoom)
        glRotatef(cam_angle_x, 1, 0, 0)
        glRotatef(cam_angle_y, 0, 1, 0)

        # Menggambar Scene dari file-file modular
        draw_room()
        draw_socket_and_cable()
        draw_table()
        draw_fan(fan_speed_level, blade_angle, head_pan_angle)
        draw_flying_papers(time_counter, wind_power, fan_speed_level, head_pan_angle)

        pygame.display.flip()

if __name__ == "__main__":
    main()