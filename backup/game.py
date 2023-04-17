import pygame
import pytmx
import pyscroll

from player import Player

pygame.init()

class Game:

    def __init__(self):
        # la fenetre
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pokemon - Le Jeu")

        #carte du jeu
        self.map = "carte"
        tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data,self.screen.get_size())
        # pour zoomer *2 :
        map_layer.zoom = 2

        # joueur
        player_position = tmx_data.get_object_by_name("spawn")
        self.player = Player(player_position.x, player_position.y)

        #collision
        self.walls = []
        for obj in tmx_data.objects:
            try:
                if obj.properties["area_type"] == "collision":
                    self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            except Exception as e:
                print("No attribute", e)

        # dessiner les calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        # rect collision enter_house
        enter_house = tmx_data.get_object_by_name('enter_house')
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animation('up')
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation('down')
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation('left')
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation('right')

    def switch_map(self, target, point):
        # carte des maisons
        tmx_data = pytmx.util_pygame.load_pygame(target+'.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        # pour zoomer *2 :
        map_layer.zoom = 2

        # collision
        self.walls = []
        for obj in tmx_data.objects:
            try:
                if obj.properties["area_type"] == "collision":
                    self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            except Exception as e:
                print("No attribute", e)

        # dessiner les calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        # rect collision enter_house
        enter_house = tmx_data.get_object_by_name('exit_house')
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

        # spawn maison
        spawn_house_point = tmx_data.get_object_by_name('spawn_house')
        self.player.position[0] = spawn_house_point.x
        self.player.position[1] = spawn_house_point.y - 50

    def switch_house(self):
        # carte des maisons
        tmx_data = pytmx.util_pygame.load_pygame('house.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        # pour zoomer *2 :
        map_layer.zoom = 2

        # collision
        self.walls = []
        for obj in tmx_data.objects:
            try:
                if obj.properties["area_type"] == "collision":
                    self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            except Exception as e:
                print("No attribute", e)

        # dessiner les calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        # rect collision enter_house
        enter_house = tmx_data.get_object_by_name('exit_house')
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

        # spawn maison
        spawn_house_point = tmx_data.get_object_by_name('spawn_house')
        self.player.position[0] = spawn_house_point.x
        self.player.position[1] = spawn_house_point.y - 50

    def switch_world(self):
        # carte des maisons
        tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        # pour zoomer *2 :
        map_layer.zoom = 2

        # collision
        self.walls = []
        for obj in tmx_data.objects:
            try:
                if obj.properties["area_type"] == "collision":
                    self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            except Exception as e:
                print("No attribute", e)

        # dessiner les calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        # rect collision enter_house
        enter_house = tmx_data.get_object_by_name('enter_house')
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

        # spawn dvt maison
        spawn_house_point = tmx_data.get_object_by_name('enter_house_exit')
        self.player.position[0] = spawn_house_point.x
        self.player.position[1] = spawn_house_point.y +20






    def switch_house1(self):
        # carte des maisons
        tmx_data = pytmx.util_pygame.load_pygame('house1.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        # pour zoomer *2 :
        map_layer.zoom = 2

        # collision
        self.walls = []
        for obj in tmx_data.objects:
            try:
                if obj.properties["area_type"] == "collision":
                    self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            except Exception as e:
                print("No attribute", e)

        # dessiner les calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        # rect collision enter_house
        enter_house1 = tmx_data.get_object_by_name('exit_house1')
        self.enter_house1_rect = pygame.Rect(enter_house1.x, enter_house1.y, enter_house1.width, enter_house1.height)

        # spawn maison
        spawn_house1_point = tmx_data.get_object_by_name('spawn_house1')
        self.player.position[0] = spawn_house1_point.x
        self.player.position[1] = spawn_house1_point.y - 50

    def switch_world1(self):
        # carte des maisons
        tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        # pour zoomer *2 :
        map_layer.zoom = 2

        # collision
        self.walls = []
        for obj in tmx_data.objects:
            try:
                 if obj.properties["area_type"] == "collision":
                    self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
            except Exception as e:
                print("No attribute", e)

        # dessiner les calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        # rect collision enter_house
        enter_house1 = tmx_data.get_object_by_name('enter_house1')
        self.enter_house1_rect = pygame.Rect(enter_house1.x, enter_house1.y, enter_house1.width, enter_house1.height)

        # spawn dvt maison
        spawn_house_point1 = tmx_data.get_object_by_name('enter_house_exit1')
        self.player.position[0] = spawn_house_point.x
        self.player.position[1] = spawn_house_point.y + 20








    def update(self):
        self.group.update()

        # enter maison
        if self.map == 'world' and self.player.feet.colliderect(self.enter_house_rect):
            self.switch_house()
            self.map = 'house'

        # enter maison
        if self.map == 'house' and self.player.feet.colliderect(self.enter_house_rect):
            self.switch_world()
            self.map = 'world'


        # collision
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back()

    def run(self):
        clock = pygame.time.Clock()
        # boucle
        running = True

        while running:
            self.player.save_location()
            self.handle_input()
            self.update()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick((60))

        pygame.quit()