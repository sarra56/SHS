import pygame

# Charger les images des tiles
grass = pygame.image.load("assets/grass.png")
noir = pygame.image.load("assets/noir.png")
sol = pygame.image.load("assets/sol.png")
blue1 = pygame.image.load("assets/blue1.png")
blue2 = pygame.image.load("assets/blue2.png")
blue3 = pygame.image.load("assets/blue3.png")
blue4 = pygame.image.load("assets/blue4.png")
blue1_2 = pygame.image.load("assets/blue1-2.png")
blue1_2_2 = pygame.image.load("assets/blue1-2-2.png")
blue2_3 = pygame.image.load("assets/blue2-3.png")
blue2_3_2 = pygame.image.load("assets/blue2-3-2.png")
blue3_4 = pygame.image.load("assets/blue3-4.png")
blue3_4_2 = pygame.image.load("assets/blue3-4-2.png")
rectangle = pygame.image.load("assets/rectangle3.png")
tree_height = pygame.image.load("assets/tree_height.png")
tree_root = pygame.image.load("assets/tree_root.png")
rock = pygame.image.load("assets/rock.png")

# Organiser les tiles dans un dictionnaire
tiles = {
    0: noir,
    1: sol,
    2: grass,
    3: blue1,
    4: blue2,
    5: blue3,
    6: blue4,
    7: blue1_2,
    8: blue1_2_2,
    9: blue2_3,
    10: blue2_3_2,
    11: blue3_4,
    12: blue3_4_2,
    13: rectangle,
    14: rock,
    15: tree_height,
    16: tree_root
}

# Carte du jeu
game_map = [
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [13, 3, 13, 13, 3, 13, 13, 13, 13, 3, 13, 13],
    [15, 3, 15, 15, 3, 15, 15, 15, 15, 3, 15, 15],
    [16, 14, 16, 16, 14, 16, 16, 16, 16, 14, 16, 16],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],   
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

# Initialisation de Pygame
pygame.init()

# Taille des tiles
TILE_SIZE = 48  # Taille des images : 48x48

# Dimensions de l'écran
SCREEN_WIDTH = len(game_map[0]) * TILE_SIZE
SCREEN_HEIGHT = len(game_map) * TILE_SIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mon Jeu")

# Couleur de fond
BG_COLOR = (0, 0, 0)  # Noir

# Fonction pour dessiner la carte
def draw_map():
    for y, row in enumerate(game_map):
        for x, tile_id in enumerate(row):
            if tile_id in tiles:  # S'assurer que le tile existe
                screen.blit(tiles[tile_id], (x * TILE_SIZE, y * TILE_SIZE))

# Boucle principale du jeu
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Remplir l'écran avec la couleur de fond
    screen.fill(BG_COLOR)

    # Dessiner la carte
    draw_map()

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Limiter la vitesse de la boucle
    clock.tick(60)

pygame.quit()
