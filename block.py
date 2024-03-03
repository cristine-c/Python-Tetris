from colors import Colors
import pygame
from position import Position


class Block():

  def __init__(self, id):
    self.id = id
    self.cells = {}
    self.cell_size = 30
    self.rotation = 0
    self.row_offset = 0
    self.col_offset = 0
    self.colors = Colors.get_cell_colors()

  def move(self, rows, cols):
    self.row_offset += rows
    self.col_offset += cols

  def get_cell_positions(self):
    tiles = self.cells[self.rotation]
    moved_tiles = []
    for position in tiles:
      position = Position(position.row + self.row_offset,
                          position.col + self.col_offset)
      moved_tiles.append(position)
    return moved_tiles

  def rotate(self):
    # rotate though block positions
    self.rotation = (self.rotation + 1) % len(self.cells)

  def undo_rotation(self):
    self.rotation = (self.rotation - 1) % len(self.cells)

  def draw(self, screen, offset_x=0, offset_y=0):
    tiles = self.get_cell_positions()
    for tile in tiles:
      tile_rect = pygame.Rect((tile.col * self.cell_size) + offset_x,
                              (tile.row * self.cell_size) + offset_y,
                              self.cell_size - 1, self.cell_size - 1)
      pygame.draw.rect(screen, self.colors[self.id], tile_rect)
