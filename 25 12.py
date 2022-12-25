import pygame
import sys
 
# здесь определяются константы,
# классы и функции
FPS = 60
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1000
STACK_WIDTH = 20
STACK_HEIGHT= 120
STACK_OFFSET = 1110
STICK_WIDTH = 20
STICK_HEIGHT = 120
STICK_OFFSET = 10
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
 
# здесь происходит инициация,
# создание объектов
pygame.init()
sc = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
# радиус мяча
r = 20
# координаты мяча
ball_x = SCREEN_WIDTH//2
ball_y = SCREEN_HEIGHT // 2
# скорости мяча
ball_speed_x = 5
ball_speed_y = 4
#Кординаты ракетки
stack_x =STACK_OFFSET
stack_y = (SCREEN_HEIGHT - STACK_HEIGHT) //2
stick_x =STICK_OFFSET
stick_y =(SCREEN_HEIGHT - STICK_HEIGHT) // 2
#скорость ракетки
stack_speed_y =0
stick_speed_y =0
# главный цикл
while True:
    # задержка
    clock.tick(FPS)
    # цикл обработки событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
    # --------
    # изменение объектов
    # --------
    # передвигаем мяч по экрану
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    # Выход за края экрана
    # левый
    if ball_x <= r:
        # летел налево - полетел направо
        ball_speed_x = -ball_speed_x
    # правый
    if ball_x >= SCREEN_WIDTH - r:
        # летел направо - полетел налево
        ball_speed_x = -ball_speed_x
    #Верхний
    if ball_y <=r:
        ball_speed_y = -ball_speed_y
    #Нижний
    if ball_y >= SCREEN_HEIGHT - r:
        ball_speed_y = -ball_speed_y
    #передвигаем ракетку по экрану
    stick_y +=stick_speed_y
    stack_y +=stack_speed_y
    if stick_y <=0:
        stick_y =0
    elif stick_y >= SCREEN_HEIGHT - STICK_HEIGHT:
        stick_y = SCREEN_HEIGHT - STICK_HEIGHT
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        stick_y -= 15
    elif keys[pygame.K_DOWN]:
        stick_y += 15
    
    # обновление экрана
    # заливаем фон
    sc.fill(BLACK)
    # рисуем круг
    pygame.draw.circle(sc, ORANGE,(ball_x, ball_y), r)
    pygame.draw.rect(sc,ORANGE, (stick_x, stick_y, STICK_WIDTH, STICK_HEIGHT))
    pygame.draw.rect(sc,ORANGE, (stack_x, stack_y, STACK_WIDTH, STACK_HEIGHT))
    pygame.display.update()
    
