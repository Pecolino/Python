import pygame
from pygame.locals import *
import keyboard
from pynput.mouse import Controller, Button
import pyautogui
import win32api, win32con

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("Nenhum controle encontrado.")

mouse = Controller()
controle = pygame.joystick.Joystick(0)
controle.init()

#print do controle conectado
print ("Controle Conectado", controle.get_name())

#loop do código
while True:
    
    #pegando a cordeda do mouse
    
    #apertando botões
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            print(f'Botão pressionado: {event.button}')
            if event.button == 0:
                keyboard.press (" ")
            elif event.button == 1:
                keyboard.press ("g")
            elif event.button == 2:
                keyboard.press ("f")
            elif event.button == 3:
                keyboard.press ("x")
            elif event.button == 9:
                keyboard.press ("h")
            elif event.button == 10:
                keyboard.press ("t")
    
    #soltando botões            
        if event.type == pygame.JOYBUTTONUP:
            print(f'Botão pressionado: {event.button}')
            if event.button == 0:
                keyboard.release (" ")
            elif event.button == 1:
                keyboard.release ("g")
            elif event.button == 2:
                keyboard.release ("f")
            elif event.button == 3:
                keyboard.release ("x")
            elif event.button == 9:
                keyboard.release ("h")
            elif event.button == 10:
                keyboard.release ("t")
    
    #declarando variaveis correspondentes aos analógicos e gatilhos           
    eixoXE = controle.get_axis(0)
    eixoYE = controle.get_axis(1)
    eixoXD = controle.get_axis(2)
    eixoYD = controle.get_axis(3)
    eixoGatilhoE = controle.get_axis(4)
    eixoGatilhoD = controle.get_axis(5)
    
    #limitar cordenada dos analógicos e gatilhos
    limitar = 0.4
    
    #analógico esquerdo
    if eixoXE < -limitar:
        keyboard.press ("a")
    else: keyboard.release ("a")
    
    if eixoXE > limitar:
        keyboard.press ("d")
    else: keyboard.release ("d")
    
    if eixoYE < -limitar:
        keyboard.press ("w")
    else: keyboard.release ("w")
    
    if eixoYE > limitar:
        keyboard.press ("s")
    else: keyboard.release ("s")
    
    #analógico direito
    if eixoXD < -limitar:
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(-20), int(0), 0, 0)
    if eixoXD > limitar:
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(20), int(0), 0, 0)
    if eixoYD < -limitar:
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(0), int(-20), 0, 0)
    if eixoYD > limitar:
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(0), int(20), 0, 0)
        
    #gatilho esquerdo
    if eixoGatilhoE > limitar:
        mouse.click(Button.right)
        
    if eixoGatilhoD > limitar:
        mouse.click(Button.left)
        
    pygame.time.wait(10)