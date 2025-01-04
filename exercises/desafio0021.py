"""
Escreva um programa em Python que abra e reproduza um arquivo do tipo .mp3.
"""

import pygame

# Inicializa o mixer de áudio do pygame
pygame.mixer.init()

# Carrega o arquivo mp3
pygame.mixer.music.load('scom.mp3')

# Reproduz o arquivo
pygame.mixer.music.play()

# Mantém o programa rodando enquanto a música é reproduzida
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)  # Espera até que a música termine
