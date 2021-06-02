from random import randint
import pygame as pygame
import sys
# from tkinter import messagebox
# import tkinter as tk

pygame.init()

u1 = pygame.USEREVENT
pygame.time.set_timer(u1, 200)
# u2 = pygame.USEREVENT + 1
# pygame.time.set_timer(u2, 4000)

W = 442
H = 800
RUN = 'run'
PAUSE = 'pause'
CARS = (r'pictures/car0_2.png', r'pictures/car1.png', r'pictures/car2.png', r'pictures/car3.png')
# для хранения готовых машин-поверхностей
CARS_SURF = []

dict_colors = {
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
    'BLUE': (173, 223, 237),
    'RED': (252, 61, 3),
    'ORANGE': (252, 186, 3),
    'YELLOW': (200, 255, 200)
}

# надо установить видео режим
# до вызова image.load()
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption('Crazy driver')

for i in range(len(CARS)):
    CARS_SURF.append(pygame.image.load(CARS[i]).convert_alpha())


class Car(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.surf = pygame.image.load(filename)
        self.rect = self.surf.get_rect(center=(x, y))


class CarGroup(pygame.sprite.Sprite):
    def __init__(self, surf):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.x = ar_line_x[randint(0, len(ar_line_x)) - 1] - line_width // 2
        self.rect = self.image.get_rect(center=(self.x, 0))
        # у машин будет разная скорость
        self.speed = randint(speed_cars // 2, speed_cars)
        self.speed_art = self.speed

    def update(self):
        if self.rect.y < H:
            self.rect.y += self.speed_art
        else:
            self.speed_art = self.speed
            self.x = ar_line_x[randint(0, len(ar_line_x)) - 1] - line_width // 2
            self.rect = self.image.get_rect(center=(self.x, 0))
            self.kill()
            # self.remove(cars)


def show_text(message, font_size, x=0, y=0):
    font_obj = pygame.font.Font('freesansbold.ttf', font_size)  # pygame.sont.SysFont('arial', 32)
    text_surf_obj = font_obj.render(message, True, dict_colors['BLACK'])  # create object from class Surface
    text_rect_obj = text_surf_obj.get_rect(center=(x, y))
    sc.blit(text_surf_obj, text_rect_obj)


def faced_head(surf1, surf2):
    return surf1.rect.top - 5 <= surf2.rect.bottom and \
           surf1.rect.left == surf2.rect.left


cars = pygame.sprite.Group()

main_car = Car(W // 2, H - 50, CARS[0])
car_width = 32
car_height = 50

change_x = 3
speed = 3
speed_cars = 16

line_width = 56
ar_line_x = [i for i in range(line_width, line_width * 8 + 1, line_width)]

car1 = CarGroup(CARS_SURF[1])
car2 = CarGroup(CARS_SURF[2])
car3 = CarGroup(CARS_SURF[3])
car4 = CarGroup(CARS_SURF[1])
car5 = CarGroup(CARS_SURF[2])
car6 = CarGroup(CARS_SURF[3])
car7 = CarGroup(CARS_SURF[1])
car8 = CarGroup(CARS_SURF[2])
car9 = CarGroup(CARS_SURF[3])
car10 = CarGroup(CARS_SURF[1])
car11 = CarGroup(CARS_SURF[2])
car12 = CarGroup(CARS_SURF[3])
car13 = CarGroup(CARS_SURF[1])
car14 = CarGroup(CARS_SURF[2])
car15 = CarGroup(CARS_SURF[3])
car16 = CarGroup(CARS_SURF[1])
car17 = CarGroup(CARS_SURF[2])
car18 = CarGroup(CARS_SURF[3])
car19 = CarGroup(CARS_SURF[1])
car20 = CarGroup(CARS_SURF[2])
car21 = CarGroup(CARS_SURF[3])
car22 = CarGroup(CARS_SURF[1])
car23 = CarGroup(CARS_SURF[2])

car1.add(cars)

ar_cars = [car1, car2, car3, car4, car5, car6, car7, car8, car9, car10, car11, car12, car13, car14, car15,
           car16, car17, car18, car19, car20, car21, car22, car23]
in_cars = [car1]
stop = 1
state = RUN

scores = 0

button_rect = pygame.Rect((W // 2 - 50, H - 300), (100, 100))

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:  #  or state != RUN:
            pygame.quit()
            sys.exit()
        elif i.type == u1 and state == RUN:  #  and stop:
            a = [i for i in ar_cars if i not in in_cars]
            a[randint(0, len(a)) - 1].add(cars)
            scores += 1
        elif i.type == pygame.MOUSEBUTTONDOWN and state != RUN:
            if button_rect.collidepoint(i.pos):
                state = RUN
                scores = 0
                for car in in_cars:
                    car.rect.y = 0
                    car.kill()
                in_cars = [car1]
                car1.add(cars)

    if state == RUN:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and main_car.rect.x > 0:
            main_car.rect.x -= change_x
        elif keys[pygame.K_RIGHT] and main_car.rect.x < W - car_width:
            main_car.rect.x += change_x

        if keys[pygame.K_UP] and main_car.rect.y > 0:  # i.key ==
            main_car.rect.y -= speed
        elif keys[pygame.K_DOWN] and main_car.rect.y < H - car_height:
            main_car.rect.y += speed

        sc.fill(dict_colors['YELLOW'])

        cars.draw(sc)

        for line in ar_line_x:
            pygame.draw.line(sc, dict_colors['BLACK'], [line, 0], [line, H], 3)

        sc.blit(main_car.surf, main_car.rect)
        show_text(f'{scores}', 14, x=10, y=6)

        pygame.display.update()
        # pygame.time.delay(20)
        pygame.time.Clock().tick(70)

        in_cars = [i for i in ar_cars if i in cars.sprites()]
        cars.update()
        if len(in_cars) >= 2:
            for c1 in range(len(in_cars) - 1):
                for c2 in range(c1 + 1, len(in_cars)):
                    if in_cars[c2].rect.y > in_cars[c1].rect.y:
                        if faced_head(in_cars[c2], in_cars[c1]):
                            in_cars[c1].rect.y -= 10
                            in_cars[c1].speed = in_cars[c2].speed_art
                    else:
                        if faced_head(in_cars[c1], in_cars[c2]):
                            in_cars[c2].rect.y -= 10
                            in_cars[c2].speed = in_cars[c1].speed_art

        if pygame.sprite.spritecollide(main_car, cars, False):  # collided=pygame.sprite.collide_circle):
            state = PAUSE
            sound_obj = pygame.mixer.music
            sound_obj.load(r'music\CrashAuto.mp3')
            sound_obj.play()
            pygame.time.delay(1500)
            # tk.Tk().wm_withdraw()
            # messagebox.showinfo(message=f'Your scores is [ {scores} ]. One more round?')

    else:
        sc.fill(dict_colors['WHITE'])
        show_text(f'Your scores is [ {scores} ]. One more round?', 20, x=W // 2, y=H // 2)
        # button
        pygame.draw.rect(sc, dict_colors['ORANGE'], button_rect)
        load_surf = pygame.image.load(r'pictures\reload-icon_removebg.png').convert_alpha()
        sc.blit(load_surf, button_rect)
        pygame.draw.rect(sc, dict_colors['BLACK'], button_rect, 4)
        pygame.display.update()

