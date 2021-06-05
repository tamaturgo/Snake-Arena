import time
import menu
from src.model import ball
from src.model import apple
from src.constant import *

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake")

arena_bg = pygame.image.load("assets/images/arena.png")
sprite_trap = pygame.image.load("assets/images/trap.png")

sprite_apple = pygame.image.load("assets/images/apple.png")
sprite_body = pygame.image.load("assets/images/snake_body.png")
# Game Controllers
score = 0
game_cycle = True
game_over = False

# Snake Controller
speed_x = 32
speed_y = 0
last_key = 1
balls = []
list_snake = []
list_sprites = []
snake_head = [WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2]


def consult_score():
    file = open("data/score_file.txt", "r")
    record = int(file.read())
    file.close()
    return record


def update_score(current_score):
    if current_score > consult_score():
        file = open("data/score_file.txt", "w")
        file.write(str(score))
        file.close()


def reset_game():
    global speed_x, speed_y, balls, last_key, list_snake, list_sprites, game_over, score
    speed_x = 32
    speed_y = 0
    last_key = 1
    list_snake = []
    list_sprites = []
    balls = []
    game_over = False
    score = 0
    apple.apple_pos_xy = []


def draw_snake(list_position):
    index = 0
    global sprite_body
    for pos_xy in list_position:
        if not index == len(list_sprites) - 1:
            list_sprites[index] = sprite_body
        window.blit(list_sprites[index], [pos_xy[0], pos_xy[1]])
        index += 1
    if last_key == 0:
        assets_ref = pygame.image.load("assets/images/head_bottom.png")
    elif last_key == 1:
        assets_ref = pygame.image.load("assets/images/head_right.png")
    elif last_key == 2:
        assets_ref = pygame.image.load("assets/images/head_top.png")
    else:
        assets_ref = pygame.image.load("assets/images/head_left.png")
    list_sprites[len(list_sprites) - 1] = assets_ref


def snake_collision_wall():
    global game_over
    if 1 > snake_head[0] or snake_head[0] > 1186:
        game_over = True
        if snake_head[0] < 1:
            die_SFX.play()
            snake_head[0] = 15
        else:
            die_SFX.play()
            snake_head[0] = 1185
    if snake_head[1] < 70 or snake_head[1] > 641:
        game_over = True
        if snake_head[1] < 72:
            die_SFX.play()
            snake_head[1] = 73
        else:
            die_SFX.play()
            snake_head[1] = 640


def handle_events_on_game():
    global game_cycle, speed_y, speed_x, last_key
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_cycle = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_over:
                if 522 < pygame.mouse.get_pos()[0] < 700:
                    if 453 < pygame.mouse.get_pos()[1] < 532:
                        click_SFX.play()
                        menu.menu()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_cycle = False
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s) \
                    and not (last_key == 2):
                speed_y = 32
                speed_x = 0
                last_key = 0

            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) \
                    and not (last_key == 3):
                speed_y = 0
                speed_x = 32
                last_key = 1

            if (event.key == pygame.K_UP or event.key == pygame.K_w) \
                    and not (last_key == 0):
                speed_y = -32
                speed_x = 0
                last_key = 2

            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) \
                    and not (last_key == 1):
                speed_y = 0
                speed_x = -32
                last_key = 3


def main():
    global game_cycle, game_over, snake_head, score
    pos_x = 80 + WINDOW_WIDTH / 2
    pos_y = 72 + WINDOW_HEIGHT / 2
    list_snake.append(snake_head)
    list_sprites.append(sprite_body)

    while game_cycle:
        if not game_over:
            # position next move
            pos_x += speed_x
            pos_y += speed_y

            # Snake moving
            snake_head = [pos_x, pos_y]
            list_snake.append(snake_head)

            # Removing the last block
            if len(list_snake) > 1:
                del list_snake[0]

        # Snake collision with the body
        for i in list_snake[:-1]:
            if i == snake_head:
                game_over = True
                die_SFX.play()
                snake_head[0] -= 1
                snake_head[1] -= 1

        for i in list_snake:
            x = i[0]
            y = i[1]

            # Snake collision with the traps
            for j in range(len(balls)):
                if balls[j][0].collidepoint([x, y]):
                    game_over = True
                    die_SFX.play()
                    balls[j][1] *= -1

        # Traps Move
        for i in range(len(balls)):
            balls[i][0].x += balls[i][1]
            balls[i][0].y += balls[i][2]

            if balls[i][0].x > 1186 - 32 or balls[i][0].x < 14:
                balls[i][1] *= -1
            if balls[i][0].y > 700 - 60 or balls[i][0].y < 72:
                balls[i][2] *= -1

        # Apple Spawn
        if not apple.apple_pos_xy:
            balls.append([ball.init_ball(), BALL_SPEED_X, BALL_SPEED_Y])
            for i in range(5):
                apple.apple_pos_xy.append(apple.create_apple())

        # Collecting apples
        for i in range(len(apple.apple_pos_xy)):
            if snake_head[0] == apple.apple_pos_xy[i][0] and snake_head[1] + 2 == apple.apple_pos_xy[i][1]:
                apple.apple_pos_xy.remove(apple.apple_pos_xy[i])
                list_snake.append(snake_head)
                list_sprites.append(sprite_body)
                score += 1
                apple_SFX.play()
                break

        window.blit(arena_bg, (0, 0))
        handle_events_on_game()
        snake_collision_wall()
        draw_snake(list_snake)

        for i in range(len(balls)):
            window.blit(sprite_trap, (balls[i][0].x, balls[i][0].y))

        # Draw Apples
        for i in range(len(apple.apple_pos_xy)):
            window.blit(sprite_apple, apple.apple_pos_xy[i])

        # Score
        initial_score_text = font_30.render('%03d' % score,
                                            True, (242, 195, 82))
        initial_score_text_rect = initial_score_text.get_rect()
        initial_score_text_rect.center = (200, 40)

        record_score_text = font_30.render('%03d' % consult_score(),
                                           True, (242, 195, 82))
        record_score_text_rect = record_score_text.get_rect()
        record_score_text_rect.center = (1000, 40)
        update_score(score)

        window.blit(initial_score_text, initial_score_text_rect)
        window.blit(record_score_text, record_score_text_rect)
        if game_over:
            game_over_bg = pygame.image.load("assets/images/popup_game_over.png")
            if 522 < pygame.mouse.get_pos()[0] < 700:
                if 453 < pygame.mouse.get_pos()[1] < 532:
                    game_over_bg = pygame.image.load("assets/images/popup_game_over_pressed.png")
            window.blit(game_over_bg, (280, 200))
            initial_score_text = font_20.render('Your Score: %03d' % score,
                                                True, (242, 195, 82))
            initial_score_text_rect = initial_score_text.get_rect()
            initial_score_text_rect.center = (580, 380)
            window.blit(initial_score_text, initial_score_text_rect)

        pygame.display.flip()
        time.sleep(1 / FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
