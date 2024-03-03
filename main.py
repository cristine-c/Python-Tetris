import pygame, sys
# asterisk to import all the classses
from game import Game
from colors import Colors

pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)
# creates scoreboard rect object (top corner x, y, height, width)
score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)


# sets the display size (width * height)
screen = pygame.display.set_mode((500,620))
# sets title of the game
pygame.display.set_caption("Python Tetris")

# create a clock object to control the frame rate of game
clock = pygame.time.Clock()

# create a game object
game = Game()

# creates a timer to trigger game update event every ms
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

while True:
  for event in pygame.event.get():
    # if user clicks on X, quit program
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    # if player presses a key
    if event.type == pygame.KEYDOWN:
      if game.game_over == True:
        game.game_over = False
        game.reset()
      if event.key == pygame.K_LEFT and game.game_over == False:
        game.move_left()
      if event.key == pygame.K_RIGHT and game.game_over == False:
        game.move_right()
      if event.key == pygame.K_DOWN and game.game_over == False:
        game.move_down()
        game.update_score(0, 1)
      if event.key == pygame.K_UP and game.game_over == False:
        game.rotate()
    # automatically moves block down
    if event.type == GAME_UPDATE and game.game_over == False:
      game.move_down()
      
  score_value_surface = title_font.render(str(game.score), True, Colors.white)      
    
  # draws pictures based on changes made
  screen.fill(Colors.dark_blue)
  # blit = block image transfer
  screen.blit(score_surface, (365, 20, 50, 50))
  screen.blit(next_surface, (375, 180, 50, 50))

  if game.game_over:
    screen.blit(game_over_surface, (320, 450, 50, 50))
  # args: surface, color, object, outline, border radius
  pygame.draw.rect(screen, Colors.grey, score_rect, 0, 10)
  screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
  pygame.draw.rect(screen, Colors.grey, next_rect, 0, 10)
  game.draw(screen)
  
  pygame.display.update()
  # 60 frames per second
  clock.tick(60)