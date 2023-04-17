import pygame

# Initialisation de Pygame
pygame.init()

# Définition de la taille de la fenêtre
WINDOW_SIZE = (400, 400)

# Définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Définition des types de Pokémons
TYPES = ['Normal', 'Feu', 'Eau', 'Terre']

# Définition des couleurs associées à chaque type de Pokémon
TYPE_COLORS = {'Normal': (168, 168, 120), 'Feu': (240, 128, 48), 'Eau': (104, 144, 240), 'Terre': (120, 200, 80)}

# Création de la fenêtre
screen = pygame.display.set_mode(WINDOW_SIZE)

# Boucle principale
while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Effacement de l'écran
    screen.fill(WHITE)

    # Affichage des types de Pokémon
    for i, pokemon_type in enumerate(TYPES):
        # Calcul des coordonnées de chaque case
        x = (i % 6) * 60 + 20
        y = (i // 6) * 60 + 20

        # Affichage de la case
        pygame.draw.rect(screen, TYPE_COLORS[pokemon_type], (x, y, 50, 50))

        # Affichage du nom du type de Pokémon
        font = pygame.font.SysFont(None, 20)
        text = font.render(pokemon_type, True, BLACK)
        text_rect = text.get_rect(center=(x+25, y+35))
        screen.blit(text, text_rect)

    # Actualisation de l'affichage
    pygame.display.flip()
