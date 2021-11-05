import pygame
import math
import  os

pygame.init()
pygame.font.init()
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400

A = 65

word = "DEVELOPER"

guessed = ['D']

img_status = 1

for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])


def draw():
    WIN.fill(BLACK)

    display_word = ""

    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "

    font = pygame.font.SysFont(None, 40)
    img = font.render(display_word, 1, WHITE)
    WIN.blit(img, (400, 200))

    for i in range(6):
        WIN.blit(pygame.image.load(os.path.join('C:/Users/PC/Desktop/Python/games/hangman/images', 
    'hangman' + str(img_status) + '.png'
)), (100, 100))

    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(WIN, WHITE, (x, y), RADIUS, 3)

            font = pygame.font.SysFont(None, 40)
            img = font.render(ltr, 1, WHITE)
            WIN.blit(img, (x - img.get_width() / 2, y - img.get_width() / 2))

def display_alert(text):
    WIN.fill(BLACK)
    font = pygame.font.SysFont(None, 40)
    img = font.render(text, 1, WHITE)
    WIN.blit(img, (WIDTH / 2 - img.get_width() / 2, HEIGHT / 2 - img.get_width() / 2))
    pygame.display.update()
    pygame.time.delay(3000)

def main():
    run = True

    global img_status

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                    if dis < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            img_status += 1

        won = True
        for letter in word:
            if letter not in guessed:
                won = False

        if won:
            display_alert('You won!!')
            break
        if img_status == 6:
            display_alert('You lost!!')
            break

        draw()
        pygame.display.update()    
    pygame.quit()


if __name__ == '__main__':
    main()